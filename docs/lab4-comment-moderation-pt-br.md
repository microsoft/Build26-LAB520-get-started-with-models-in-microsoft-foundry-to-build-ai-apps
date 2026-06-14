# Lab 4: Construir uma Aplicação de Moderação de Avaliações de Produtos para Zava

> **Duração:** ~20 minutos | **Fase:** Implementação de Tarefa do Mundo Real

## Objetivo

Construir um pipeline de moderação de avaliações de produtos funcional para a loja online da Zava. O sistema aceita avaliações de produtos enviadas por clientes, as classifica usando um modelo hospedado em Foundry, aplica lógica de moderação e emite resultados estruturados -- garantindo que as avaliações de clientes como Bruno sejam seguras e úteis antes de irem ao vivo no site.

---

## O Problema

A loja online da Zava recebe milhares de avaliações de produtos diariamente em centenas de categorias de melhorias para o lar -- desde ferramentas elétricas e tinta até armários de cozinha e dispositivos inteligentes. Revisão manual não se dimensiona. Serena precisa construir um sistema automatizado que possa:

1. Aceitar uma avaliação de cliente como entrada
2. Classificá-la em uma categoria de moderação
3. Devolver uma decisão estruturada com raciocínio
4. Lidar graciosamente com casos extremos

---

## Arquitetura

![architecture_lab520.png](./images/architecture_lab520.png)

---

## Passo 1: Revisar o Prompt do Sistema

A chave para moderação confiável é um prompt do sistema bem estruturado. Abra src/02_comment_moderation.py e examine o SYSTEM_PROMPT:

```python
SYSTEM_PROMPT = """You are a product review moderation system for Zava, a global home-improvement retailer. Analyze the provided customer review and classify it.

Respond ONLY with valid JSON in this exact format:
{
    "classification": "<SAFE|NEEDS_REVIEW|UNSAFE>",
    "confidence": <0.0-1.0>,
    "reason": "<brief explanation>"
}

Classification rules:
- SAFE: Constructive product feedback, installation questions, positive experiences, neutral observations about products or services
- NEEDS_REVIEW: Borderline content, strong complaints about products or staff, potential sarcasm, frustration without abuse
- UNSAFE: Hate speech, threats toward staff or customers, harassment, explicit content, personal attacks

Do not include any text outside the JSON object."""
```

Este prompt:

- **Restringe o formato de saída** -- Apenas JSON, estrutura previsível
- **Define categorias claras** -- Classificação de três níveis
- **Fornece regras de classificação** -- Reduz ambiguidade
- **Elimina ruído de texto livre** -- "Não inclua nenhum texto fora do objeto JSON"

---

## Passo 2: Compreender o Pipeline de Moderação

A aplicação segue este fluxo:

### 2a. Enviar Comentário para Classificação

```python
def classify_comment(client, model: str, comment: str) -> dict:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": comment},
            ],
            temperature=0.0,  # Saída determinística
        )
    except Exception as e:
        if "content_filter" in str(e) or "content management policy" in str(e):
            return {
                "classification": "UNSAFE",
                "confidence": 1.0,
                "reason": "Blocked by Azure content safety filter.",
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
```

Decisões de design-chave:

| Decisão | Razão |
|---------|-------|
| temperature=0.0 | Mesmo comentário sempre recebe a mesma classificação |
| Formato de saída JSON | Analisável por máquina, sem regex necessário |
| Prompt do sistema estruturado | Categorização confiável e consistente |
| try/except ao redor da inferência | Captura blocos de filtro de segurança de conteúdo do Azure graciosamente |
| try/except ao redor de json.loads() | Volta para NEEDS_REVIEW se o modelo retorna saída malformada |

### 2b. Aplicar Lógica de Moderação

```python
def apply_moderation(result: dict) -> str:
    classification = result["classification"]
    confidence = result["confidence"]

    if classification == "SAFE" and confidence >= 0.8:
        return "APPROVED"
    elif classification == "UNSAFE" and confidence >= 0.7:
        return "BLOCKED"
    else:
        return "FLAGGED_FOR_REVIEW"
```

Isto adiciona uma **camada de lógica de negócios** na topo da classificação do modelo:

- SAFE de alta confiança → aprovação automática (avaliação vai ao vivo no site da Zava)
- UNSAFE de alta confiança → bloqueio automático (avaliação é rejeitada)
- Todo o resto → fila de revisão humana (equipe de confiança e segurança da Zava)

### 2c. Processar Resultados

```python
def moderate_comment(client, model: str, comment: str) -> dict:
    classification = classify_comment(client, model, comment)
    action = apply_moderation(classification)
    return {
        "comment": comment,
        "classification": classification["classification"],
        "confidence": classification["confidence"],
        "reason": classification["reason"],
        "action": action,
    }
```

