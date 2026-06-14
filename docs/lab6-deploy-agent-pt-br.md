# Lab 6: Implantar um Agente Hospedado com o AZD AI CLI

> **Duração:** ~20 minutos | **Fase:** Solução Final -- Implantação de Agente Hospedado

## Objetivo

Implantar a lógica de moderação de avaliações de produtos da Zava do Lab 4 como um **agente hospedado** no Serviço de Agente Microsoft Foundry usando o Azure Developer CLI (azd ai agent). Isto transforma o script Python local de Serena em um serviço em nuvem persistente e dimensionável que pode lidar com o volume diário de avaliações da Zava. Todo o fluxo de trabalho -- inicialização, construção, implantação, invocação, monitoramento e limpeza -- é impulsionado por comandos CLI.

---

## O Que é um Agente Hospedado?

Um **agente hospedado** é uma aplicação contêinerizada que executa na infraestrutura gerenciada do Foundry:

| Propriedade | Descrição |
|-------------|-----------|
| **Tempo de execução** | Seu código em um conteiner Docker, gerenciado pelo Foundry |
| **Adaptador** | Adaptador de hospedagem expõe seu agente como API REST |
| **Protocolo** | Compatível com API de Respostas do OpenAI |
| **Dimensionamento** | Automático (réplicas mín/máx configuráveis) |
| **Ciclo de vida** | init → deploy → invoke → monitor → cleanup via azd |
| **Identidade** | Identidade gerenciada do projeto (auto-configurada) |

Diferente dos scripts nos Labs 3-5 que são executados localmente, um agente hospedado é um **serviço em nuvem persistente e acessível** a partir do Playground Foundry, outros agentes ou qualquer aplicação.

---

## Arquitetura

![mermaid_diagram2.png](./images/mermaid_diagram2.png)

---

## O Que é Novo Neste Lab

Labs 3-4 foram Python puro -- você escreveu um script, o executou localmente e viu a saída no seu terminal. Este lab introduz **três novos conceitos**, mas não se preocupe: azd manipula o trabalho pesado para todos eles.

| Novo conceito | O que significa | O que você realmente faz |
|---|---|---|
| **Conteiner Docker** | Seu código do agente é empacotado em uma imagem portátil | **azd up** o constrói para você -- você não escreve ou executa nenhum comando Docker |
| **Registro de Conteiner do Azure (ACR)** | Armazenamento em nuvem para imagens de contêiner | Já foi provisionado no Lab 0 -- azd o pressiona automaticamente |
| **Agente hospedado no Foundry** | Uma API REST persistente executando sua lógica de moderação | **azd up** o implanta; **azd ai agent invoke** o chama |

O resultado final: você editará zero arquivos de infraestrutura. Os comandos são **azd up** (implantar) e **azd ai agent invoke** (testar).

---

## Pré-requisitos

- Labs 1-4 concluídos (projeto Foundry provisionado, modelo implantado)
- Azure Developer CLI instalado com a extensão ai agent:
  ```bash
  azd ext install azure.ai.agents
  azd ext upgrade azure.ai.agents
  ```
- Arquivo .env com PROJECT_ENDPOINT e MODEL_DEPLOYMENT_NAME definidos

> **Do Lab 4 ao agente hospedado:** Nos Labs 3-4, você construiu o pipeline de moderação de avaliações da Zava que executa localmente -- você envia uma avaliação de produto, o modelo a classifica e seu código aplica lógica de negócios. Neste lab, você pega essa mesma lógica de moderação e a implanta como um **agente hospedado** no Foundry. O agente executa em um conteiner gerenciado, é acessível via API REST e pode ser usado no Playground Foundry, outros agentes (como Cora, a assistente de compras da Zava) ou qualquer aplicação. Mesma inteligência, agora como um serviço em nuvem persistente.

---

## Passo 1: Revisar o Código do Agente

O código-fonte do agente está em src/agent/. Três arquivos compõem a aplicação do agente hospedado: app.py, dockerfile e agent.yml:

### src/agent/app.py -- O Agente

```python
from agent_framework import Agent
from agent_framework_foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
....

Do not include any text outside the JSON object."""

agent = Agent(
    client=FoundryChatClient(
        project_endpoint=PROJECT_ENDPOINT,
        model=MODEL_DEPLOYMENT_NAME,
        credential=DefaultAzureCredential(),
    ),
    name="zava-review-moderation-agent",
    instructions=SYSTEM_PROMPT,  # Mesmo prompt de moderação de avaliação da Zava do Lab 4
)

if __name__ == "__main__":
    ResponsesHostServer(agent).run(port=8088)
```

Componentes-chave:
- **Agent** do Microsoft Agent Framework -- define o comportamento do agente
- **FoundryChatClient** -- se conecta ao Foundry para inferência de modelo usando o padrão de amostra atual do Agent Framework
- **ResponsesHostServer(agent).run(port=8088)** -- o adaptador de hospedagem do Foundry envolve seu agente como um servidor HTTP na porta 8088

### src/agent/Dockerfile -- Definição de Conteiner

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8088
CMD ["python", "-u", "app.py"]
```

### src/agent/agent.yaml -- Manifesto do Agente

```yaml
kind: hosted
name: zava-review-moderation-agent
description: Product review moderation agent for Zava that classifies customer reviews
protocols:
    - protocol: responses
      version: "1.0.0"
environment_variables:
    - name: AZURE_AI_PROJECT_ENDPOINT
      value: ${AZURE_AI_PROJECT_ENDPOINT}
    - name: AZURE_AI_MODEL_DEPLOYMENT_NAME
      value: ${MODEL_DEPLOYMENT_NAME}
