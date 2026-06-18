"""
Lab 4: Moderação de Avaliações de Produtos da Zava
=================================================
Um pipeline funcional de moderação de avaliações de produtos para a Zava, uma
varejista global de melhoria residencial, usando modelos hospedados no Microsoft Foundry.

Uso:
    python 02_comment_moderation.py                          # Processar comentários de exemplo
    python 02_comment_moderation.py --interactive            # Modo interativo
    python 02_comment_moderation.py --file sample_comments_pt_br.json  # A partir de arquivo
"""

import argparse
import json
import os
import sys

# Ensure UTF-8 output on Windows (cp1252 cannot encode emoji)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

from azure.ai.projects import AIProjectClient
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# System prompt -- the core of the moderation logic
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """Você é um sistema de moderação de avaliações de produtos para a Zava, uma varejista global de melhoria residencial. Analise a avaliação do cliente fornecida e classifique-a.

Responda SOMENTE com JSON válido neste formato exato:
{
    "classification": "<SAFE|NEEDS_REVIEW|UNSAFE>",
    "confidence": <0.0-1.0>,
    "reason": "<breve explicação>"
}

Regras de classificação:
- SAFE: Feedback construtivo sobre o produto, dúvidas sobre instalação, experiências positivas, observações neutras sobre produtos ou serviços
- NEEDS_REVIEW: Conteúdo no limite, reclamações fortes sobre produtos ou equipe, potencial sarcasmo, frustração sem abuso
- UNSAFE: Discurso de ódio, ameaças contra funcionários ou clientes, assédio, conteúdo explícito, ataques pessoais

Não inclua nenhum texto fora do objeto JSON."""

