# Configuração do Lab

> **Duração:** ~10 minutos

Complete estas etapas antes de iniciar os módulos do lab.

> **Opção rápida:** Execute `.\scripts\setup.ps1` (Windows) ou `./scripts/setup.sh` (Linux/macOS) para automatizar a instalação de **todos** os pré-requisitos, registro de provedores de recursos, provisionamento do Azure e configuração do ambiente em um único comando. Depois, vá para o Lab 1.

---

## Termos-chave

Novo no desenvolvimento de IA? Aqui estão os termos principais usados neste workshop:

| Termo | Definição |
|------|------------|
| **Inferência** | Enviar um prompt a um modelo e obter uma resposta. |
| **Token** | A unidade que modelos usam para medir texto — aproximadamente ¾ de uma palavra. O preço é por token. |
| **System prompt** | Instruções ocultas que dizem ao modelo como se comportar (ex: "classificar comentários como SEGURO ou INSEGURO"). |
| **Endpoint** | A URL à qual seu código se conecta para acessar um modelo implantado ou um projeto. |
| **Model deployment** | Um modelo específico (como `gpt-4.1-mini`) disponibilizado em seu projeto, pronto para receber solicitações de inferência. |
| **Credencial / autenticação** | Como seu código prova que tem permissão para usar recursos do Azure — geralmente via `az login` ou identidade gerenciada. |
| **Hosted agent** | Seu código empacotado como um contêiner e implantado no Foundry, acessível via API REST sem gerenciar servidores. |
| **RBAC** | Role-Based Access Control — O sistema do Azure para conceder permissões específicas a usuários e serviços. |

---

## Etapa 1: Verificar Git

```bash
git --version
```

Saída esperada: versão 2.40 ou posterior. Se não estiver instalado:

| SO | Comando de Instalação |
|----|-----------------|
| Windows | `winget install -e --id Git.Git` |
| macOS | `brew install git` |
| Ubuntu/Debian | `sudo apt-get install git` |

---

## Etapa 2: Verificar Azure CLI

```bash
az version
```

A saída esperada inclui um número de versão (ex: `2.67.0` ou posterior). Se não estiver instalado:

| SO | Comando de Instalação |
|----|-----------------|
| Windows | `winget install -e --id Microsoft.AzureCLI` |
| macOS | `brew install azure-cli` |
| Ubuntu/Debian | `curl -sL https://aka.ms/InstallAzureCLIDeb \| sudo bash` |

