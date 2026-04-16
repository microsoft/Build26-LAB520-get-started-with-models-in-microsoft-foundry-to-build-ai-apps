<p align="center">
<img src="img/banner-build-26.png" alt="Microsoft Build 2026" width="1200"/>
</p>

# [Microsoft Build 2026](https://build.microsoft.com)

## 🔥 LAB520: Get Started with Models in Microsoft Foundry: From First Inference to Deployed Agent

### Scenario: Zava

**Zava** is a fictional global home-improvement retailer used across Microsoft demos and labs to provide a consistent, realistic enterprise narrative. In this lab, you play the role of **Serena**, a developer at Zava, tasked with building an automated product review moderation system. Customers like **Bruno** -- who is renovating his kitchen -- leave reviews on Zava's online store, and your system must classify them as safe, needs review, or unsafe before they go live. The moderation agent you build could eventually work alongside **Cora**, Zava's AI shopping assistant.

### Session Description

In this hands-on lab, you will go from zero to a production-ready application using Microsoft Foundry, with no fine-tuning or deep ML expertise required. Starting with the Foundry model catalog, you will provision a project, connect to a hosted model via the OpenAI SDK (through the Azure AI Projects client), and build a complete product review moderation pipeline for Zava that classifies customer-submitted reviews as safe, needs review, or unsafe. You will compare outputs across models to make informed deployment decisions, then package your moderation logic into a hosted agent running on Foundry's managed infrastructure. By the end of the lab, you will have working Python code, a deployed agent accessible via the OpenAI Responses API, and the confidence to integrate production-ready models into your own applications.

### 🏫 Getting started in a guided session

To get started in a guided lab session:
- Open the lab environment provided by your instructor
- Run `.\scripts\setup.ps1` (Windows) or `./scripts/setup.sh` (Linux/macOS) to provision Azure resources and configure your environment
- Start with [Lab 1: Discover Models](docs/lab1-discover-models.md)

### 🏠 Getting started in your own environment

If you are following these steps at your own pace:
- Clone this repository and open it in Visual Studio Code
- Ensure you have Python 3.10+, Azure CLI, and Azure Developer CLI installed (see [Setup Guide](setup/SETUP.md) for details)
- Run `.\scripts\setup.ps1` (Windows) or `./scripts/setup.sh` (Linux/macOS) to provision Azure resources and configure your environment
- Start with [Lab 1: Discover Models](docs/lab1-discover-models.md)

> ⚠️ This lab provisions Azure resources that may incur costs on your subscription. See [Cleanup](cleanup/CLEANUP.md) when you are done.

### 🧠 Learning Outcomes

By the end of this lab, you will be able to:

- Discover, provision, and connect to hosted models in Microsoft Foundry using the Azure AI Projects SDK and OpenAI client
- Build a complete product review moderation pipeline for Zava that classifies customer reviews as safe, needs review, or unsafe -- and compare outputs across models
- Package moderation logic into a hosted agent and deploy it to Microsoft Foundry's managed infrastructure

### 💬 Keep Learning with Copilot

Try these prompts with GitHub Copilot to explore the topics from this lab. Open Copilot Chat in Visual Studio Code (`Ctrl+Alt+I` on Windows/Linux, `Cmd+Shift+I` on Mac), paste a prompt, and see what you learn. Try connecting the [Microsoft Learn MCP Server](#-microsoft-learn-mcp-server) for the latest official documentation.

Use these as a starting point -- or write your own!

1. Understand the basics:

```
Explain how Microsoft Foundry model inference works and how the Azure AI Projects SDK provides an OpenAI-compatible client
```

2. Go deeper with docs:

```
Using the Microsoft Learn MCP Server, find the latest documentation on Microsoft Foundry hosted agents and walk me through how to create one
```

3. Extend the moderation pipeline:

```
Help me extend Zava's product review moderation system from this lab to support multiple languages and add a confidence threshold that routes low-confidence results to human review
```

4. Explore model comparison:

```
Compare the trade-offs between gpt-4.1-mini and gpt-4.1 for product review classification tasks at Zava's scale -- when should I choose one over the other?
```

5. Build something new:

```
Help me adapt the Zava review moderation agent from this lab into a customer support triage agent that classifies incoming tickets by urgency and department
```

### 💻 Technologies Used

1. [Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/)
1. [OpenAI SDK](https://learn.microsoft.com/azure/foundry/how-to/model-inference-to-openai-migration) (via Azure AI Projects client)
1. [Python](https://www.python.org/)
1. [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/)
1. [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)

### 📚 Resources and Next Steps

| Resource | Description |
|:---------|:------------|
| [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/) | Official docs for Microsoft Foundry projects, models, and agents |
| [OpenAI SDK migration guide](https://learn.microsoft.com/azure/foundry/how-to/model-inference-to-openai-migration) | Migration guide and reference for the OpenAI SDK used in this lab |
| [Azure Developer CLI documentation](https://learn.microsoft.com/azure/developer/azure-developer-cli/) | Getting started with azd for provisioning and deploying |
| [Foundry Toolkit for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) | Visual Studio Code extension for working with Foundry projects |
| [Build 2026 next steps](https://aka.ms/build26-next-steps) | Continue your learning journey after Build 2026 |


### 🌟 Microsoft Learn MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D)

The Microsoft Learn MCP Server is a remote MCP Server that enables clients like GitHub Copilot and other AI agents to bring trusted and up-to-date information directly from Microsoft's official documentation. Get started by using the one-click button above for VSCode or access the [mcp.json](.vscode/mcp.json) file included in this repo.

For more information, setup instructions for other dev clients, and to post comments and questions, visit our Learn MCP Server GitHub repo at [https://github.com/MicrosoftDocs/MCP](https://github.com/MicrosoftDocs/MCP). Find other MCP Servers to connect your agent to at [https://mcp.azure.com](https://mcp.azure.com).

*Note: When you use the Learn MCP Server, you agree with [Microsoft Learn](https://learn.microsoft.com/en-us/legal/termsofuse) and [Microsoft API Terms](https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use) of Use.*

## Content Owners

<table>
<tr>
    <td align="center"><a href="https://github.com/leestott">
        <img src="https://github.com/leestott.png" width="100px;" alt="Lee Stott"/><br />
        <sub><b>Lee Stott</b></sub></a><br />
            <a href="https://github.com/leestott" title="talk">📢</a>
    </td>
</tr></table>

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit [Contributor License Agreements](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
