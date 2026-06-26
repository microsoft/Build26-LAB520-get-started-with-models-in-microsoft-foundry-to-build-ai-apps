## Welcome to Your Lab Environment

To begin, log into the virtual machine using the following credentials: +++@lab.VirtualMachine(Win11-Pro-Base).Password+++

# Lab 1: Discover Models in Microsoft Foundry

> **Duration:** ~10 minutes | **Phase:** Orientation (UI)

## Scenario

You are **Serena**, a developer at **Zava** -- a large global home-improvement retailer that operates both online and physical stores. Zava's platform receives thousands of customer product reviews daily from shoppers like **Bruno**, who is renovating his kitchen. Your task is to build an automated review moderation system that classifies customer reviews before they go live on the site. Eventually, this system will work alongside **Cora**, Zava's AI shopping assistant, to keep the platform safe and helpful.

In this lab, you will explore the Microsoft Foundry model catalog to find a model that can power Zava's review moderation pipeline.

## Objective

Explore the Microsoft Foundry portal to discover available hosted models, understand model capabilities, and identify a model suitable for inference-based tasks like product review moderation.

---

## Step 1: Open Microsoft Foundry Portal

Open, Microsoft Foundry Portal https://ai.azure.com and sign in with the following Azure credentials:

Login with your Microsoft Foundry Username and password


You will land on the Foundry home page. This is the central hub for managing AI projects, models, and deployments.

Ensure the new foundry switch at the top of the screen is turned on. 

![newfoundry.png](./images/newfoundry.png)

You will also have to update the current project to the latest Foundry version. Select the project listed to update.
![selectproject.png](./images/selectproject.png) 


---

## Step 2: Explore the Model Catalog

1. In the main windows, click **Find models** or select **discover** from the top menu.
2. In the top menu navigation you will now be in **discover**
3. In the main window browse the available models -- these are production-ready, hosted models you can use without fine-tuning
4. You can use the filters models within the model select page, filter for model types **capabilities**, **Inference task**, **Chat Completition**, **Image Analysis** etc This allow you to quickly filter models based on a specific task or requirement.

Select a Model to view the Model Card

Take note of the following for each model:

| Property | What to Look For |
|----------|-----------------|
| **Publisher** | OpenAI, Microsoft, Meta, Mistral, etc. |
| **Task type** | Chat completion, text generation, embeddings |
| **Deployment options** | Serverless API, managed compute |
| **Pricing tier** | Pay-as-you-go, free playground |
| **Benchmarks** | Model performance and stats|
| **Responsible AI** | Prompts and completions are passed through a default configuration of Azure AI Content Safety classification models |

---

## Step 3: Identify a Model for This Lab

For this workshop, you need a model that supports **chat completion** -- the ability to accept a system prompt and user messages and return a structured response.

**Recommended models for this lab:**

| Model | Publisher | Why |
|-------|-----------|-----|
| gpt-5.4-mini | OpenAI | Fast, cost-efficient, excellent for classification |
| gpt-5.4 | OpenAI | Higher quality, good for complex moderation |
| Phi-4 | Microsoft | Strong reasoning, open-weight |

> **Tip:** gpt-5.4-mini is the best choice for this lab -- it is fast, inexpensive, and well-suited for moderation and classification tasks.

---

## Step 4: Check Model Details

Click on your chosen model (e.g., **gpt-5.4-mini**) to view its detail page:

1. **Details** Read the model description and capabilities
2. **Deployments** -- Deployment options
2. **Benchmarks** -- Review performance metrics
3. **License** -- The Model License

> You will deploy this model programmatically in Lab 2. For now, just confirm it is available in the catalog and you can see the model card details.

---


## Step 5: Explore the Playground (Optional)

1. Return to the model detail page
2. Select **Deploy** → Select "gpt-5.4-mini" under Use an existing deployment, which then brings you to the **playground** for the model deployment.
3. In the **instructions**, enter:

```
You are a product review moderator for Zava, a home-improvement retailer. Classify the following customer review as SAFE, NEEDS_REVIEW, or UNSAFE. Respond with only the classification label.
```

4. In the chat with model window, enter:

```
This paint is garbage and whoever designed it should be fired
```

5. Click **Send** and observe the response

This is a preview of the inference pattern you will implement in code during Labs 3 and 4 to moderate Zava product reviews.

---

## What You Learned

- ✅ How to navigate the Microsoft Foundry portal
- ✅ How to browse the model catalog
- ✅ How to identify models suitable for chat completion tasks
- ✅ How to check quota and region availability
- ✅ How a model responds to a Zava review moderation prompt

---

## Key Takeaway

> Microsoft Foundry provides access to production-ready hosted models from multiple publishers. You do not need to train, fine-tune, or host these models yourself -- you simply connect to them via API and start building. For Zava, this means Serena can have a working review moderation prototype in hours, not weeks.

---

**Next:** [Lab 2 - Verify your Microsoft Foundry Project](./lab2-verifysetup.md) 

