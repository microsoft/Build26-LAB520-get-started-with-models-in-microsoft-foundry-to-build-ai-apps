# Lab 5: Comparar Resultados de Modelos (Extensão Opcional)

> **Duração:** ~15 minutos | **Fase:** Desafio de Extensão

## Objetivo

Compare como diferentes modelos hospedados classificam as mesmas avaliações de produtos da Zava, meça qualidade de resposta e latência, e ajude Serena a tomar uma decisão informada sobre qual modelo implantar para o pipeline de moderação de avaliações da Zava.

---

## Por Que Comparar Modelos?

Diferentes modelos têm diferentes forças:

| Modelo | Forças | Trade-offs |
|--------|--------|-----------|
| gpt-4.1-mini | Rápido, eficiente em custo, bom para tarefas simples | Pode perder nuance em casos complexos |
| gpt-4.1 | Qualidade de raciocínio superior, melhor em casos extremos | Mais lento, mais caro |
| Phi-4 | Código aberto, raciocínio forte, executa em dispositivo | Pode precisar de ajuste de prompt diferente |

Comparar modelos em seus **dados reais de avaliação da Zava** ajuda Serena a tomar decisões de implantação informadas.

---

## Pré-requisitos

Faça login na sua Assinatura do Azure 

```Powershell
az login 
```
Isto abrirá uma tela de login 'faça login com uma conta de trabalho ou escola'

Certifique-se de que sua assinatura esteja definida para sua assinatura executando adicione seu ID de Assinatura do Azure

# Substitua <@lab.CloudSubscription.Id> pelo seu próprio ID de assinatura encontre-o com: 

```Powershell
az account show --query id -o tsv)
```

Em seguida, execute o comando 

```Powershell
az account set --subscription "<@lab.CloudSubscription.Id>"
```

Este passo é importante para garantir que todas as implantações e comandos sejam executados contra a assinatura do Azure correta onde seu recurso Foundry foi provisionado.

Para completar este lab, você precisa de **duas implantações de modelo** em seu projeto Foundry. Atualize seu .env:

```ini
MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
MODEL_DEPLOYMENT_NAME_2=gpt-4.1
```

Se você tem apenas um modelo implantado, implante um segundo usando:

**Bash (Mac/Linux):**

```bash
az cognitiveservices account deployment create \
  --name <seu-nome-de-recurso-foundry> \
  --resource-group rg-foundry-lab \
  --deployment-name gpt-4.1 \
  --model-name gpt-4.1 \
  --model-version "2025-04-14" \
  --model-format OpenAI \
  --sku-capacity 10 \
  --sku-name "GlobalStandard"
```

**PowerShell (Windows):**

```powershell
az cognitiveservices account deployment create `
  --name <seu-nome-de-recurso-foundry> `
  --resource-group rg-foundry-lab `
  --deployment-name gpt-4.1 `
  --model-name gpt-4.1 `
  --model-version "2025-04-14" `
  --model-format OpenAI `
  --sku-capacity 10 `
  --sku-name "GlobalStandard"
```

### Alternativa com Um Modelo

Se você tem apenas **um modelo** implantado, você ainda pode obter insights de comparação significativos variando **como** você chama-o ao invés de **qual** modelo você chama. Tente esses experimentos com src/02_comment_moderation.py:

**1. Comparar estratégias de prompt** -- Edite o prompt do sistema em classify_comment() para ser mais rigoroso ou mais indulgente:

```python
# Rigoroso: tolerância mais baixa
"Classify as UNSAFE if there is any negativity or personal criticism."

# Indulgente: tolerância mais alta
"Only classify as UNSAFE if the comment contains explicit threats or slurs."
```

Execute o script com cada prompt e compare como as classificações mudam para os mesmos comentários.

**2. Comparar configurações de temperatura** -- Altere temperature=0.0 para temperature=0.7 e execute o script de moderação várias vezes. Em 0.0, os resultados devem ser idênticos a cada execução; em 0.7, você pode ver desvio de classificação em comentários borderline.

**3. Comparar formatos de saída** -- Modifique o prompt do sistema para devolver um rótulo de texto simples ao invés de JSON. Compare como você consegue analisar a resposta confiável vs a abordagem JSON estruturada.

Esses experimentos ensinam a mesma lição central que comparação de múltiplos modelos: **pequenas alterações em configuração produzem resultados mensuravelmente diferentes**, e você deve testar sistematicamente antes de se comprometer com uma configuração de produção.

---

## Passo 1: Revisar o Código de Comparação

Abra src/03_model_comparison.py. A função principal executa o mesmo comentário através de múltiplos modelos:

```python
def compare_models(client, models: list[str], comment: str) -> list[dict]:
    results = []
    for model in models:
        start = time.time()
        result = classify_comment(client, model, comment)
        elapsed = time.time() - start
        results.append({
            "model": model,
            "classification": result["classification"],
            "confidence": result["confidence"],
            "reason": result["reason"],
            "latency_ms": round(elapsed * 1000),
        })
    return results
```

---

## Passo 2: Executar a Comparação

