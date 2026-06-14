# Instruções de Limpeza

Após concluir o workshop, remova os recursos do Azure para evitar cobranças contínuas.

---

## Opção 1: Deletar via Azure Developer CLI (Recomendado)

Se você provisionou usando `azd provision`, a limpeza mais rápida é:

```bash
azd down --force --purge
```

| Flag | Propósito |
|------|---------|
| `--force` | Pular prompts de confirmação |
| `--purge` | Deletar permanentemente recursos com exclusão reversível (AI Services, Key Vault) |

Isso remove todo o grupo de recursos e todos os recursos dentro dele.

---

## Opção 2: Deletar via Azure CLI

Se você preferir deletar recursos manualmente:

### Deletar o grupo de recursos

```bash
az group delete --name rg-foundry-lab --yes --no-wait
```

### Limpar AI Services com exclusão reversível (se aplicável)

```bash
az cognitiveservices account purge \
  --name <seu-nome-recurso-foundry> \
  --resource-group rg-foundry-lab \
  --location <sua-regiao>
```

---

## Opção 3: Deletar via Portal do Azure

1. Navegue até **[https://portal.azure.com](https://portal.azure.com)**
2. Procure por **Grupos de recursos**
3. Encontre `rg-foundry-lab`
4. Clique em **Deletar grupo de recursos**
5. Digite o nome do grupo de recursos para confirmar
6. Clique em **Deletar**

---

## Limpeza Local

Remova arquivos locais criados durante o workshop:

```bash
# Remover o diretório do projeto azd
rm -rf foundry-project

# Remover ambiente virtual Python (se criado)
rm -rf .venv

# Remover arquivo .env (contém seu endpoint)
rm .env
```

---

## Verificar Limpeza

Confirme que todos os recursos foram deletados:

```bash
az group show --name rg-foundry-lab 2>&1
```

Saída esperada: `Resource group 'rg-foundry-lab' could not be found.`

---

## Nota de Custo

Se você **não** deletar seus recursos:

- **Implantações de modelo** incorrem em cobranças com base na capacidade provisionada (tokens por minuto)
- **Recurso AI Services** tem um custo base dependendo do SKU
- **Application Insights** pode gerar cobranças de ingestão

Delete recursos prontamente após concluir o lab para evitar cobranças inesperadas.
