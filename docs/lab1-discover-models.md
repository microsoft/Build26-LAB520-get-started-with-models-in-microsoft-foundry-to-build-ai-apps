# Lab 1: Discover Models in Microsoft Foundry

> **Duration:** ~10 minutes | **Phase:** Orientation (UI)

## Objective

Explore the Microsoft Foundry portal to discover available hosted models, understand model capabilities, and identify a model suitable for inference-based tasks like comment moderation.

---

## Step 1: Open Microsoft Foundry Portal

Navigate to **[https://ai.azure.com](https://ai.azure.com)** and sign in with your Azure credentials.

You will land on the Foundry home page. This is the central hub for managing AI projects, models, and deployments.

---

## Step 2: Explore the Model Catalog

1. In the left navigation, click **Model catalog**
2. Browse the available models — these are production-ready, hosted models you can use without fine-tuning

Take note of the following for each model:

| Property | What to Look For |
|----------|-----------------|
| **Publisher** | OpenAI, Microsoft, Meta, Mistral, etc. |
| **Task type** | Chat completion, text generation, embeddings |
| **Deployment options** | Serverless API, managed compute |
| **Pricing tier** | Pay-as-you-go, free playground |

---

## Step 3: Identify a Model for This Lab

For this workshop, you need a model that supports **chat completion** — the ability to accept a system prompt and user messages and return a structured response.

**Recommended models for this lab:**

| Model | Publisher | Why |
|-------|-----------|-----|
| `gpt-4.1-mini` | OpenAI | Fast, cost-efficient, excellent for classification |
| `gpt-4.1` | OpenAI | Higher quality, good for complex moderation |
| `Phi-4` | Microsoft | Strong reasoning, open-weight |

> **Tip:** `gpt-4.1-mini` is the best choice for this lab — it is fast, inexpensive, and well-suited for moderation and classification tasks.

---

## Step 4: Check Model Details

Click on your chosen model (e.g., **gpt-4.1-mini**) to view its detail page:

1. **Overview** — Read the model description and capabilities
2. **Benchmarks** — Review performance metrics
3. **Try it** — Use the playground to send a test prompt (optional)

> You will deploy this model programmatically in Lab 2. For now, just confirm it is available in the catalog.

---

## Step 5: Review Quota Availability

1. Navigate to **Management** → **Quota** in the left navigation
2. Verify you have available quota for the model you selected
3. Note the **region** where your quota is allocated

If you do not have quota for your chosen model:

- Select a different model with available quota
- Or request a quota increase (this may take time — for this lab, choose an available model)

---

## Step 6: Explore the Playground (Optional)

1. Return to the model detail page
2. Click **Try in Playground** or **Deploy** → **Playground**
3. In the system message, enter:

```
You are a content moderator. Classify the following comment as SAFE, NEEDS_REVIEW, or UNSAFE. Respond with only the classification label.
```

4. In the user message, enter:

```
This product is terrible and the company should be ashamed!
```

5. Click **Send** and observe the response

This is a preview of the inference pattern you will implement in code during Labs 3 and 4.

---

## What You Learned

- ✅ How to navigate the Microsoft Foundry portal
- ✅ How to browse the model catalog
- ✅ How to identify models suitable for chat completion tasks
- ✅ How to check quota and region availability
- ✅ How a model responds to a moderation prompt

---

## Key Takeaway

> Microsoft Foundry provides access to production-ready hosted models from multiple publishers. You do not need to train, fine-tune, or host these models yourself — you simply connect to them via API and start building.

---

**Next:** [Lab 2 - Project Setup →](lab2-project-setup.md)
