# Lab 2: Verificar seu Projeto Microsoft Foundry 

## Passo 1: Verificar no Portal Foundry

1. Abra https://ai.azure.com no navegador
2. Faça login com nome de usuário e senha: 
2. Você deve ver seu novo projeto listado
3. Clique no projeto e verifique:
   - O endpoint do projeto corresponde ao seu .env
   - Sua implantação de modelo aparece em **Implantações**

---

## Passo 2: Abrir a pasta no VS Code e confiar no espaço de trabalho

Abra o Visual Studio Code

Inicie o VS Code pelo Menu Iniciar ou área de trabalho.

Abra a pasta do lab

No VS Code, selecione:

Arquivo → Abrir Pasta

Navegue para:
C:\Users\LabUser\Desktop\Build26-LAB520-main

Clique Selecionar Pasta

Alternativa (opção mais rápida):

Abra o Explorador de Arquivos
Vá para:
C:\Users\LabUser\Desktop\Build26-LAB520-main

Clique com o botão direito na pasta e escolha Abrir com Code (se instalado)

---

## Passo 3: Confiar no espaço de trabalho

![trust.png](.images/trust.png)

Quando solicitado com "Você confia nos autores dos arquivos nesta pasta?"
Clique Sim, confio nos autores

Selecione Confiar

Resultado esperado

A pasta abre no VS Code
Todos os recursos (extensões, terminais, scripts) estão totalmente habilitados
Nenhum aviso de modo restrito é exibido

---

## Passo 4. Validar que seu .env foi criado e preenchido


Certifique-se de que o arquivo .env foi criado na raiz de seu projeto.

```powershell
Test-Path .env
```
Compare .env contra .env.sample

Valide que todas as chaves necessárias de .env.sample existem em .env.

Opção A – Verificação Manual
Abra ambos os arquivos e confirme as seguintes variáveis existem:

PROJECT_ENDPOINT
MODEL_DEPLOYMENT_NAME
MODEL_DEPLOYMENT_NAME_2 (opcional)
AZURE_CONTAINER_REGISTRY_NAME (opcional)

Opção B - Verificação Automática 

Copie e cole o seguinte na janela de comando PowerShell

```powershell

# Carregar chaves de amostra
$sampleKeys = Get-Content .env.sample | Where-Object { $_ -match "=" } | ForEach-Object {
    ($_ -split "=")[0].Trim()
}

# Carregar chaves env
$envKeys = Get-Content .env | Where-Object { $_ -match "=" } | ForEach-Object {
    ($_ -split "=")[0].Trim()
}

# Comparar
$missingKeys = $sampleKeys | Where-Object { $_ -notin $envKeys }

if ($missingKeys.Count -eq 0) {
    Write-Host "✅ Todas as chaves necessárias estão presentes em .env"
} else {
    Write-Host "❌ Chaves faltando em .env:"
    $missingKeys
}
```

--- 

## Passo 5: Validar Sua Configuração

Execute o script de validação incluído para confirmar que todos os arquivos, dependências, ferramentas CLI e configuração estão corretos:

Abra uma Janela de Terminal no Visual Studio Code 

```bash
python -X utf8 src/tests/validate_lab.py
```

> **Nota:** Use o sinalizador -X utf8 no Windows para evitar erros de codificação. No Linux/macOS você pode omiti-lo.

Você deve ver uma saída terminando com:

```
  VALIDATION SUMMARY
  Total checks: 100
  Passed:  99
  Failed:  0
  Skipped: 1

  Result: PASS  - lab is ready!
```

Se alguma verificação falhar, a saída diz exatamente o que corrigir. Problemas comuns:

| Falha | Solução |
|------|---------|
| Arquivo faltando | Revise a saída do azd provision para erros |
| CLI não encontrada | Instale a ferramenta faltante (veja [SETUP.md](../setup/SETUP.md)) |
| Pacote não instalado | Execute pip install -r requirements.txt dentro de seu .venv |
| .env não configurado | Copie .env.sample para .env e preencha seu endpoint |

> **Dica:** Execute novamente a validação após qualquer correção para confirmar que resolve o problema.

---
## O Que Você Aprendeu

- ✅ Como validar sua configuração com o script de validação automatizado
- ✅ Carregando a solução do workshop no VSCode


---

## Checkpoint

Antes de prosseguir, confirme o seguinte:

- [ ] Arquivo .env existe e contém PROJECT_ENDPOINT e MODEL_DEPLOYMENT_NAME
- [ ] python -X utf8 src/tests/validate_lab.py mostra todas as verificações passando
- [ ] azd env get-values mostra seu endpoint de projeto e grupo de recursos
- [ ] Seu projeto Foundry é visível em https://ai.azure.com

Se a validação falhar, verifique as mensagens de falha -- problemas comuns incluem valores .env faltando ou provisionamento incompleto.

---

## Conceito-Chave

> Um projeto Foundry é seu espaço de trabalho para organizar recursos de IA. O endpoint do projeto é o único ponto de conexão que seu código de aplicação precisa para acessar qualquer modelo implantado dentro dele.

---
**Próximo:** [Lab 3 - Conectar e Inferência](./lab3-connect-and-infer.md)