> **Nota:** A função classify_comment usa json.loads() para analisar a resposta do modelo. Como definimos temperature=0.0 e usamos um prompt do sistema estruturado, o modelo retorna confiável JSON válido. Se você modificar o prompt e vir json.JSONDecodeError, verifique que seu prompt do sistema ainda instrui o modelo a responder em formato JSON.

---

## Passo 3: Executar a Aplicação

```bash
python src/02_comment_moderation.py
```

### Saída Esperada (Você está usando uma solução LLM não determinística, então a saída não será 100% correspondida, simplesmente valide mensagem e formato)

```
========================================
  Zava Product Review Moderation System
  Model: gpt-4.1-mini
========================================

Processing 5 sample reviews...

--- Comment 1/5 ---
Comment:  "Love this cordless drill! Battery lasts all day and the torque is impressive."
Classification: SAFE (confidence: 0.95)
Reason:  Constructive positive product feedback
Action:  ✅ APPROVED

--- Comment 2/5 ---
Comment:  "This paint is garbage and whoever designed it should be fired"
Classification: NEEDS_REVIEW (confidence: 0.75)
Reason:  Strong negative sentiment with borderline personal attack toward staff
Action:  🔍 FLAGGED_FOR_REVIEW

--- Comment 3/5 ---
Comment:  "You're all idiots if you shop here -- worst store ever"
Classification: UNSAFE (confidence: 0.95)
Reason:  Contains insults directed at customers
Action:  🚫 BLOCKED

--- Comment 4/5 ---
Comment:  "Does this deck stain work on pressure-treated lumber?"
Classification: SAFE (confidence: 0.98)
Reason:  Constructive product question
Action:  ✅ APPROVED

--- Comment 5/5 ---
Comment:  "Meh, the tile cutter is okay. Not great, not terrible."
Classification: SAFE (confidence: 0.82)
Reason:  Neutral product observation with mild criticism
Action:  ✅ APPROVED

========================================
  Summary
========================================
Total comments: 5
  APPROVED:          3
  FLAGGED_FOR_REVIEW: 1
  BLOCKED:           1
```

> **Nota:** Alguns comentários de teste contendo ameaças ou conteúdo explícito podem ser bloqueados pelo filtro de segurança de conteúdo integrado do Azure *antes* de alcançar o modelo. Quando isso acontece, a aplicação o manipula graciosamente e rotula o comentário como UNSAFE com uma razão "Bloqueado pelo filtro de segurança de conteúdo do Azure". Este é um comportamento esperado -- o filtro de conteúdo é uma camada adicional de proteção em implantações de produção.

---

## Passo 4: Testar com Comentários Personalizados

A aplicação também aceita entrada interativa. Execute-a com o sinalizador --interactive:

```bash
python src/02_comment_moderation.py --interactive
```

Digite comentários para classificá-los em tempo real:

```
Enter a comment (or 'quit' to exit): The cabinet hardware feels cheap for the price
Classification: NEEDS_REVIEW (confidence: 0.65)
Reason: Product complaint that could be constructive feedback or frustration
Action: 🔍 FLAGGED_FOR_REVIEW
```

---

## Passo 5: Testar com o Conjunto de Dados de Amostra

O arquivo src/sample_comments.json contém um conjunto mais amplo de comentários de teste. Execute o teste em lote:

```bash
python src/02_comment_moderation.py --file src/sample_comments.json
```

---

## Passo 6: Personalizar a Lógica de Moderação

Tente ajustar os limites de confiança na função apply_moderation:

| Mudança de Limite | Efeito |
|-----------------|--------|
| Reduzir limite SAFE (0.8 → 0.6) | Mais comentários aprovados automaticamente |
| Aumentar limite UNSAFE (0.7 → 0.9) | Menos bloqueios automáticos, mais revisão humana |
| Adicionar manipulador NEEDS_REVIEW | Roteamento personalizado para conteúdo borderline |

---

## O Que Você Aprendeu

- ✅ Como projetar um prompt do sistema para saída estruturada (JSON)
- ✅ Como construir um pipeline de classificação usando inferência de modelo
- ✅ Como aplicar lógica de negócios na topo de respostas de modelo
- ✅ Como processar lotes de conteúdo programaticamente
- ✅ Como lidar com entrada interativa para moderação em tempo real

---

## Checkpoint

Antes de prosseguir, confirme:

- [ ] python src/02_comment_moderation.py classifica todos os 5 comentários de amostra sem erros
- [ ] Você vê todos os três tipos de ação: APPROVED, FLAGGED_FOR_REVIEW e BLOCKED
- [ ] python src/02_comment_moderation.py --file src/sample_comments.json processa todos os 15 comentários

Se as classificações parecerem inconsistentes, verifique se está usando temperature=0.0 em suas solicitações.

---

## Conceito-Chave