# ---------------------------------------------------------------------------
# Sample comments for demonstration
# ---------------------------------------------------------------------------
SAMPLE_COMMENTS = [
    "Adoro esta furadeira sem fio! A bateria dura o dia todo e o torque é impressionante.",
    "Essa tinta é um lixo e quem a projetou deveria ser demitido.",
    "Vocês todos são idiotas se compram aqui -- pior loja de todas.",
    "Esse stain para deck funciona em madeira tratada a pressão?",
    "Hmmm, o cortador de azulejos é razoável. Não é ótimo, não é terrível.",
]


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------
def classify_comment(client, model: str, comment: str) -> dict:
    """Send a comment to the model and get a structured classification."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": comment},
            ],
            temperature=0.0,
        )
    except Exception as e:
        if "content_filter" in str(e) or "content management policy" in str(e):
            return {
                "classification": "UNSAFE",
                "confidence": 1.0,
                "reason": "Bloqueado pelo filtro de segurança de conteúdo da Azure.",
            }
        raise

    raw = response.choices[0].message.content.strip()
    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        result = {
            "classification": "NEEDS_REVIEW",
            "confidence": 0.0,
            "reason": f"Model returned non-JSON response: {raw[:100]}",
        }

    return result


def apply_moderation(result: dict) -> str:
    """Apply business logic to determine the moderation action."""
    classification = result.get("classification", "NEEDS_REVIEW")
    confidence = result.get("confidence", 0.0)

    if classification == "SAFE" and confidence >= 0.8:
        return "APPROVED"
    elif classification == "UNSAFE" and confidence >= 0.7:
        return "BLOCKED"
    else:
        return "FLAGGED_FOR_REVIEW"


def moderate_comment(client, model: str, comment: str) -> dict:
    """Full moderation pipeline: classify → apply logic → return result."""
    classification = classify_comment(client, model, comment)
    action = apply_moderation(classification)
    return {
        "comment": comment,
        "classification": classification.get("classification", "UNKNOWN"),
        "confidence": classification.get("confidence", 0.0),
        "reason": classification.get("reason", ""),
        "action": action,
    }


ACTION_ICONS = {
    "APPROVED": "\u2705",
    "BLOCKED": "\U0001f6ab",
    "FLAGGED_FOR_REVIEW": "\U0001f50d",
}


def print_result(result: dict, index: int = None, total: int = None):
    """Exibe um resultado de moderação de forma legível."""
    header = f"--- Comentário {index}/{total} ---" if index else "---"
    icon = ACTION_ICONS.get(result["action"], "")
    print(header)
    print(f'Comentário:  "{result["comment"]}"')
    print(
        f"Classificação: {result['classification']} "
        f"(confiança: {result['confidence']:.2f})"
    )
    print(f"Motivo:  {result['reason']}")
    print(f"Ação:  {icon} {result['action']}")
    print()


# ---------------------------------------------------------------------------
# Execution modes
# ---------------------------------------------------------------------------
def run_samples(client, model: str):
    """Processa os comentários de exemplo incorporados."""
    print(f"\nProcessando {len(SAMPLE_COMMENTS)} comentários de exemplo...\n")
    results = []
    for i, comment in enumerate(SAMPLE_COMMENTS, 1):
        result = moderate_comment(client, model, comment)
        print_result(result, index=i, total=len(SAMPLE_COMMENTS))
        results.append(result)
    print_summary(results)


def run_file(client, model: str, filepath: str):
    """Processa comentários a partir de um arquivo JSON."""
    with open(filepath, "r", encoding="utf-8") as f:
        comments = json.load(f)

    print(f"\nProcessando {len(comments)} comentários de {filepath}...\n")
    results = []
    for i, item in enumerate(comments, 1):
        comment = item if isinstance(item, str) else item.get("comment", "")
        result = moderate_comment(client, model, comment)
        print_result(result, index=i, total=len(comments))
        results.append(result)
    print_summary(results)


def run_interactive(client, model: str):
    """Modo interativo -- digite comentários para classificar em tempo real."""
    print("\nModo interativo. Digite um comentário e pressione Enter.")
    print("Digite 'quit' para sair.\n")
    while True:
        try:
            comment = input("Digite um comentário: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if comment.lower() in ("quit", "exit", "q"):
            break
        if not comment:
            continue
        result = moderate_comment(client, model, comment)
        print_result(result)


def print_summary(results: list[dict]):
    """Print a summary of moderation actions."""
    print("=" * 40)
    print("  Summary")
    print("=" * 40)
    total = len(results)
    counts = {}
    for r in results:
        counts[r["action"]] = counts.get(r["action"], 0) + 1
    print(f"Total comments: {total}")
    for action in ("APPROVED", "FLAGGED_FOR_REVIEW", "BLOCKED"):
        print(f"  {action + ':':21s} {counts.get(action, 0)}")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    model = os.environ.get("MODEL_DEPLOYMENT_NAME")

    if not endpoint or endpoint.startswith("https://<"):
        print("ERRO: Defina PROJECT_ENDPOINT no seu arquivo .env (veja Lab 2).")
        sys.exit(1)
    if not model:
        print("ERRO: Defina MODEL_DEPLOYMENT_NAME no seu arquivo .env.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Sistema de moderação de comentários")
    parser.add_argument("--interactive", action="store_true", help="Modo interativo")
    parser.add_argument("--file", type=str, help="Caminho para arquivo JSON com comentários")
    args = parser.parse_args()

    # --- Connect ---
    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )
    inference_client = project_client.get_openai_client()

    print("=" * 40)
    print("  Sistema de moderação de comentários")
    print(f"  Modelo: {model}")
    print("=" * 40)

    try:
        if args.interactive:
            run_interactive(inference_client, model)
        elif args.file:
            run_file(inference_client, model, args.file)
        else:
            run_samples(inference_client, model)
    except HttpResponseError as e:
        if e.status_code == 429:
            print("ERRO: Limite de taxa atingido. Aguarde um momento e tente novamente.")
        elif e.status_code == 401:
            print("ERRO: Falha de autenticação. Execute 'az login' e tente novamente.")
        else:
            print(f"ERRO: {e.message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
