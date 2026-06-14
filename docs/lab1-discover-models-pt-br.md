## Bem-vindo ao Seu Ambiente de Lab

Para começar, faça login na máquina virtual usando as seguintes credenciais: +++@lab.VirtualMachine(Win11-Pro-Base).Password+++

# Lab 1: Descobrir Modelos no Microsoft Foundry

> **Duração:** ~10 minutos | **Fase:** Orientação (UI)

## Cenário

Você é **Serena**, uma desenvolvedora na **Zava** -- uma grande varejista global de melhorias para o lar que opera tanto online quanto lojas físicas. A plataforma da Zava recebe milhares de avaliações de produtos de clientes diariamente de compradores como **Bruno**, que está renovando sua cozinha. Sua tarefa é construir um sistema de moderação de avaliações automatizado que classifica as avaliações de clientes antes de irem ao vivo no site. Eventualmente, este sistema funcionará juntamente com **Cora**, a assistente de compras de IA da Zava, para manter a plataforma segura e útil.

Neste lab, você explorará o catálogo de modelos do Microsoft Foundry para encontrar um modelo que possa alimentar o pipeline de moderação de avaliações da Zava.

## Objetivo

Explore o portal Microsoft Foundry para descobrir modelos hospedados disponíveis, compreenda as capacidades do modelo e identifique um modelo adequado para tarefas baseadas em inferência, como moderação de avaliações de produtos.

---

## Passo 1: Abrir Portal Microsoft Foundry

Abra o Portal Microsoft Foundry https://ai.azure.com e faça login com as seguintes credenciais do Azure:

Faça login com seu Nome de usuário e senha do Microsoft Foundry


Você chegará na página inicial do Foundry. Este é o hub central para gerenciar projetos de IA, modelos e implantações.

Certifique-se de que o novo switch foundry na parte superior da tela está ativado.

![newfoundry.png](./images/newfoundry.png)

Você também terá que atualizar o projeto atual para a versão mais recente do Foundry. Selecione o projeto listado para atualizar.
![selectproject.png](./images/selectproject.png) 


---

## Passo 2: Explorar o Catálogo de Modelos

1. Na janela principal, clique em **Encontrar modelos** ou selecione **descobrir** no menu superior.
2. Na navegação do menu superior você agora estará em **descobrir**
3. Na janela principal, navegue pelos modelos disponíveis -- estes são modelos hospedados prontos para produção que você pode usar sem ajuste fino
4. Você pode usar os filtros de modelos dentro da página de seleção de modelos, filtrar por tipos de modelo **capacidades**, **Tarefa de Inferência**, **Conclusão de Bate-papo**, **Análise de Imagem** etc. Isto permite que você filtre rapidamente modelos com base em uma tarefa ou requisito específico.

Selecione um Modelo para visualizar o Cartão do Modelo

Tome nota do seguinte para cada modelo:

| Propriedade | O Que Procurar |
|-------------|---|
| **Publicador** | OpenAI, Microsoft, Meta, Mistral, etc. |
| **Tipo de tarefa** | Conclusão de bate-papo, geração de texto, incorporações |
| **Opções de implantação** | API sem servidor, computação gerenciada |
| **Nível de preço** | Pagamento conforme o uso, playground gratuito |
| **Benchmarks** | Desempenho e estatísticas do modelo |
| **IA Responsável** | Prompts e conclusões são passados através de uma configuração padrão de modelos de classificação de Segurança de Conteúdo de IA do Azure |

---

## Passo 3: Identificar um Modelo para Este Lab

Para este workshop, você precisa de um modelo que suporte **conclusão de bate-papo** -- a capacidade de aceitar um prompt do sistema e mensagens do usuário e retornar uma resposta estruturada.

**Modelos recomendados para este lab:**

| Modelo | Publicador | Por Quê |
|--------|-----------|--------|
| gpt-4.1-mini | OpenAI | Rápido, eficiente em custo, excelente para classificação |
| gpt-4.1 | OpenAI | Qualidade superior, bom para moderação complexa |
| Phi-4 | Microsoft | Raciocínio forte, código aberto |

> **Dica:** gpt-4.1-mini é a melhor escolha para este lab -- é rápido, barato e bem adequado para tarefas de moderação e classificação.

---

## Passo 4: Verificar Detalhes do Modelo

Clique em seu modelo escolhido (por ex., **gpt-4.1-mini**) para visualizar sua página de detalhes:

1. **Detalhes** Leia a descrição e capacidades do modelo
2. **Implantações** -- Opções de implantação
3. **Benchmarks** -- Analise métricas de desempenho
4. **Licença** -- A Licença do Modelo

> Você implantará este modelo programaticamente no Lab 2. Por enquanto, apenas confirme que está disponível no catálogo e você pode ver os detalhes do cartão do modelo.

---

## Passo 5: Explorar o Playground (Opcional)

1. Retorne à página de detalhes do modelo
2. Selecione **Implantar** → Selecione "gpt-4.1-mini" em Usar uma implantação existente, o que o leva ao **playground** para a implantação do modelo.
3. Nas **instruções**, digite:

```
You are a product review moderator for Zava, a home-improvement retailer. Classify the following customer review as SAFE, NEEDS_REVIEW, or UNSAFE. Respond with only the classification label.
```

4. Na janela de bate-papo com o modelo, digite:

```
This paint is garbage and whoever designed it should be fired
```

5. Clique em **Enviar** e observe a resposta

Este é um preview do padrão de inferência que você implementará em código durante os Labs 3 e 4 para moderar as avaliações de produtos da Zava.

---

## O Que Você Aprendeu

- ✅ Como navegar no portal Microsoft Foundry
- ✅ Como navegar pelo catálogo de modelos
- ✅ Como identificar modelos adequados para tarefas de conclusão de bate-papo
- ✅ Como verificar quota e disponibilidade de região
- ✅ Como um modelo responde a um prompt de moderação de avaliação da Zava

---

## Conceito-Chave

> Microsoft Foundry fornece acesso a modelos hospedados prontos para produção de vários publicadores. Você não precisa treinar, ajustar ou hospedar esses modelos você mesmo -- você simplesmente se conecta a eles via API e começa a construir. Para Zava, isso significa que Serena pode ter um protótipo de moderação de avaliações funcionando em horas, não semanas.

---

**Próximo:** [Lab 2 - Verifique seu Projeto Microsoft Foundry](./lab2-verifysetup.md) 