Ou siga o [guia de instalação do Azure CLI](https://aka.ms/installazurecli).

---

## Etapa 3: Faça login no Azure

```bash
az login
```

Complete o fluxo de autenticação baseado em navegador. Depois, verifique sua assinatura:

```bash
az account show --query "{Name:name, SubscriptionId:id, State:state}" -o table
```

Se você tiver múltiplas assinaturas, selecione a que deseja usar:

```bash
az account set --subscription "<seu-id-assinatura>"
```

---

## Etapa 4: Verificar Permissões de Função

Confirme que você tem permissões suficientes para criar recursos do Foundry:

```bash
az role assignment list \
  --assignee "$(az ad signed-in-user show --query id -o tsv)" \
  --query "[?contains(roleDefinitionName, 'Owner') || contains(roleDefinitionName, 'Contributor') || contains(roleDefinitionName, 'Azure AI')].{Role:roleDefinitionName, Scope:scope}" \
  -o table
```

Você precisa de **Owner**, **Contributor** ou **Azure AI Owner** no nível de assinatura ou grupo de recursos. Se você não tiver a função necessária, entre em contato com seu administrador do Azure antes de continuar.

---

## Etapa 5: Registrar Provedores de Recursos do Azure

O lab requer que vários provedores de recursos sejam registrados em sua assinatura:

```bash
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.OperationalInsights
az provider register --namespace Microsoft.Insights
az provider register --namespace Microsoft.ContainerRegistry
```

Verifique o status do registro:

```bash
az provider show --namespace Microsoft.CognitiveServices --query registrationState -o tsv
```

> Todos devem retornar `Registered`. O registro pode levar alguns minutos.

---

## Etapa 6: Verificar Azure Developer CLI

```bash
azd version
```

Se não estiver instalado:

| SO | Comando de Instalação |
|----|-----------------|
| Windows | `winget install -e --id Microsoft.Azd` |
| macOS/Linux | `curl -fsSL https://aka.ms/install-azd.sh \| bash` |

Ou siga o [guia de instalação do Azure Developer CLI](https://aka.ms/azure-dev/install).

Faça login no azd:

```bash
azd auth login --check-status
```

Se não estiver logado:

```bash
azd auth login
```

---

## Etapa 7: Verificar Python

```bash
python --version
```

Requer **Python 3.10 ou posterior**. Se não estiver instalado, baixe em [python.org](https://www.python.org/downloads/).

---

## Etapa 8: Criar um Ambiente Virtual

Crie e ative um ambiente virtual Python para que as dependências do lab sejam isoladas de seu Python do sistema:

```bash
python -m venv .venv
```

Ative o ambiente:

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Você deve ver `(.venv)` no prompt do seu terminal.

> **Dica:** Você precisará ativar o ambiente virtual cada vez que abrir um novo terminal para este workshop. Visual Studio Code pode fazer isso automaticamente — quando solicitado a selecionar um interpretador Python, escolha o dentro de `.venv`.

---

## Etapa 9: Instalar Dependências Python

Com o ambiente virtual ativo, instale os requisitos:

```bash
pip install -r requirements.txt
```

Isso instala:

| Pacote | Propósito |
|---------|---------|
| `azure-ai-projects` | Cliente do projeto Foundry |
| `azure-identity` | Autenticação do Azure (DefaultAzureCredential) |
| `openai` | Cliente compatível com API OpenAI |
| `python-dotenv` | Gerenciamento de variáveis de ambiente |

---

## Etapa 10: Instalar Extensões do Visual Studio Code (Recomendado)

Se você está usando Visual Studio Code, instale as extensões recomendadas:

```bash
code --install-extension ms-windows-ai-studio.windows-ai-studio
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
```

| Extensão | Propósito |
|-----------|---------|
| Foundry Toolkit | Integração do projeto Foundry |
| Python | Suporte à linguagem Python |
| Pylance | IntelliSense para Python |

---

## Etapa 11: Docker (Opcional — Apenas Lab 6)

Docker é necessário apenas se você quiser construir o contêiner do agente localmente no Lab 6. Lab 6 também suporta construções em nuvem via ACR Tasks (Docker não é necessário).

```bash
docker --version
```

Se você quiser instalá-lo: [Get Docker](https://docs.docker.com/get-docker/).

---

## Etapa 12: Preparar Arquivo de Ambiente

Copie o arquivo de ambiente de exemplo e preencha seus valores (você obterá esses valores no Lab 2):

```bash
cp .env.sample .env
```

Você preencherá `.env` com o endpoint do seu projeto e o nome da implantação do modelo durante o Lab 2.

---

## Lista de Verificação de Validação

Antes de prosseguir para o Lab 1, confirme:

- [ ] `git --version` retorna 2.40+
- [ ] `az version` retorna 2.67.0+
- [ ] `az account show` mostra uma assinatura ativa
- [ ] Você tem a função Owner/Contributor/Azure AI Owner
- [ ] Provedores de recursos registrados (`Microsoft.CognitiveServices`, etc.)
- [ ] `azd version` retorna 1.11.0+
- [ ] `azd auth login --check-status` mostra logado
- [ ] `python --version` mostra 3.10+
- [ ] Diretório `.venv` existe e está ativado (prompt mostra `(.venv)`)
- [ ] `pip install -r requirements.txt` completado com sucesso
- [ ] Extensões do Visual Studio Code instaladas (recomendado)
- [ ] Arquivo `.env` criado a partir de `.env.sample`

---

**Próximo:** [Lab 1 - Descobrir Modelos →](../docs/lab1-discover-models-pt-br.md)
