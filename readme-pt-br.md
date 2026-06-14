<p align="center">
<img src="img/banner-build-26.png" alt="Microsoft Build 2026" width="1200"/>
</p>

# [Microsoft Build 2026](https://build.microsoft.com)

## 🔥 LAB520: Começando com modelos no Microsoft Foundry: da primeira inferência ao agente implantado

### Cenário: Zava

A **Zava** é uma varejista global fictícia de artigos para casa usada em demos e labs da Microsoft para oferecer uma narrativa empresarial consistente e realista. Neste lab, você assume o papel de **Serena**, uma desenvolvedora da Zava, encarregada de criar um sistema automatizado de moderação de avaliações de produtos. Clientes como **Bruno** -- que está reformando a cozinha -- deixam avaliações na loja online da Zava, e seu sistema deve classificá-las como seguras, precisam de revisão ou inseguras antes de irem ao ar. O agente de moderação que você criar poderá, futuramente, atuar junto com a **Cora**, a assistente de compras com IA da Zava.

### Descrição da sessão

Neste lab prático, você sairá do zero para uma aplicação pronta para produção usando o Microsoft Foundry, sem necessidade de fine-tuning ou conhecimento aprofundado em ML. Começando pelo catálogo de modelos do Foundry, você provisionará um projeto, conectará a um modelo hospedado via SDK do OpenAI (por meio do cliente Azure AI Projects) e criará um pipeline completo de moderação de avaliações de produtos para a Zava, classificando avaliações enviadas por clientes como seguras, precisam de revisão ou inseguras. Você comparará saídas entre modelos para tomar decisões informadas de implantação e, em seguida, empacotará sua lógica de moderação em um agente hospedado executando na infraestrutura gerenciada do Foundry. Ao final do lab, você terá código Python funcional, um agente implantado acessível via OpenAI Responses API e confiança para integrar modelos prontos para produção em suas próprias aplicações.

### 🏫 Como começar em uma sessão guiada

Para começar em uma sessão de lab guiada:
- Abra o ambiente de lab fornecido pelo instrutor
- Execute `.\scripts\setup.ps1` (Windows) ou `./scripts/setup.sh` (Linux/macOS) para provisionar recursos do Azure e configurar seu ambiente
- Comece pelo [Lab 1: Discover Models](docs/lab1-discover-models-pt-br.md)

### 🏠 Como começar no seu próprio ambiente

Se você estiver seguindo estes passos no seu ritmo:
- Faça o clone deste repositório e abra-o no Visual Studio Code
- Garanta que você tenha Python 3.10+, Azure CLI e Azure Developer CLI instalados (veja o [Guia de Setup](setup/SETUP-pt-br.md) para detalhes)
- Execute `.\scripts\setup.ps1` (Windows) ou `./scripts/setup.sh` (Linux/macOS) para provisionar recursos do Azure e configurar seu ambiente
- Comece pelo [Lab 1: Discover Models](docs/lab1-discover-models-pt-br.md)

> ⚠️ Este lab provisiona recursos do Azure que podem gerar custos na sua assinatura. Consulte [Cleanup](cleanup/CLEANUP-pt-br.md) ao finalizar.

### 🧠 Resultados de aprendizado

Ao final deste lab, você será capaz de:

- Descobrir, provisionar e conectar-se a modelos hospedados no Microsoft Foundry usando o SDK do Azure AI Projects e o cliente OpenAI
- Criar um pipeline completo de moderação de avaliações de produtos para a Zava que classifica avaliações como seguras, precisam de revisão ou inseguras -- e comparar saídas entre modelos
- Empacotar a lógica de moderação em um agente hospedado e implantá-lo na infraestrutura gerenciada do Microsoft Foundry

### 💬 Continue aprendendo com o Copilot

