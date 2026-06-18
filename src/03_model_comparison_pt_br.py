"""
Lab 5: Comparação de Modelos para Moderação de Avaliações da Zava
================================================================
Compare como diferentes modelos classificam as mesmas avaliações de produtos da Zava.
Mede concordância, confiança e latência.

Uso:
    python 03_model_comparison.py              # Comparação lado a lado
    python 03_model_comparison.py --hybrid     # Modo de escalonamento híbrido
"""

import argparse
import json
import os
import sys
import time

# Ensure UTF-8 output on Windows (cp1252 cannot encode emoji)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

# Reuse the same system prompt from Lab 4
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

TEST_COMMENTS = [
    "Adoro esta furadeira sem fio! A bateria dura o dia todo e o torque é impressionante.",
    "Essa tinta é um lixo e quem a projetou deveria ser demitido.",
    "Vocês todos são idiotas se compram aqui -- pior loja de todas.",
    "Esse stain para deck funciona em madeira tratada a pressão?",
    "Os funcionários são inúteis e feios -- nunca mais volto a essa loja da Zava.",
    "Hmmm, o cortador de azulejos é razoável. Não é ótimo, não é terrível.",
    "Discordo respeitosamente das avaliações de 5 estrelas -- a lixadeira vibra demais.",
    "LOL a Zava vende tralha cara, eles estão se esforçando mesmo???",
]


def classify_comment(client, model: str, comment: str) -> dict:
    """Classify a single comment using the given model."""
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
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "classification": "NEEDS_REVIEW",
            "confidence": 0.0,
            "reason": f"Non-JSON response: {raw[:80]}",
        }


def compare_models(client, models: list[str], comment: str) -> list[dict]:
    """Run the same comment through multiple models and collect results."""
    results = []
    for model in models:
        start = time.time()
        result = classify_comment(client, model, comment)
        elapsed = time.time() - start
        results.append(
            {
                "model": model,
                "classification": result["classification"],
                "confidence": result["confidence"],
                "reason": result["reason"],
                "latency_ms": round(elapsed * 1000),
            }
        )
    return results


def hybrid_classify(
    client, primary: str, secondary: str, comment: str, threshold: float = 0.8
) -> dict:
    """Use the primary model first; escalate to secondary if confidence is low."""
    start = time.time()
    result = classify_comment(client, primary, comment)
    primary_latency = round((time.time() - start) * 1000)

    escalated = False
    if result["confidence"] < threshold:
        start = time.time()
        result = classify_comment(client, secondary, comment)
        secondary_latency = round((time.time() - start) * 1000)
        escalated = True
        total_latency = primary_latency + secondary_latency
        model_used = secondary
    else:
        total_latency = primary_latency
        model_used = primary

    return {
        "comment": comment,
        "model_used": model_used,
        "escalated": escalated,
        "classification": result["classification"],
        "confidence": result["confidence"],
        "reason": result["reason"],
        "latency_ms": total_latency,
    }


def run_comparison(client, models: list[str]):
    """Side-by-side comparison of models on all test comments."""
    print("=" * 60)
    print("  Comparação de Modelos: Moderação de Comentários")
    print("=" * 60)

    all_results = []
    for comment in TEST_COMMENTS:
        print(f'\nComentário: "{comment}"')
        print()
        results = compare_models(client, models, comment)
        all_results.append(results)

        # Table header
        print(
            f"  {'Model':<20s} {'Classification':<16s} "
            f"{'Confidence':<12s} {'Latency':<10s} Reason"
        )
        print(f"  {'-'*18:<20s} {'-'*14:<16s} {'-'*10:<12s} {'-'*8:<10s} {'-'*20}")
        for r in results:
            print(
                f"  {r['model']:<20s} {r['classification']:<16s} "
                f"{r['confidence']:<12.2f} {str(r['latency_ms'])+'ms':<10s} "
                f"{r['reason'][:40]}"
            )

    # Resumo
    print("\n" + "=" * 60)
    print("  Resumo da Comparação")
    print("=" * 60)

    agreements = sum(
        1
        for r in all_results
        if len(set(x["classification"] for x in r)) == 1
    )
    total = len(all_results)
    print(f"  Taxa de concordância: {agreements}/{total} ({agreements/total*100:.0f}%)")

    for model in models:
        latencies = [
            x["latency_ms"]
            for results in all_results
            for x in results
            if x["model"] == model
        ]
        avg = sum(latencies) / len(latencies) if latencies else 0
        print(f"  Avg latency - {model}: {avg:.0f}ms")
    print()


def run_hybrid(client, primary: str, secondary: str):
    """Hybrid escalation mode."""
    print("=" * 60)
    print("  Moderação Híbrida (Modo de Escalonamento)")
    print(f"  Primário: {primary} | Secundário: {secondary}")
    print(f"  Limite de escalonamento: confiança < 0.8")
    print("=" * 60)

    escalation_count = 0
    for comment in TEST_COMMENTS:
        result = hybrid_classify(client, primary, secondary, comment)
        icon = "\u2b06\ufe0f " if result["escalated"] else "  "
        print(f'\n{icon}"{comment}"')
        print(
            f"   Model: {result['model_used']} | "
            f"{result['classification']} ({result['confidence']:.2f}) | "
            f"{result['latency_ms']}ms"
        )
        if result["escalated"]:
            escalation_count += 1

    print(f"\n  Escalated: {escalation_count}/{len(TEST_COMMENTS)} comments")
    print()


def main():
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    model_1 = os.environ.get("MODEL_DEPLOYMENT_NAME")
    model_2 = os.environ.get("MODEL_DEPLOYMENT_NAME_2")

    if not endpoint or endpoint.startswith("https://<"):
        print("ERRO: Defina PROJECT_ENDPOINT no seu arquivo .env.")
        sys.exit(1)
    if not model_1:
        print("ERRO: Defina MODEL_DEPLOYMENT_NAME no seu arquivo .env.")
        sys.exit(1)
    if not model_2:
        print(
            "AVISO: MODEL_DEPLOYMENT_NAME_2 não definido. "
            "Usando apenas MODEL_DEPLOYMENT_NAME para demonstração."
        )
        print("      Defina MODEL_DEPLOYMENT_NAME_2 no .env para uma comparação real.\n")
        model_2 = model_1

    parser = argparse.ArgumentParser(description="Comparação de Modelos")
    parser.add_argument("--hybrid", action="store_true", help="Modo de escalonamento híbrido")
    args = parser.parse_args()

    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )
    inference_client = project_client.get_openai_client()

    models = [model_1, model_2] if model_1 != model_2 else [model_1]

    if args.hybrid and len(models) == 2:
        run_hybrid(inference_client, models[0], models[1])
    else:
        if args.hybrid and len(models) < 2:
            print("AVISO: O modo híbrido requer dois modelos. Executando comparação em vez disso.\n")
        run_comparison(inference_client, models)


if __name__ == "__main__":
    main()