> Um modelo fornece a inteligência -- sua aplicação fornece a lógica. Combinando um prompt estruturado com configurações determinísticas e tomada de decisão programática, Serena pode construir um sistema de moderação de avaliações de qualidade de produção para Zava sem nenhum ajuste fino.

---

## Opcional: Escrever um Teste Unitário para a Lógica de Moderação

O script de validação (src/tests/validate_lab.py) testa setup e inferência end-to-end, mas não testa unitariamente a lógica de negócios em isolamento. Aqui está um padrão rápido que você pode usar para testar apply_moderation sem chamar o modelo:

```python
# test_moderation.py -- execute com: python test_moderation.py
import sys
sys.path.insert(0, "src")
from importlib import import_module
mod = import_module("02_comment_moderation")

def test_apply_moderation():
    # SAFE de alta confiança → APPROVED
    assert mod.apply_moderation({"classification": "SAFE", "confidence": 0.95}) == "APPROVED"
    # SAFE de baixa confiança → FLAGGED
    assert mod.apply_moderation({"classification": "SAFE", "confidence": 0.5}) == "FLAGGED_FOR_REVIEW"
    # UNSAFE de alta confiança → BLOCKED
    assert mod.apply_moderation({"classification": "UNSAFE", "confidence": 0.9}) == "BLOCKED"
    # UNSAFE de baixa confiança → FLAGGED
    assert mod.apply_moderation({"classification": "UNSAFE", "confidence": 0.3}) == "FLAGGED_FOR_REVIEW"
    # NEEDS_REVIEW sempre → FLAGGED
    assert mod.apply_moderation({"classification": "NEEDS_REVIEW", "confidence": 0.8}) == "FLAGGED_FOR_REVIEW"
    print("All tests passed!")

test_apply_moderation()
```

Isto testa a **lógica de negócios** independentemente do modelo -- você pode executá-lo offline, em CI e sem credenciais do Azure. Valida que seus limites de confiança roteiam comentários corretamente.

### Versão pytest

Se você está familiarizado com pytest, aqui está a mesma cobertura como um módulo de teste adequado. Crie src/tests/test_moderation.py:

```python
# src/tests/test_moderation.py -- execute com: pytest src/tests/test_moderation.py -v
import sys
sys.path.insert(0, "src")
from importlib import import_module

mod = import_module("02_comment_moderation")
apply_moderation = mod.apply_moderation
classify_comment = mod.classify_comment


class TestApplyModeration:
    """Testes unitários para a camada de lógica de negócios (sem chamadas de modelo)."""

    def test_safe_high_confidence_approved(self):
        assert apply_moderation({"classification": "SAFE", "confidence": 0.95}) == "APPROVED"

    def test_safe_low_confidence_flagged(self):
        assert apply_moderation({"classification": "SAFE", "confidence": 0.5}) == "FLAGGED_FOR_REVIEW"

    def test_safe_at_threshold_approved(self):
        assert apply_moderation({"classification": "SAFE", "confidence": 0.8}) == "APPROVED"

    def test_unsafe_high_confidence_blocked(self):
        assert apply_moderation({"classification": "UNSAFE", "confidence": 0.9}) == "BLOCKED"

    def test_unsafe_low_confidence_flagged(self):
        assert apply_moderation({"classification": "UNSAFE", "confidence": 0.3}) == "FLAGGED_FOR_REVIEW"

    def test_unsafe_at_threshold_blocked(self):
        assert apply_moderation({"classification": "UNSAFE", "confidence": 0.7}) == "BLOCKED"

    def test_needs_review_always_flagged(self):
        assert apply_moderation({"classification": "NEEDS_REVIEW", "confidence": 0.99}) == "FLAGGED_FOR_REVIEW"

    def test_missing_classification_flagged(self):
        assert apply_moderation({"confidence": 0.9}) == "FLAGGED_FOR_REVIEW"

    def test_missing_confidence_flagged(self):
        assert apply_moderation({"classification": "SAFE"}) == "FLAGGED_FOR_REVIEW"
```

Execute com:

```bash
pytest src/tests/test_moderation.py -v
```

Saída esperada:

```
src/tests/test_moderation.py::TestApplyModeration::test_safe_high_confidence_approved PASSED
src/tests/test_moderation.py::TestApplyModeration::test_safe_low_confidence_flagged PASSED
src/tests/test_moderation.py::TestApplyModeration::test_safe_at_threshold_approved PASSED
...
9 passed in 0.02s
```

> **Por que pytest?** Ele descobre testes automaticamente, dá diffs de falha claras e se integra com pipelines CI (GitHub Actions, Azure DevOps). O script autônomo acima é mais simples de executar; pytest é o que você usaria em um projeto real.

---

**Próximo:** [Lab 5 - Comparação de Modelos (Extensão Opcional)](./lab5-model-comparison-pt-br.md)
