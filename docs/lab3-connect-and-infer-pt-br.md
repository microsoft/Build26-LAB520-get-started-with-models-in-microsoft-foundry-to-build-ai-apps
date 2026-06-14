# Lab 3: Conectar e Enviar Sua Primeira Inferência

> **Duração:** ~15 minutos | **Fase:** Interação Baseada em Código

## Objetivo

Como Serena (desenvolvedora da Zava), escreva código Python que se autentica contra seu projeto Foundry, se conecta a um endpoint de modelo hospedado e envia sua primeira solicitação de inferência -- estabelecendo a base para o sistema de moderação de avaliações da Zava.

---

## Conceitos

| Conceito | Descrição |
|----------|-----------|
| **AIProjectClient** | Cliente SDK que se conecta ao seu projeto Foundry |
| **DefaultAzureCredential** | Cadeia de credencial automática -- usa sua sessão az login localmente |
| **Conclusão de Bate-papo** | Envie um prompt do sistema + mensagem do usuário, receba uma resposta do modelo |
| **Endpoint de Inferência** | O endpoint da API que sua implantação de modelo expõe |

---

## Passo 1: Revisar o Código

Abra src/01_first_inference.py em seu editor. 

As seções a seguir orientam e explicam o código na solução passo a passo, cobrindo os aspectos-chave da solução.

### Autenticação e Configuração do Cliente

```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

def main():
    # --- Validar ambiente ---
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    model = os.environ.get("MODEL_DEPLOYMENT_NAME")

    if not endpoint or endpoint.startswith("https://<"):
        print("ERROR: Set PROJECT_ENDPOINT in your .env file (see Lab 2).")
        sys.exit(1)
    if not model:
        print("ERROR: Set MODEL_DEPLOYMENT_NAME in your .env file.")
        sys.exit(1)

    # --- Conectar ao projeto Foundry ---
    print("Connecting to Foundry project...")
    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )
```

Isto cria um cliente de projeto autenticado com suas credenciais do Azure. O PROJECT_ENDPOINT vem do seu arquivo .env (configurado no Lab 2).

### Obtendo um Cliente de Inferência

```python
inference_client = project_client.get_openai_client()
```

O cliente do projeto fornece um cliente compatível com OpenAI para conclusões de bate-papo. Este cliente é pré-configurado com o endpoint e credenciais do seu projeto.

### Enviando uma Solicitação

```python
response = inference_client.chat.completions.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    messages=[
        {"role": "system", "content": "You are a helpful assistant for Zava, a global home-improvement retailer. Respond concisely."},
        {"role": "user", "content": "What is Microsoft Foundry and how could a retailer like Zava use it? Answer in one sentence."},
    ],
)
```

O método chat.completions.create() envia uma solicitação de conclusão de bate-papo com:

- **model** -- O nome da implantação (ex: gpt-4.1-mini)
- **messages** -- Um array de mensagens de conversa com funções (sistema, usuário, assistente)

### Processando a Resposta

```python
print(response.choices[0].message.content)
```

O objeto de resposta contém um array de escolhas. Cada escolha tem uma mensagem com conteúdo -- a resposta de texto do modelo.

---

## Passo 2: Executar o Código

Certifique-se de que seu arquivo .env está configurado dentro de sua solução (do Lab 2) e execute o seguinte comando a partir de uma janela de terminal:

Para abrir uma janela de terminal no VSCode selecione Terminal -> nova janela no menu superior no VSCode 

```bash
python src/01_first_inference.py
```

### Saída Esperada (Você está usando uma solução LLM não determinística, então a saída não será 100% correspondida, simplesmente valide mensagem e formato)

```
Connecting to Foundry project...
Sending inference request to model: gpt-4.1-mini
---
Response:
Microsoft Foundry is a unified platform for discovering, deploying, and
managing AI models, which Zava could use to power product recommendations,
review moderation, and customer support agents at scale.
---
Model: gpt-4.1-mini
Tokens used: 52 (prompt: 30, completion: 22)
```

> **Nota:** A primeira solicitação de inferência pode levar 3-5 segundos devido ao início frio (o endpoint do modelo aquecendo). Solicitações subsequentes na mesma sessão são tipicamente muito mais rápidas (menos de 2 segundos). Este é um comportamento normal -- se você vir um atraso na primeira chamada, apenas aguarde a resposta.

### Solução de Problemas de Erros Comuns

Se o script falhar, verifique a tabela abaixo antes de pedir ajuda:

| Erro | Causa | Solução |
|------|-------|--------|
| KeyError: PROJECT_ENDPOINT | Arquivo .env está faltando ou incompleto | Execute azd env get-values > .env para regenerá-lo |
| AuthenticationError ou DefaultAzureCredential falhou | Sessão do Azure CLI expirou | Execute az login e tente novamente |
| Conexão expirada após 30+ segundos | Endpoint está inacessível | Verifique sua rede/VPN; verifique a URL do endpoint em .env |
| ResourceNotFoundError | Nome da implantação de modelo não corresponde | Execute az cognitiveservices account deployment list para verificar o nome exato |

---

## Passo 3: Experimentar

Tente modificar o código para explorar diferentes comportamentos:

### Alterar o Prompt do Sistema

Edite a mensagem do sistema para alterar o comportamento do modelo:

```python
{"role": "system", "content": "You are Cora, Zava's friendly AI shopping assistant. Help customers find the right home-improvement products."},
```

### Alterar a Entrada do Usuário

```python
{"role": "user", "content": "I'm Bruno and I'm renovating my kitchen. What tools do I need to install new cabinets?"},
```

### Adicionar Controle de Temperatura

```python
response = inference_client.chat.completions.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    messages=[...],
    temperature=0.0,  # Saída determinística
)
```

| Temperatura | Comportamento |
|-------------|-----------|
| 0.0 | Determinística -- mesma entrada produz mesma saída |
| 0.7 | Criatividade equilibrada (padrão) |
| 1.0 | Criatividade máxima / variabilidade |

> **Para tarefas de moderação de avaliações da Zava (Lab 4), use temperature=0.0** para obter classificações consistentes e reproduzíveis.

## Experimentar (Executar, Observar, Aprender)

Agora que seu código está funcionando, este passo é sobre **testar ativamente alterações e observar como o modelo se comporta**.

***

## Onde Executar Seus Experimentos

Você deve executar e testar suas alterações em seu **ambiente Python**:

* Abra a pasta raiz em seu terminal ou VS Code
* Execute seu script:

```bash
python src/01_first_inference.py
```

Cada vez que fizer uma alteração, execute novamente o script e observe a saída no terminal.

* Use **Playground do Microsoft Foundry** apenas para comparar comportamento de prompt, não para depurar seu código

***

## Como Experimentar

Siga um loop simples:

1. Altere uma coisa apenas
2. Execute o script
3. Observe a saída
4. Compare com execuções anteriores

***

## Experimentos para Tentar

### Alterar o Prompt do Sistema

Edite a mensagem do sistema para controlar tom e comportamento:

```python
{"role": "system", "content": "You are Cora, Zava's friendly AI shopping assistant. Help customers find the right home-improvement products."},
```

Pergunte:

* O tom muda?
* Permanece no papel?
* Dá respostas mais focadas?

***

### Alterar a Entrada do Usuário

```python
{"role": "user", "content": "I'm Bruno and I'm renovating my kitchen. What tools do I need to install new cabinets?"},
```

Pergunte:

* Adicionar contexto melhora a resposta?
* Faz perguntas de esclarecimento?
* O que acontece se a entrada for vaga ou breve?

Tente variações:

* "Tools for cabinets?"
* "I want to install cabinets but avoid power tools"

***

### Adicionar Controle de Temperatura

```python
response = inference_client.chat.completions.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    messages=[...],
    temperature=0.0,
)
```

| Temperatura | Comportamento                             |
| ----------- | ------------------------------------- |
| 0.0         | Mesma saída sempre, determinística |
| 0.7         | Equilibrado e natural                  |
| 1.0         | Mais criativo e variável            |

Pergunte:

* A saída permanece igual em 0.0?
* A criatividade aumenta em valores mais altos?
* A qualidade diminui em 1.0?

Para tarefas de classificação depois, sempre use `temperature=0.0`.

***

### Adicionar Contexto de Conversa

Estenda as mensagens para simular uma conversa:

```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "I am installing cabinets"},
    {"role": "assistant", "content": "You will need a drill, level, and measuring tape"},
    {"role": "user", "content": "What if I have uneven walls?"}
]
```

Pergunte:

* O modelo se lembra das etapas anteriores?
* Dá respostas de acompanhamento melhores?


## O Que Você Deve Estar Aprendendo

Após executar esses experimentos, você deve entender:

* Como prompts controlam comportamento
* Como entrada afeta qualidade de saída
* Quando usar configurações determinísticas vs criativas
* Como contexto de conversa funciona
* Como reconhecer e diagnosticar erros comuns

***

## Dica

Próximas seções

**Próxima:** [Lab 4 - Zava Review Moderation App](./lab4-comment-moderation-pt-br.md)