Experimente estes prompts com o GitHub Copilot para explorar os tópicos deste lab. Abra o Copilot Chat no Visual Studio Code (`Ctrl+Alt+I` no Windows/Linux, `Cmd+Shift+I` no Mac), cole um prompt e veja o que aprende. Tente conectar o [Microsoft Learn MCP Server](#-microsoft-learn-mcp-server) para acessar a documentação oficial mais recente.

Use estes exemplos como ponto de partida -- ou escreva os seus próprios!

1. Entenda o básico:

```
Explain how Microsoft Foundry model inference works and how the Azure AI Projects SDK provides an OpenAI-compatible client
```

2. Aprofunde com documentação:

```
Using the Microsoft Learn MCP Server, find the latest documentation on Microsoft Foundry hosted agents and walk me through how to create one
```

3. Expanda o pipeline de moderação:

```
Help me extend Zava's product review moderation system from this lab to support multiple languages and add a confidence threshold that routes low-confidence results to human review
```

4. Explore comparação de modelos:

```
Compare the trade-offs between gpt-4.1-mini and gpt-4.1 for product review classification tasks at Zava's scale -- when should I choose one over the other?
```

5. Crie algo novo:

```
Help me adapt the Zava review moderation agent from this lab into a customer support triage agent that classifies incoming tickets by urgency and department
```

### 💻 Tecnologias utilizadas

1. [Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
1. [OpenAI SDK](https://learn.microsoft.com/azure/foundry/how-to/model-inference-to-openai-migration) (via cliente Azure AI Projects)
1. [Python](https://www.python.org/)
1. [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/)
1. [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)

### 📚 Recursos e próximos passos

| Recurso | Descrição |
|:---------|:------------|
| [Documentação do Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/) | Documentação oficial para projetos, modelos e agentes no Microsoft Foundry |
| [Guia de migração do OpenAI SDK](https://learn.microsoft.com/azure/foundry/how-to/model-inference-to-openai-migration) | Guia de migração e referência para o OpenAI SDK usado neste lab |
| [Documentação do Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/) | Introdução ao azd para provisionamento e implantação |
| [Foundry Toolkit para Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) | Extensão do Visual Studio Code para trabalhar com projetos do Foundry |
| [Próximos passos do Build 2026](https://aka.ms/build26-next-steps) | Continue sua jornada de aprendizado após o Build 2026 |


Encontre outros desenvolvedores, como você, criando com Microsoft Foundry no Discord

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/bSC7dqjAU5)


### 🌟 Microsoft Learn MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D)

O Microsoft Learn MCP Server é um servidor MCP remoto que permite que clientes como GitHub Copilot e outros agentes de IA tragam informações confiáveis e atualizadas diretamente da documentação oficial da Microsoft. Comece usando o botão de instalação com um clique acima para VSCode ou acesse o arquivo [mcp.json](.vscode/mcp.json) incluído neste repositório.

Para mais informações, instruções de configuração para outros clientes de desenvolvimento e para enviar comentários e dúvidas, visite o repositório do Learn MCP Server em [https://github.com/MicrosoftDocs/MCP](https://github.com/MicrosoftDocs/MCP). Encontre outros MCP Servers para conectar ao seu agente em [https://mcp.azure.com](https://mcp.azure.com).

*Observação: ao usar o Learn MCP Server, você concorda com os Termos de Uso do [Microsoft Learn](https://learn.microsoft.com/en-us/legal/termsofuse) e dos [Microsoft APIs](https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use).*

## Responsáveis pelo conteúdo

<table>
<tr>
    <td align="center"><a href="https://github.com/leestott">
        <img src="https://github.com/leestott.png" width="100px;" alt="Lee Stott"/><br />
        <sub><b>Lee Stott</b></sub></a><br />
            <a href="https://github.com/leestott" title="talk">📢</a>
    </td>
</tr></table>

## Contribuição

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que você concorde com um
Contrato de Licença de Contribuidor (CLA), declarando que você tem o direito de, e de fato concede, os
direitos de uso da sua contribuição. Para detalhes, visite [Contributor License Agreements](https://cla.opensource.microsoft.com).

Quando você envia um pull request, um bot de CLA determina automaticamente se você precisa fornecer
um CLA e marca o PR adequadamente (por exemplo, verificação de status, comentário). Basta seguir as instruções
fornecidas pelo bot. Você só precisará fazer isso uma vez em todos os repositórios que usam nosso CLA.

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para mais informações, consulte o [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ou
entre em contato por [opencode@microsoft.com](mailto:opencode@microsoft.com) em caso de dúvidas ou comentários adicionais.

## Marcas registradas

Este projeto pode conter marcas registradas ou logotipos de projetos, produtos ou serviços. O uso autorizado de marcas
registradas ou logotipos da Microsoft está sujeito e deve seguir as
[Diretrizes de Marca e Uso de Marcas Registradas da Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
O uso de marcas registradas ou logotipos da Microsoft em versões modificadas deste projeto não deve causar confusão nem sugerir patrocínio da Microsoft.
Qualquer uso de marcas registradas ou logotipos de terceiros está sujeito às políticas desses terceiros.
