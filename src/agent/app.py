"""
Lab 6: Comment Moderation Hosted Agent
========================================
A content moderation agent using Microsoft Agent Framework and the
hosting adapter for deployment to Microsoft Foundry Agent Service.

Locally: python app.py  (starts on http://localhost:8088)
Deploy:  azd up          (builds container, deploys to Foundry)
"""

import os
import sys

print("Starting comment moderation agent...", flush=True)

try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except ImportError:
    pass  # dotenv is optional in container

from agent_framework import Agent
from agent_framework.azure import AzureAIAgentClient
from azure.ai.agentserver.agentframework import from_agent_framework
from azure.identity import DefaultAzureCredential

# These are injected as environment variables by azd / agent.yaml
PROJECT_ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT") or os.getenv("PROJECT_ENDPOINT")
MODEL_DEPLOYMENT_NAME = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME") or os.getenv("MODEL_DEPLOYMENT_NAME", "gpt-4.1-mini")

if not PROJECT_ENDPOINT:
    print("ERROR: AZURE_AI_PROJECT_ENDPOINT not set", flush=True)
    sys.exit(1)

print(f"  Endpoint: {PROJECT_ENDPOINT}", flush=True)
print(f"  Model:    {MODEL_DEPLOYMENT_NAME}", flush=True)

SYSTEM_PROMPT = """You are a content moderation system. Analyze the provided user comment and classify it.

Respond ONLY with valid JSON in this exact format:
{
    "classification": "<SAFE|NEEDS_REVIEW|UNSAFE>",
    "confidence": <0.0-1.0>,
    "reason": "<brief explanation>"
}

Classification rules:
- SAFE: Constructive feedback, questions, positive comments, neutral observations
- NEEDS_REVIEW: Borderline content, strong emotions, potential sarcasm, complaints without abuse
- UNSAFE: Hate speech, threats, harassment, explicit content, personal attacks

Do not include any text outside the JSON object."""

agent = Agent(
    client=AzureAIAgentClient(
        project_endpoint=PROJECT_ENDPOINT,
        model_deployment_name=MODEL_DEPLOYMENT_NAME,
        credential=DefaultAzureCredential(),
    ),
    instructions=SYSTEM_PROMPT,
)

if __name__ == "__main__":
    print("Starting hosting adapter on port 8088...", flush=True)
    from_agent_framework(agent).run()
