# Lab 0: Configuração e Autenticação do Projeto Foundry

> **Duração:** ~15 minutos | **Fase:** Configuração do Projeto

## Objetivo

Criar um projeto Microsoft Foundry usando o Azure Developer CLI (azd), provisionar a infraestrutura necessária e configurar seu ambiente de desenvolvimento local para inferência de modelo.

---

## O que é um Projeto Foundry?

Um **projeto** Foundry é a unidade organizacional dentro do Microsoft Foundry que agrupa:

- Implantações de modelo
- Agentes
- Avaliações
- Ativos de arquivos e dados

Os projetos são criados dentro de uma **conta Foundry** (recurso de Serviços de IA do Azure) e fornecem o endpoint ao qual seu código de aplicação se conecta.

**Por que você precisa de um?** Um projeto Foundry atua como um único ponto de conexão para todos os seus recursos de IA -- modelos, agentes, avaliações e dados -- para que seu código precise apenas de um endpoint e um conjunto de credenciais para acessar tudo.

> [Saiba mais: Criar um projeto no Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects)

---

> **Qual opção devo escolher?** Use a **Opção A** -- ela executa um script e faz tudo para você. A Opção B abaixo cobre os mesmos passos manualmente, um por um. Está lá como referência ou para solução de problemas, não é algo que você precisa seguir. **Se não tiver certeza, escolha a Opção A.**

## Opção A: Configuração com Um Comando (Recomendado)

A forma mais rápida de provisionar tudo é usar o script de configuração incluído. Do **diretório raiz do workshop**, execute:

**Windows (PowerShell):**

```powershell
.\scripts\setup.ps1
```

**Linux / macOS:**

```bash
./scripts/setup.sh
```

Este script irá:

1. Verificar todos os pré-requisitos (Azure CLI, azd, Python)
2. Fazer login no Azure e azd
3. Criar e ativar um ambiente virtual Python (`.venv`)
4. Inicializar o ambiente azd
5. Provisionar toda a infraestrutura (conta Foundry, projeto, implantação de modelo, monitoramento)
6. Instalar dependências Python no ambiente virtual
7. Escrever seu arquivo `.env` automaticamente

> **⏱ O provisionamento leva aproximadamente 5-10 minutos.**

**Flags opcionais:**

| Flag | Efeito |
|------|--------|
| `-Location swedencentral` / `-l swedencentral` | Implantar em uma região diferente |
| `-DeploySecondModel` / `-s` | Também implantar `gpt-4.1` para comparação no Lab 5 |
| `-SkipProvision` / `--skip-provision` | Pular provisionamento do Azure (se recursos já existem) |

Após o script terminar, pule para **Passo 8: Verificar no Portal Foundry** e depois **Passo 9: Validar Sua Configuração** abaixo.

---

<details>
<summary><strong>Opção B: Configuração Manual Passo a Passo</strong> (clique para expandir)</summary>

Se preferir entender cada passo, siga o processo manual abaixo.

### Passo 1: Inicializar o Ambiente azd

Do diretório raiz do workshop (que contém `azure.yaml` e a pasta `infra/`):

```bash
azd init --no-prompt -e foundry-lab
```

### Passo 2: Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual Python para manter as dependências do lab isoladas:

```bash
python -m venv .venv
```

Ative-o:

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Você deve ver `(.venv)` no prompt do seu terminal. Instale as dependências do lab:

```bash
pip install -r requirements.txt
```

> **Dica:** Visual Studio Code pode ativar o venv automaticamente -- quando solicitado, selecione o interpretador Python dentro de `.venv`.

### Passo 3: Configurar a Região do Azure

Defina a região onde você tem quota de modelo (verificada no Lab 1):

```bash
azd env set AZURE_LOCATION northcentralus
```

> **Regiões comuns com disponibilidade de modelo:** `eastus`, `eastus2`, `westus3`, `northcentralus`, `swedencentral`

### Passo 4: Defina Seu ID Principal (para RBAC)

Isto concede à sua conta de usuário as funções `Cognitive Services OpenAI User` e `Cognitive Services Contributor` no recurso de Serviços de IA provisionado:

```bash
# Obtenha seu ID de objeto do Azure AD
az ad signed-in-user show --query id -o tsv
```

```bash
azd env set AZURE_PRINCIPAL_ID <seu-id-principal>
```

### Passo 5: (Opcional) Ativar Segundo Modelo para Lab 5

Para implantar `gpt-4.1` juntamente com `gpt-4.1-mini` para o lab de comparação de modelos:

```bash
azd env set DEPLOY_SECOND_MODEL true
```

### Passo 6: Provisionar Infraestrutura

```bash
azd provision --no-prompt
```

Isto implanta os templates Bicep em `infra/` e cria:

| Recurso | Propósito |
|---------|-----------|
| Grupo de recursos (`rg-foundry-lab`) | Contentor para todos os recursos |
| Conta de Serviços de IA do Azure | Conta Foundry (host de modelo) |
| Projeto Foundry | Organiza modelos, agentes, avaliações |
| Implantação de `gpt-4.1-mini` | Modelo primário para Labs 3-4 |
| Implantação de `gpt-4.1` *(opcional)* | Segundo modelo para Lab 5 |
| Espaço de trabalho Log Analytics | Armazenamento de telemetria |
| Application Insights | Monitoramento do projeto |
| Atribuições de função RBAC | Seu usuário obtém OpenAI User + Contributor |

> **⏱ Isto leva aproximadamente 5-10 minutos.** Aguarde a conclusão.

Você verá uma saída como:

```
SUCCESS: Your application was provisioned in Azure in XX minutes XX seconds.
```

### Passo 7: Recuperar e Configurar Ambiente

Após o provisionamento, o **hook de pós-provisionamento** cria automaticamente seu arquivo `.env`. Verifique-o:

> **O que é um arquivo `.env`?** É um arquivo de texto simples que armazena valores de configuração (como seu endpoint de projeto e nome de modelo) como pares `CHAVE=VALOR`. O pacote `python-dotenv` carrega esses em seus scripts Python automaticamente via `load_dotenv()`, para que você nunca codifique segredos ou endpoints no seu código-fonte.

```bash
azd env get-values
```

Saídas principais:

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `AZURE_AI_PROJECT_ENDPOINT` | URL do seu endpoint de projeto | `https://ai-xxxx.services.ai.azure.com/api/projects/foundry-lab-project` |
| `AZURE_RESOURCE_GROUP` | Nome do grupo de recursos | `rg-foundry-lab` |
| `MODEL_DEPLOYMENT_NAME` | Modelo primário | `gpt-4.1-mini` |

Verifique se `.env` foi escrito:

```bash
cat .env
```

Se `.env` estiver faltando, copie a amostra e edite manualmente:

```bash
cp .env.sample .env
# Edite PROJECT_ENDPOINT e MODEL_DEPLOYMENT_NAME com valores de azd env get-values
```

</details>

---

## Passo 8: Verificar no Portal Foundry

1. Abra **[https://ai.azure.com](https://ai.azure.com)**
2. Você deve ver seu novo projeto listado
3. Clique no projeto e verifique:
   - O endpoint do projeto corresponde ao seu `.env`
   - Sua implantação de modelo aparece em **Implantações**

---

## Passo 9: Validar Sua Configuração

Execute o script de validação incluído para confirmar que todos os arquivos, dependências, ferramentas CLI e configuração estão corretos:

```bash
python -X utf8 src/tests/validate_lab.py
```

> **Nota:** Use o sinalizador `-X utf8` no Windows para evitar erros de codificação. No Linux/macOS você pode omiti-lo.

Você deve ver uma saída terminando com:

```
  VALIDATION SUMMARY
  Total checks: 100
  ✅ Passed:  100
  ❌ Failed:  0

  Result: PASS  - lab is ready!
```

Se alguma verificação falhar, a saída diz exatamente o que corrigir. Problemas comuns:

| Falha | Solução |
|------|---------|
| Arquivo faltando | Revise a saída do seu `azd provision` para erros |
| CLI não encontrada | Instale a ferramenta faltante (veja [SETUP.md](../setup/SETUP.md)) |
| Pacote não instalado | Execute `pip install -r requirements.txt` dentro de seu `.venv` |
| `.env` não configurado | Copie `.env.sample` para `.env` e preencha seu endpoint |

> **Dica:** Execute novamente a validação após qualquer correção para confirmar que resolve o problema.

---

## O Que Você Aprendeu

- ✅ Como provisionar um projeto Foundry usando azd com templates Bicep
- ✅ Como funciona infraestrutura como código (grupo de recursos, Serviços de IA, projeto, implantações de modelo)
- ✅ Como hooks de pós-provisionamento do azd automatizam configuração de ambiente
- ✅ Como atribuições de função RBAC concedem acesso ao modelo do seu usuário
- ✅ Como recuperar configuração de projeto para uso do SDK
- ✅ Como validar sua configuração com o script de validação automatizado

---

## Checkpoint

Antes de prosseguir, confirme o seguinte:

- [ ] Arquivo `.env` existe e contém `PROJECT_ENDPOINT` e `MODEL_DEPLOYMENT_NAME`
- [ ] `python -X utf8 src/tests/validate_lab.py` mostra todas as verificações passando
- [ ] `azd env get-values` mostra seu endpoint de projeto e grupo de recursos
- [ ] Seu projeto Foundry é visível em [ai.azure.com](https://ai.azure.com)

Se a validação falhar, verifique as mensagens de falha -- problemas comuns incluem valores `.env` faltando ou provisionamento incompleto.

---

## Conceito-Chave

> Um projeto Foundry é seu espaço de trabalho para organizar recursos de IA. O endpoint do projeto é o único ponto de conexão que seu código de aplicação precisa para acessar qualquer modelo implantado dentro dele.

---

**Próximo:** [Lab 1 - Descobrir Modelos →](./lab1-discover-models-pt-br.md)
