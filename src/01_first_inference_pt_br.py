"""
Lab 3: Primeira Inferência com Microsoft Foundry
================================================
Conecte-se a um projeto Foundry e envie sua primeira solicitação de inferência para um modelo hospedado.

Cenário: Você é Serena, uma desenvolvedora na Zava (uma varejista global de melhoria residencial),
exploramdo Microsoft Foundry para alimentar recursos de IA para a plataforma Zava.
"""

import os
import sys

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()


def main():
    # --- Validar ambiente ---
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    model = os.environ.get("MODEL_DEPLOYMENT_NAME")

    if not endpoint or endpoint.startswith("https://<"):
        print("ERRO: Defina PROJECT_ENDPOINT no seu arquivo .env (veja Lab 2).")
        sys.exit(1)
    if not model:
        print("ERRO: Defina MODEL_DEPLOYMENT_NAME no seu arquivo .env.")
        sys.exit(1)

    # --- Conectar ao projeto Foundry ---
    print("Conectando ao projeto Foundry...")
    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )

    # --- Obter cliente de inferência ---
    inference_client = project_client.get_openai_client()

    # --- Enviar solicitação de inferência ---
    print(f"Enviando solicitação de inferência para o modelo: {model}")
    response = inference_client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente útil para Zava, uma varejista global de melhoria residencial. Responda de forma concisa.",
            },
            {
                "role": "user",
                "content": "O que é Microsoft Foundry e como um varejista como Zava poderia usá-lo? Responda em uma frase.",
            },
        ],
    )

    # --- Processar resposta ---
    content = response.choices[0].message.content
    print("---")
    print(f"Resposta:\n{content}")
    print("---")
    print(f"Modelo: {response.model}")
    print(f"Motivo de conclusão: {response.choices[0].finish_reason}")
    print(
        f"Tokens usados: {response.usage.total_tokens} "
        f"(prompt: {response.usage.prompt_tokens}, "
        f"conclusão: {response.usage.completion_tokens})"
    )


if __name__ == "__main__":
    main()