```bash
python src/03_model_comparison.py
```

### Saída Esperada

```
========================================
  Model Comparison: Zava Review Moderation
========================================

Comment: "This paint is garbage and whoever designed it should be fired"

  Model         Classification  Confidence  Latency   Reason
  ------------- -------------- ----------  --------  ------
  gpt-4.1-mini   NEEDS_REVIEW   0.75        324ms     Strong negative sentiment...
  gpt-4.1        NEEDS_REVIEW   0.80        891ms     Borderline personal attack toward staff...

Comment: "You're all idiots if you shop here -- worst store ever"

  Model         Classification  Confidence  Latency   Reason
  ------------- -------------- ----------  --------  ------
  gpt-4.1-mini   UNSAFE         0.95        298ms     Contains insults directed at customers
  gpt-4.1        UNSAFE         0.98        845ms     Personal attacks targeting customers

========================================
  Comparison Summary
========================================
  Agreement rate: 100% (both models agreed on all classifications)
  Avg latency - gpt-4.1-mini: 310ms
  Avg latency - gpt-4.1:      868ms
  Cost ratio:  gpt-4.1-mini is ~10x cheaper per token
```

---

## Passo 3: Analisar os Resultados

Procure por padrões na comparação:

### Acordo

Ambos os modelos classificam comentários da mesma forma? Se discordarem, em qual modelo você confiaria para seu caso de uso?

### Confiança

O modelo mais capaz consistentemente dá pontuações de confiança mais altas? Confiança mais alta pode justificar o custo adicional para casos borderline.

### Latência

Qual é a latência do modelo maior? Para moderação em tempo real (ex: bate-papo), latência importa. Para processamento em lote, pode não.

### Custo

| Modelo | Entrada (por 1 milhão de tokens) | Saída (por 1 milhão de tokens) |
|--------|--------------------------------|------|
|gpt-4.1-mini | ~$0.15 | ~$0.60 |
|gpt-4.1 | ~$2.50 | ~$10.00 |

**Estimando seu custo de lab:** Cada solicitação de moderação usa aproximadamente 250 tokens de entrada (prompt do sistema + comentário) e 50 tokens de saída (resposta JSON). Com 5 comentários de amostra entre 2 modelos, são 10 solicitações totais:

| | Tokens de entrada | Tokens de saída | Custo por 1M tokens (entrada/saída) | Custo estimado |
|---|---|---|---|---|
| gpt-4.1-mini | 5 × 250 = 1.250 | 5 × 50 = 250 | $0.15 / $0.60 | **$0.0003** |
| gpt-4.1 | 5 × 250 = 1.250 | 5 × 50 = 250 | $2.50 / $10.00 | **$0.006** |
| **Total para este lab** | | | | **< $0.01** |

Mesmo executando o sample_comments.json completo (15 avaliações da Zava × 2 modelos = 30 solicitações) fica bem abaixo de $0.01. A diferença de custo se torna significativa na escala da Zava -- em 100.000 avaliações/dia, gpt-4.1-mini custa ~$5/dia vs gpt-4.1 a ~$80/dia.

> **Dica:** Para este tipo de tarefa de classificação, gpt-4.1-mini frequentemente corresponde ao desempenho de gpt-4.1 por uma fração do custo.

---

## Passo 4: Tentar uma Abordagem Híbrida

Um padrão de produção comum é usar o modelo mais barato primeiro e escalar desacordos para o modelo mais capaz.

O script de comparação inclui um modo --hybrid:

```bash
python src/03_model_comparison.py --hybrid
```

Isto executa gpt-4.1-mini primeiro. Se a confiança estiver abaixo de 0.8, ele executa novamente com gpt-4.1 para uma segunda opinião.

---

## Desafios de Extensão

Se você terminar cedo, tente estes:

1. **Adicionar um terceiro modelo** -- Implante Phi-4 e adicione-o à comparação
2. **Criar seu próprio conjunto de teste** -- Escreva 10 avaliações de produtos da Zava que abranjam casos extremos (reclamações de devoluções, menções de concorrentes, elogios sarcásticos)
3. **Medir consistência** -- Execute a mesma avaliação 5 vezes e verifique se a classificação varia (não deveria em temperature=0.0)
4. **Ajustar o prompt** -- Torne o prompt do sistema mais rigoroso sobre reclamações para os funcionários da Zava e veja como isso muda as classificações

---

## O Que Você Aprendeu

- ✅ Como executar a mesma inferência entre múltiplos modelos
- ✅ Como comparar qualidade de classificação, confiança e latência
- ✅ Como tomar decisões de seleção de modelo com base em requisitos de tarefa
- ✅ Como implementar um padrão de escalação híbrida

---

## Conceito-Chave

> Seleção de modelo é uma decisão de produto, não apenas uma técnica. Comparando programaticamente modelos em dados de tarefa reais, você pode otimizar para o equilíbrio correto de qualidade, velocidade e custo.

---

**Próximo:** [Lab 6 - Implantar Agente](./lab6-deploy-agent.md)