```

O manifesto diz ao Foundry como configurar o agente de moderação de avaliações da Zava -- quais protocolos ele suporta e quais variáveis de ambiente injetar.

---

## Passo 2: Inicializar o Projeto (Opcional -- Já Feito)

> **Nota:** O repo já inclui os arquivos do agente e configuração azure.yaml. Este passo mostra como foi configurado, como referência.

Se você estivesse começando do zero, você executaria:

**Bash (Mac/Linux):**

```bash
azd ai agent init \
    --project-id "<seu-id-de-recurso-de-projeto-foundry>" \
    --model-deployment gpt-4.1-mini \
    --protocol responses \
    --src src/agent
```

**PowerShell (Windows):**

```powershell
azd ai agent init `
    --project-id "<seu-id-de-recurso-de-projeto-foundry>" `
    --model-deployment gpt-4.1-mini `
    --protocol responses `
    --src src/agent
```

Este comando:
1. Detecta seu projeto Foundry existente e ACR
2. Gera agent.yaml com o manifesto do agente
3. Registra o agente como um serviço em azure.yaml
4. Define todas as variáveis de ambiente azd necessárias

---

## Passo 3: Testar o Agente Localmente

Antes de implantar na nuvem, valide que o agente executa corretamente em sua máquina. Isto detecta erros de importação, problemas de configuração e bugs de lógica cedo.

### Instalar Dependências do Agente

O agente usa pacotes que são separados dos requisitos principais do lab. Instale-os primeiro:

```bash
pip install -r src/agent/requirements.txt
```

### Iniciar o Agente

Abra um terminal, ative seu ambiente virtual e execute:

```bash
cd src/agent
python app.py
```

Você deve ver uma saída como:

```
Starting Zava product review moderation agent...
  Endpoint: https://<seu-recurso>.services.ai.azure.com/api/projects/<seu-projeto>
  Model:    gpt-4.1-mini
Starting hosting adapter on port 8088...
INFO:     Uvicorn running on http://0.0.0.0:8088 (Press CTRL+C to quit)
```

### Enviar uma Solicitação de Teste

Abra um **segundo terminal** e envie um comentário de teste para o agente executando localmente:

**PowerShell:**

```powershell
Invoke-RestMethod -Uri "http://localhost:8088/responses" `
    -Method POST -ContentType "application/json" `
    -Body '{"input": "Love this cordless drill! Battery lasts all day and the torque is impressive.", "model": "gpt-4.1-mini"}' | ConvertTo-Json -Depth 10
```

**Bash / curl:**

```bash
curl -s http://localhost:8088/responses \
    -H "Content-Type: application/json" \
    -d '{"input": "Love this cordless drill! Battery lasts all day and the torque is impressive.", "model": "gpt-4.1-mini"}' | python -m json.tool
```

### Resposta Esperada

Procure pelo campo output_text na resposta -- deve conter uma classificação JSON:

```json
{
    "classification": "SAFE",
    "confidence": 1.0,
    "reason": "Positive and constructive product feedback about a cordless drill."
}
```

### Testar uma Avaliação Insegura

```bash
curl -s http://localhost:8088/responses \
    -H "Content-Type: application/json" \
    -d '{"input": "Zava employees are the worst people on earth", "model": "gpt-4.1-mini"}'
```

Esperado: "classification": "UNSAFE"

### Alternativamente, Use o CLI

Se preferir, use **azd ai agent invoke** com o sinalizador **--local**:

```bash
azd ai agent invoke --local "The cabinet hardware feels cheap for the price Zava is charging"
```

> **Solução de problemas:** Se você ver ImportError, certifique-se de que seu ambiente virtual está ativado e os pacotes de src/agent/requirements.txt estão instalados:
> ```bash
> pip install -r src/agent/requirements.txt
> ```

Uma vez que você confirmou que o agente funciona localmente, pressione **Ctrl+C** para pará-lo e prossiga para implantação na nuvem.

---

## Passo 4: Implantar o Agente

Construa a imagem de conteiner em ACR e implante o agente hospedado no Foundry:

```bash
azd up
```
Se você receber o erro: "ERROR: FOUNDRY_PROJECT_ENDPOINT is required: environment variable was not found in the current azd environment"

execute 
```bash 
azd env set FOUNDRY_PROJECT_ENDPOINT "https://<seu-endpoint-de-projeto-foundry>"
```
Você obtém seu endpoint da página de configuração em https://ai.azure.com/ para o projeto. 

Agora re-execute para implantar

```bash
azd up 
```

### O Que azd up Faz

1. **Provisiona** -- Cria/atualiza infraestrutura (ACR, host de capacidade, RBAC)
2. **Constrói** -- Envia src/agent/ para ACR para uma construção remota de Docker
3. **Implanta** -- Registra uma versão de agente hospedado no Serviço de Agente Foundry
4. **Inicia** -- Inicia o conteiner e aguarda estar pronto

### Saída Esperada

```
Provisioning Azure resources (azd provision)
...
(✓) Done: Resource group: rg-<seu-grupo-de-recursos>

Deploying services (azd deploy)
  Building container image...
  (✓) Done: Container image built and pushed to ACR
  Creating hosted agent version...
  (✓) Done: Agent deployed and started

SUCCESS: Your application was provisioned and deployed to Azure.
```

> A primeira implantação leva 3-5 minutos. Implantações subsequentes são mais rápidas.

---

## Passo 5: Verificar Status do Agente

Se a implantação foi bem-sucedida, seu agente está agora hospedado no Foundry. Verifique o status:

**Próximo:** [Lab 7 - Resumo do Workshop](./lab7-summary-pt-br.md)
