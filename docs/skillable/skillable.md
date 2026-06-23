@lab.Title

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

Open, Microsoft Foundry Portal +++https://ai.azure.com+++ and sign in with the following Azure credentials using the **start building** button:

Username:  
+++@lab.CloudPortalCredential(User1).Username+++

If Prompted for a temporary Access Password 'TAP'
+++@lab.CloudPortalCredential(User1).AccessToken+++

If Prompted for a Password: 
+++@lab.CloudPortalCredential(User1).Password+++


You will land on the Foundry **resources** page. This is the central hub for managing AI resources.

Ensure the new foundry switch at the top of the screen is turned on for New Foundry. 


!IMAGE[newfoundry.png](instructions343795/newfoundry.png)

If don't get the screen below."You will  have to update the current project to the latest Foundry version. Select the project listed to update. 

!IMAGE[selectproject.png](instructions343795/selectproject.png) 

Now Select the project from the available projects screen to load the project.

> [+alert] **If you are unable to view the project please see below**
> 
1. Switch to old foundry portal by toggling the New Foundry toggle at the top of the page
!IMAGE[sla1i1tp.png](instructions343795/sla1i1tp.png)
2. Click "Continue without feedback"
!IMAGE[yc6ix262.png](instructions343795/yc6ix262.png)
3. Project will be visible in old foundry portal, click on the project
!IMAGE[f71vnukz.png](instructions343795/f71vnukz.png)
4. Once in the project click on the New Foundry toggle button to return to new foundry with the project retained in the new foundry
!IMAGE[0dt15v07.png](instructions343795/0dt15v07.png)
!IMAGE[wwez4x1w.png](instructions343795/wwez4x1w.png)


---

## Step 2: Explore the Model Catalog

1. In the main windows, click **discover** from the top menu.
2. In the discover section browse the available models by clicking **view all models** -- these are production-ready, hosted models you can use without fine-tuning
4. You can use the filters within the 'Models' page to narrow down the list of models. For example you can filter by Supported features (Agent service, Fine-tuning, etc), Source (Azure OpenAI, Microsoft, Meta, Mistral, etc.) or by Inference Task (Chat Completition, Image Analysis etc). This allows you to quickly filter models based on a specific task or requirement.

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
| gpt-4.1-mini | OpenAI | Fast, cost-efficient, excellent for classification |
| gpt-4.1 | OpenAI | Higher quality, good for complex moderation |
| Phi-4 | Microsoft | Strong reasoning, open-weight |

> **Tip:** gpt-4.1-mini is the best choice for this lab -- it is fast, inexpensive, and well-suited for moderation and classification tasks.

---

## Step 4: Check Model Details

Click on your chosen model (e.g., **gpt-4.1-mini**) to view its detail page:

1. **Details** Read the model description and capabilities
2. **Deployments** -- Deployment options
3. **Benchmarks** -- Review performance metrics
4. **License** -- The Model License

> You will deploy this model programmatically in Lab 2. For now, just confirm it is available in the catalog and you can see the model card details.

---


## Step 5: Explore the Playground (Optional)

1. Select **Deploy** → Select "gpt-4.1-mini" under Use an existing deployment, which then brings you to the **playground** for the model deployment.
2. In the **instructions**, enter:

```Instructions
You are a product review moderator for Zava, a home-improvement retailer. Classify the following customer review as SAFE, NEEDS_REVIEW, or UNSAFE. Respond with only the classification label.
```

3. In the chat with model window, enter:

```Prompt
This paint is garbage and whoever designed it should be fired
```

4. Click **Send** and observe the response

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

**Next:** Lab 2 - Verify your Microsoft Foundry Project 

======


# Lab 2: Verify your Microsoft Foundry Project 

## Step 1: Verify in Foundry Portal if your already logged in moved to Step 2

1. Open +++https://ai.azure.com+++ in the browser
2. Login with username: 
+++@lab.CloudPortalCredential(User1).Username+++
and 
Password: 
+++@lab.CloudPortalCredential(User1).Password+++
2. You should see your new project listed


---

## Step 2: Open the folder in VS Code and trust the workspace

Open Visual Studio Code

Launch VS Code from the Start menu or desktop.

Open the lab folder

In VS Code, select:

File → Open Folder

Navigate to:
C:\Users\LabUser\Desktop\Build26-LAB520-main

Click Select Folder

Alternative (faster option):

Open File Explorer
Go to:
C:\Users\LabUser\Desktop\Build26-LAB520-main

Right-click in the folder and choose Open with Code (if installed)


---

## Step 3: Trust the workspace

!IMAGE[trust.png](instructions343795/trust.png)

When prompted with "Do you trust the authors of the files in this folder?"
Click Yes, I trust the authors

Select Trust

Expected outcome

The folder opens in VS Code
All features (extensions, terminals, scripts) are fully enabled
No restricted mode warnings are shown

---

## Step 4. Validate your .env is created and populated


Ensure the .env file has been created in the root of your project.

To complete the command please open a terminal within VSCode click in VSCode click on the on 'Terminal' menu -> then select 'New terminal'? before running 'Test-Path .env'. This will open a new Terminal window within VSCode.

```powershell
Test-Path .env
```
Compare .env against .env.sample

Validate that all required keys from .env.sample exist in .env.

Option A - Manual check
Open both files and confirm the following variables exist:

PROJECT_ENDPOINT
MODEL_DEPLOYMENT_NAME
MODEL_DEPLOYMENT_NAME_2 (optional)
AZURE_CONTAINER_REGISTRY_NAME (optional)

Option B - Automated Check 

Copy and paste the following into a powershell command window

```powershell

# Load sample keys
$sampleKeys = Get-Content .env.sample | Where-Object { $_ -match "=" } | ForEach-Object {
    ($_ -split "=")[0].Trim()
}

# Load env keys
$envKeys = Get-Content .env | Where-Object { $_ -match "=" } | ForEach-Object {
    ($_ -split "=")[0].Trim()
}

# Compare
$missingKeys = $sampleKeys | Where-Object { $_ -notin $envKeys }

if ($missingKeys.Count -eq 0) {
    Write-Host "✅ All required keys are present in .env"
} else {
    Write-Host "❌ Missing keys in .env:"
    $missingKeys
}
```

Option C - Visual Check using VSCode Project

Open the project in VSCode and verify:
   - The project endpoint listed at https://ai.azure.com matches your .env details in the solution.
   - Your model deployment appears under **Deployments** menu at https://ai.azure.com

You will see that the Missing Keys in the .env for MODEL_DEPLOYMENT_NAME_2 as you have only one model deployed. You will need add the details manually for an additional model deployment, and we will do this in a later lab, so do not worry this error is correct.

--- 

## Step 5: Validate Your Setup

Run the included validation script to confirm that all files, dependencies, CLI tools, and configuration are correct:

In Visual Studio Code Open a Terminal Window 

```powershell
python -X utf8 src/tests/validate_lab.py
```

> **Note:** Use the -X utf8 flag on Windows to avoid encoding errors. On Linux/macOS you can omit it.

You should see output ending with:

```output
  VALIDATION SUMMARY
  Total checks: 100
  Passed:  99
  Failed:  0
  Skipped: 1

  Result: PASS  - lab is ready!
```

If any checks fail, the output tells you exactly what to fix. Common issues:

| Failure | Fix |
|---------|-----|
| Missing file | Re-check your azd provision output for errors |
| CLI not found | Install the missing tool (see [SETUP.md](../setup/SETUP.md)) |
| Package not installed | Run pip install -r requirements.txt inside your .venv |
| .env not configured | Copy .env.sample to .env and fill in your endpoint |

> **Tip:** Re-run validation after any fix to confirm it resolves the issue.

---
## What You Learned

- ✅ How to validate your setup with the automated validation script
- ✅ Loading the workshop solution in VSCode


---

## Checkpoint

Before moving on, confirm all of the following:

- [ ] .env file exists and contains PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME
- [ ] python -X utf8 src/tests/validate_lab.py shows all checks passing
- [ ] azd env get-values shows your project endpoint and resource group
- [ ] Your Foundry project is visible at https://ai.azure.com

If validation fails, check the failure messages -- common issues include missing .env values or incomplete provisioning.

---

## Key Takeaway

> A Foundry project is your workspace for organizing AI resources. The project endpoint is the single connection point your application code needs to access any model deployed within it.

---

**Next:** Lab 3 - Connect & Inference 

======

# Lab 3: Connect and Send Your First Inference

> **Duration:** ~15 minutes | **Phase:** Code-First Interaction

## Objective

As Serena (Zava's developer), write Python code that authenticates against your Foundry project, connects to a hosted model endpoint, and sends your first inference request -- laying the groundwork for Zava's review moderation system.

---

## Concepts

| Concept | Description |
|---------|-------------|
| **AIProjectClient** | SDK client that connects to your Foundry project |
| **DefaultAzureCredential** | Automatic credential chain -- uses your az login session locally |
| **Chat Completion** | Send a system prompt + user message, receive a model response |
| **Inference Endpoint** | The API endpoint your model deployment exposes |

---

## Step 1: Review the Code

Open src/01_first_inference.py in your editor. 

The following sections walk through and explains the code in the solution step by step covering the key aspects of the solution.

### Authentication and Client Setup

```python
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

def main():
    # --- Validate environment ---
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    model = os.environ.get("MODEL_DEPLOYMENT_NAME")

    if not endpoint or endpoint.startswith("https://<"):
        print("ERROR: Set PROJECT_ENDPOINT in your .env file (see Lab 2).")
        sys.exit(1)
    if not model:
        print("ERROR: Set MODEL_DEPLOYMENT_NAME in your .env file.")
        sys.exit(1)

    # --- Connect to Foundry project ---
    print("Connecting to Foundry project...")
    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
    )
```

This creates a project client authenticated with your Azure credentials. The PROJECT_ENDPOINT comes from your .env file (configured in Lab 2).

### Getting an Inference Client

```python
inference_client = project_client.get_openai_client()
```

The project client provides an OpenAI-compatible client for chat completions. This client is pre-configured with your project's endpoint and credentials.

### Sending a Request

```python
response = inference_client.chat.completions.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    messages=[
        {"role": "system", "content": "You are a helpful assistant for Zava, a global home-improvement retailer. Respond concisely."},
        {"role": "user", "content": "What is Microsoft Foundry and how could a retailer like Zava use it? Answer in one sentence."},
    ],
)
```

The chat.completions.create() method sends a chat completion request with:

- **model** -- The deployment name (e.g., gpt-4.1-mini)
- **messages** -- An array of conversation messages with roles (system, user, assistant)

### Processing the Response

```python
print(response.choices[0].message.content)
```

The response object contains an array of choices. Each choice has a message with content -- the model's text response.

---

## Step 2: Run the Code

Make sure your .env file is configured within your solution (from Lab 2), then run the following command from a terminal windows:

To open a terminal windows in VSCode select Terminal -> new windows from the top menu in VSCode 

```powershell
python src/01_first_inference.py
```

### Expected Output (You are using a LLM non determistic solution so the output will not 100% match, simply validate message and format)

```output
Connecting to Foundry project...
Sending inference request to model: gpt-4.1-mini
---
Response:
Microsoft Foundry is a unified platform for discovering, deploying, and
managing AI models, which Zava could use to power product recommendations,
review moderation, and customer support agents at scale.
---
Model: gpt-4.1-mini
Tokens used: 52 (prompt: 30, completion: 22)
```

> **Note:** The first inference request may take 3-5 seconds due to cold start (the model endpoint warming up). Subsequent requests in the same session are typically much faster (under 2 seconds). This is normal behavior -- if you see a delay on the first call, just wait for the response.

### Troubleshooting Common Errors

If the script fails, check the table below before asking for help:

| Error | Cause | Fix |
|-------|-------|-----|
| KeyError: PROJECT_ENDPOINT | .env file is missing or incomplete | Run azd env get-values > .env to regenerate it |
| AuthenticationError or DefaultAzureCredential failed | Azure CLI session expired | Run az login and try again |
| Connection timed out after 30+ seconds | Endpoint is unreachable | Check your network/VPN; verify the endpoint URL in .env |
| ResourceNotFoundError | Model deployment name does not match | Run az cognitiveservices account deployment list to check the exact name |

---

## Step 3: Experiment

Try modifying the code to explore different behaviors:

### Change the System Prompt

Edit the system message to change the model's behavior:

```python
{"role": "system", "content": "You are Cora, Zava's friendly AI shopping assistant. Help customers find the right home-improvement products."},
```

### Change the User Input

```python
{"role": "user", "content": "I'm Bruno and I'm renovating my kitchen. What tools do I need to install new cabinets?"},
```

### Add Temperature Control

```python
response = inference_client.chat.completions.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    messages=[...],
    temperature=0.0,  # Deterministic output
)
```

| Temperature | Behavior |
|-------------|----------|
| 0.0 | Deterministic -- same input produces same output |
| 0.7 | Balanced creativity (default) |
| 1.0 | Maximum creativity / variability |

> **For Zava's review moderation tasks (Lab 4), use temperature=0.0** to get consistent, reproducible classifications.

## Experiment (Run, Observe, Learn)

Now that your code is working, this step is about **actively testing changes and observing how the model behaves**.

***

## Where to Run Your Experiments

You should run and test your changes in your **Python environment**:

* Open the root folder in your terminal or VS Code
* Run your script:

```powershell
python src/01_first_inference.py
```

Each time you make a change, re-run the script and observe the output in the terminal.

* Use **Microsoft Foundry Playground** only to compare prompt behaviour, not for debugging your code

***

## How to Experiment

Follow a simple loop:

1. Change one thing only
2. Run the script
3. Observe the output
4. Compare with previous runs

***

## Experiments to Try

### Change the System Prompt

Edit the system message to control tone and behaviour:

```python
{"role": "system", "content": "You are Cora, Zava's friendly AI shopping assistant. Help customers find the right home-improvement products."},
```

Ask:

* Does the tone change?
* Does it stay in role?
* Does it give more focused answers?

***

### Change the User Input

```python
{"role": "user", "content": "I'm Bruno and I'm renovating my kitchen. What tools do I need to install new cabinets?"},
```

Ask:

* Does adding context improve the response?
* Does it ask clarifying questions?
* What happens if the input is vague or short?

Try variations:

* "Tools for cabinets?"
* "I want to install cabinets but avoid power tools"

***

### Add Temperature Control

```python
response = inference_client.chat.completions.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    messages=[...],
    temperature=0.0,
)
```

| Temperature | Behaviour                             |
| ----------- | ------------------------------------- |
| 0.0         | Same output every time, deterministic |
| 0.7         | Balanced and natural                  |
| 1.0         | More creative and variable            |

Ask:

* Does output stay the same at 0.0?
* Does creativity increase at higher values?
* Does quality decrease at 1.0?

For classification tasks later, always use `temperature=0.0`.

***

### Add Conversation Context

Extend messages to simulate a conversation:

```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "I am installing cabinets"},
    {"role": "assistant", "content": "You will need a drill, level, and measuring tape"},
    {"role": "user", "content": "What if I have uneven walls?"}
]
```

Ask:

* Does the model remember previous steps?
* Does it give better follow-up answers?


## What You Should Be Learning

After running these experiments, you should understand:

* How prompts control behaviour
* How input affects output quality
* When to use deterministic vs creative settings
* How conversation context works
* How to recognise and diagnose common errors

***

## Tip

Add simple debug output to compare runs:

```python
print("User:", user_input)
print("Temperature:", temperature)
print("Response:\n", response.choices[0].message.content)
```
**NOTE** The debug snippet references user_input and temperature, which don't exist in 01_first_inference.py today - the user message is inlined and no temperature is passed. So you'd need to extract them into variables first, then print them.

Here's the minimal change. Replace the inference request block (around lines 42-55) of 01_first_inference.py

```Python
    # --- Send inference request ---
    user_input = "What is Microsoft Foundry and how could a retailer like Zava use it? Answer in one sentence."
    temperature = 0.7

    print(f"Sending inference request to model: {model}")
    response = inference_client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant for Zava, a global home-improvement retailer. Respond concisely.",
            },
            {
                "role": "user",
                "content": user_input,
            },
        ],
    )

    # --- Debug output (compare runs) ---
    print("User:", user_input)
    print("Temperature:", temperature)
    print("Response:\n", response.choices[0].message.content)
```

### Break It on Purpose

The best way to understand what each piece does is to remove it and see what happens. Try these experiments (undo each change before the next):

| Experiment | What to Change | What Happens |
|------------|---------------|---------------|
| Remove the system prompt | Delete the {"role": "system", ...} message | The model gives a generic answer instead of a focused one |
| Send an empty user message | Change content to "" | The model may return an empty response or ask for clarification |
| Use a nonsense model name | Change MODEL_DEPLOYMENT_NAME to "fake-model" | You get a ResourceNotFoundError -- the SDK cannot find the deployment |
| Remove load_dotenv() | Comment out the line | KeyError: PROJECT_ENDPOINT -- Python cannot read your .env file |

These errors are the same ones you will hit in real projects. Seeing them now makes them easier to diagnose later.

---

## Step 4: Understand the Response Object

The full response object contains useful metadata:

```python
print(f"Model: {response.model}")
print(f"Finish reason: {response.choices[0].finish_reason}")
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Completion tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")
```

| Field | Description |
|-------|-------------|
| model | The model that generated the response |
| finish_reason | Why generation stopped (stop, length, content_filter) |
| usage.prompt_tokens | Tokens consumed by your input |
| usage.completion_tokens | Tokens generated in the response |
| usage.total_tokens | Total tokens (drives cost) |

---

## What You Learned

- ✅ How to authenticate with DefaultAzureCredential
- ✅ How to create an AIProjectClient connected to your Foundry project
- ✅ How to obtain an inference client for chat completions
- ✅ How to send a structured message (system + user) to a model
- ✅ How to process the response programmatically
- ✅ How to read token usage metadata

---

## Checkpoint

Before moving on, confirm:

- [ ] Running python src/01_first_inference.py returns a text response (not an error)
- [ ] The output shows Model: gpt-4.1-mini (or your chosen model)
- [ ] Token usage is displayed (prompt + completion tokens)

If any of these fail, check your .env file has the correct PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME values.

---

## Key Takeaway

> Connecting to a Foundry-hosted model takes three lines of setup: load credentials, create a project client, get an OpenAI-compatible client. From there, every interaction follows the same request/response pattern.

---

**Next:** Lab 4 - Zava Review Moderation App 

=====
# Lab 4: Build a Product Review Moderation Application for Zava

> **Duration:** ~20 minutes | **Phase:** Real-World Task Implementation

## Objective

Build a working product review moderation pipeline for Zava's online store. The system accepts customer-submitted product reviews, classifies them using a Foundry-hosted model, applies moderation logic, and outputs structured results -- ensuring that reviews from customers like Bruno are safe and helpful before going live on the site.

---

## The Problem

Zava's online store receives thousands of product reviews daily across hundreds of home-improvement categories -- from power tools and paint to kitchen cabinets and smart-home devices. Manual review does not scale. Serena needs to build an automated system that can:

1. Accept a customer review as input
2. Classify it into a moderation category
3. Return a structured decision with reasoning
4. Handle edge cases gracefully

---

## Architecture

!IMAGE[architecture_lab520.png](instructions343795/architecture_lab520.png)

---

## Step 1: Review the System Prompt

The key to reliable moderation is a well-structured system prompt. Open src/02_comment_moderation.py and examine the SYSTEM_PROMPT:

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

This prompt:

- **Constrains the output format** -- JSON only, predictable structure
- **Defines clear categories** -- three-tier classification
- **Provides classification rules** -- reduces ambiguity
- **Eliminates free-text noise** -- "Do not include any text outside the JSON"

---

## Step 2: Understand the Moderation Pipeline

The application follows this flow:

### 2a. Send Comment for Classification

```python
def classify_comment(client, model: str, comment: str) -> dict:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": comment},
            ],
            temperature=0.0,  # Deterministic output
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

Key design decisions:

| Decision | Rationale |
|----------|-----------|
| temperature=0.0 | Same comment always gets the same classification |
| JSON output format | Machine-parseable, no regex needed |
| Structured system prompt | Reliable, consistent categorization |
| try/except around inference | Catches Azure content safety filter blocks gracefully |
| try/except around json.loads() | Falls back to NEEDS_REVIEW if the model returns malformed output |

### 2b. Apply Moderation Logic

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

This adds a **business logic layer** on top of the model's classification:

- High-confidence SAFE → auto-approve (review goes live on Zava's site)
- High-confidence UNSAFE → auto-block (review is rejected)
- Everything else → human review queue (Zava's trust & safety team)

### 2c. Process Results

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

> **Note:** The classify_comment function uses json.loads() to parse the model's response. Because we set temperature=0.0 and use a structured system prompt, the model reliably returns valid JSON. If you modify the prompt and see json.JSONDecodeError, check that your system prompt still instructs the model to respond in JSON format.

---

## Step 3: Run the Application

```powershell
python src/02_comment_moderation.py
```

### Expected Output 
(You are using a LLM non determistic solution so the output will not 100% match, simply validate message and format)

```output
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

> **Note:** Some test comments containing threats or explicit content may be blocked by Azure's built-in content safety filter *before* reaching the model. When this happens, the application handles it gracefully and labels the comment as UNSAFE with a "Blocked by Azure content safety filter" reason. This is expected behavior -- the content filter is an additional layer of protection in production deployments.

---

## Step 4: Test with Custom Comments

The application also accepts interactive input. Run it with the --interactive flag:

```powershell
python src/02_comment_moderation.py --interactive
```

Type comments to classify them in real time:

```output
Enter a comment (or 'quit' to exit): The cabinet hardware feels cheap for the price
Classification: NEEDS_REVIEW (confidence: 0.65)
Reason: Product complaint that could be constructive feedback or frustration
Action: 🔍 FLAGGED_FOR_REVIEW
```

---

## Step 5: Test with the Sample Dataset

The src/sample_comments.json file contains a broader set of test comments. Run the batch test:

```powershell
python src/02_comment_moderation.py --file src/sample_comments.json
```

---

## Step 6: Customize the Moderation Logic

Try adjusting the confidence thresholds in the apply_moderation function:

| Threshold Change | Effect |
|-----------------|--------|
| Lower SAFE threshold (0.8 → 0.6) | More comments auto-approved |
| Raise UNSAFE threshold (0.7 → 0.9) | Fewer auto-blocks, more human review |
| Add a NEEDS_REVIEW handler | Custom routing for borderline content |

---

## What You Learned

- ✅ How to design a system prompt for structured output (JSON)
- ✅ How to build a classification pipeline using model inference
- ✅ How to apply business logic on top of model responses
- ✅ How to process batches of content programmatically
- ✅ How to handle interactive input for real-time moderation

---

## Checkpoint

Before moving on, confirm:

- [ ] python src/02_comment_moderation.py classifies all 5 sample comments without errors
- [ ] You see all three action types: APPROVED, FLAGGED_FOR_REVIEW, and BLOCKED
- [ ] python src/02_comment_moderation.py --file src/sample_comments.json processes all 15 comments

If classifications seem inconsistent, verify you are using temperature=0.0 in your requests.

---

## Key Takeaway

> A model provides the intelligence -- your application provides the logic. By combining a structured prompt with deterministic settings and programmatic decision-making, Serena can build a production-quality review moderation system for Zava without any fine-tuning.

---

## Optional: Write a Unit Test for the Moderation Logic

The validation script (src/tests/validate_lab.py) tests setup and end-to-end inference, but it does not unit-test the business logic in isolation. Here is a quick pattern you can use to test apply_moderation without calling the model:

```python
# test_moderation.py -- run with: python test_moderation.py
import sys
sys.path.insert(0, "src")
from importlib import import_module
mod = import_module("02_comment_moderation")

def test_apply_moderation():
    # High-confidence SAFE → APPROVED
    assert mod.apply_moderation({"classification": "SAFE", "confidence": 0.95}) == "APPROVED"
    # Low-confidence SAFE → FLAGGED
    assert mod.apply_moderation({"classification": "SAFE", "confidence": 0.5}) == "FLAGGED_FOR_REVIEW"
    # High-confidence UNSAFE → BLOCKED
    assert mod.apply_moderation({"classification": "UNSAFE", "confidence": 0.9}) == "BLOCKED"
    # Low-confidence UNSAFE → FLAGGED
    assert mod.apply_moderation({"classification": "UNSAFE", "confidence": 0.3}) == "FLAGGED_FOR_REVIEW"
    # NEEDS_REVIEW always → FLAGGED
    assert mod.apply_moderation({"classification": "NEEDS_REVIEW", "confidence": 0.8}) == "FLAGGED_FOR_REVIEW"
    print("All tests passed!")

test_apply_moderation()
```

This tests the **business logic** independently from the model -- you can run it offline, in CI, and with no Azure credentials. It validates that your confidence thresholds route comments correctly.

### Reun the pytest Version

If you are familiar with pytest, here is the same coverage as a proper test module. Run the following script src/tests/test_moderation.py:

```python
# src/tests/test_moderation.py -- run with: pytest src/tests/test_moderation.py -v
import sys
sys.path.insert(0, "src")
from importlib import import_module

mod = import_module("02_comment_moderation")
apply_moderation = mod.apply_moderation
classify_comment = mod.classify_comment


class TestApplyModeration:
    """Unit tests for the business-logic layer (no model calls)."""

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

Run it with:

```powershell
pytest src/tests/test_moderation.py -v
```

Expected output:

```output
src/tests/test_moderation.py::TestApplyModeration::test_safe_high_confidence_approved PASSED
src/tests/test_moderation.py::TestApplyModeration::test_safe_low_confidence_flagged PASSED
src/tests/test_moderation.py::TestApplyModeration::test_safe_at_threshold_approved PASSED
...
9 passed in 0.02s
```

> **Why pytest?** It discovers tests automatically, gives clear failure diffs, and integrates with CI pipelines (GitHub Actions, Azure DevOps). The standalone script above is simpler to run; pytest is what you'd use in a real project.

---

**Next:** Lab 5 - Model Comparison (Optional Extension)

=====

# Lab 5: Compare Model Outputs (Optional Extension)

> **Duration:** ~15 minutes | **Phase:** Extension Challenge

## Objective

Compare how different hosted models classify the same Zava product reviews, measure response quality and latency, and help Serena make an informed decision about which model to deploy for Zava's review moderation pipeline.

---

## Why Compare Models?

Different models have different strengths:

| Model | Strengths | Trade-offs |
|-------|-----------|-----------|
| gpt-4.1-mini | Fast, cost-efficient, good for simple tasks | May miss nuance in complex cases |
| gpt-4.1 | Higher reasoning quality, better at edge cases | Slower, more expensive |
| Phi-4 | Open-weight, strong reasoning, runs on-device | May need different prompt tuning |

Comparing models on your **actual Zava review data** helps Serena make informed deployment decisions.

---

## Prerequisites

Login to your Azure Subscription 

```Powershell
az login 
```
**NOTE** This will open a login screen in a new window. Ensure you 'login with a work or school account' the login/authentication windows may be hidden behind your open windows. Minimize all open windows to see the authentication window. Once authenicated maximise your VSCode window to continue.

Username:  
+++@lab.CloudPortalCredential(User1).Username+++

If Prompted for a temporary Access Password 'TAP'
+++@lab.CloudPortalCredential(User1).AccessToken+++

If Prompted for a Password: 
+++@lab.CloudPortalCredential(User1).Password+++

You will now get a message: 
The default subscription is marked with a *; the default tenant is ---- and subscription is ----

Press 1 or Enter to select the subscription 

### Validate the subscription is set

Ensure your subscription is set to your subscription by running

```Powershell
az account set --subscription "@lab.CloudSubscription.Id"
```

This step is important to make sure all deployments and commands are executed against the correct Azure subscription where your Foundry resource is provisioned.

To complete this lab, you need **two model deployments** in your Foundry project. Update your .env:

```.env
MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
MODEL_DEPLOYMENT_NAME_2=gpt-4.1
```

You need to find your-foundry-resource-name and resource group name

- Go to +++https://ai.azure.com+++
- go to the **Operate** menu at the top 
- select **Admin** left hand menu 
- select your **Project** 
- The resource group and foundry resource name are shown in this screen

## Deploying a new model 

If you only have one model deployed, deploy a second one using: 

Update the following with foundry resource name and resource group details 

**PowerShell (Windows):**

```powershell
az cognitiveservices account deployment create `
  --name <your-foundry-resource-name> `
  --resource-group <rg-foundry-lab> `
  --deployment-name gpt-4.1 `
  --model-name gpt-4.1 `
  --model-version "2025-04-14" `
  --model-format OpenAI `
  --sku-capacity 10 `
  --sku-name "GlobalStandard"
```

**NOTE** The foundry resource name is the value of the 'parent resource' field in the resource screen on Skillable. 

### Single-Model Alternative

If you only have **one model** deployed, you can still get meaningful comparison insights by varying **how** you call it rather than **which** model you call. Try these experiments with src/02_comment_moderation.py:

**1. Compare prompt strategies** -- Edit the system prompt in classify_comment() to be stricter or more lenient:

```python
# Strict: lower tolerance
"Classify as UNSAFE if there is any negativity or personal criticism."

# Lenient: higher tolerance
"Only classify as UNSAFE if the comment contains explicit threats or slurs."
```

Run the script with each prompt and compare how classifications change for the same comments.

**2. Compare temperature settings** -- Change temperature=0.0 to temperature=0.7 and run the moderation script several times. At 0.0, results should be identical every run; at 0.7, you may see classification drift on borderline comments.

**3. Compare output formats** -- Modify the system prompt to return a plain text label instead of JSON. Compare how reliably you can parse the response vs. the structured JSON approach.

These experiments teach the same core lesson as multi-model comparison: **small changes in configuration produce measurably different results**, and you should test systematically before committing to a production setup.

---

## Step 1: Review the Comparison Code

Open src/03_model_comparison.py. The key function runs the same comment through multiple models:

```python
def compare_models(client, models: list[str], comment: str) -> list[dict]:
    results = []
    for model in models:
        start = time.time()
        result = classify_comment(client, model, comment)
        elapsed = time.time() - start
        results.append({
            "model": model,
            "classification": result["classification"],
            "confidence": result["confidence"],
            "reason": result["reason"],
            "latency_ms": round(elapsed * 1000),
        })
    return results
```

---

## Step 2: Run the Comparison

```bash
python src/03_model_comparison.py
```

### Expected Output

```output
========================================
  Model Comparison: Zava Review Moderation
========================================

Comment: "This paint is garbage and whoever designed it should be fired"

  Model         Classification  Confidence  Latency   Reason
  ------------- -------------- ----------  --------  ------
  gpt-4.1-mini   NEEDS_REVIEW   0.75        324ms     Strong negative sentiment...
  gpt-4.1        NEEDS_REVIEW   0.80        891ms     Borderline personal attack toward staff...

Comment: "You're all idiots if you shop here -- worst store ever"

  Model         Classification  Confidence  Latency   Reason
  ------------- -------------- ----------  --------  ------
  gpt-4.1-mini   UNSAFE         0.95        298ms     Contains insults directed at customers
  gpt-4.1        UNSAFE         0.98        845ms     Personal attacks targeting customers

========================================
  Comparison Summary
========================================
  Agreement rate: 100% (both models agreed on all classifications)
  Avg latency - gpt-4.1-mini: 310ms
  Avg latency - gpt-4.1:      868ms
  Cost ratio:  gpt-4.1-mini is ~10x cheaper per token
```

---

## Step 3: Analyze the Results

Look for patterns in the comparison:

### Agreement

Do both models classify comments the same way? If they disagree, which model would you trust for your use case?

### Confidence

Does the more capable model consistently give higher confidence scores? Higher confidence may justify the additional cost for borderline cases.

### Latency

How much slower is the larger model? For real-time moderation (e.g., chat), latency matters. For batch processing, it may not.

### Cost

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|----------------------|
|gpt-4.1-mini | ~$0.15 | ~$0.60 |
|gpt-4.1 | ~$2.50 | ~$10.00 |

**Estimating your lab cost:** Each moderation request uses roughly 250 input tokens (system prompt + comment) and 50 output tokens (JSON response). With 5 sample comments across 2 models, that is 10 requests total:

| | Input tokens | Output tokens | Cost per 1M tokens (input/output) | Estimated cost |
|---|---|---|---|---|
| gpt-4.1-mini | 5 × 250 = 1,250 | 5 × 50 = 250 | $0.15 / $0.60 | **$0.0003** |
| gpt-4.1 | 5 × 250 = 1,250 | 5 × 50 = 250 | $2.50 / $10.00 | **$0.006** |
| **Total for this lab** | | | | **< $0.01** |

Even running the full sample_comments.json (15 Zava reviews × 2 models = 30 requests) stays well under $0.01. The cost difference becomes meaningful at Zava's scale -- at 100,000 reviews/day, gpt-4.1-mini costs ~$5/day vs. gpt-4.1 at ~$80/day.

> **Tip:** For this type of classification task, gpt-4.1-mini often matches gpt-4.1 performance at a fraction of the cost.

---

## Step 4: Try a Hybrid Approach

A common production pattern is to use the cheaper model first and escalate disagreements to the more capable model.

The comparison script includes a --hybrid mode:

```powershell
python src/03_model_comparison.py --hybrid
```

This runs gpt-4.1-mini first. If confidence is below 0.8, it re-runs with gpt-4.1 for a second opinion.

---

## Extension Challenges

If you finish early, try these:

1. **Add a third model** -- Deploy Phi-4 and add it to the comparison
2. **Create your own test set** -- Write 10 Zava product reviews that span edge cases (returns complaints, competitor mentions, sarcastic praise)
3. **Measure consistency** -- Run the same review 5 times and check if classification varies (it should not at temperature=0.0)
4. **Adjust the prompt** -- Make the system prompt stricter about complaints toward Zava staff and see how it changes classifications

---

## What You Learned

- ✅ How to run the same inference across multiple models
- ✅ How to compare classification quality, confidence, and latency
- ✅ How to make model selection decisions based on task requirements
- ✅ How to implement a hybrid escalation pattern

---

## Key Takeaway

> Model selection is a product decision, not just a technical one. By programmatically comparing models on your actual task data, you can optimize for the right balance of quality, speed, and cost.

---

**Next:** Lab 6 - Deploy Agent

=====
# Lab 6: Deploy a Hosted Agent with the AZD AI CLI

> **Duration:** ~20 minutes | **Phase:** Final Solution -- Hosted Agent Deployment

## Objective

Deploy Zava's product review moderation logic from Lab 4 as a **hosted agent** on Microsoft Foundry Agent Service using the Azure Developer CLI (azd ai agent). This turns Serena's local Python script into a persistent, cloud-hosted service that can scale to handle Zava's daily review volume. The entire workflow -- initialization, build, deploy, invoke, monitor, and cleanup -- is driven by CLI commands.

---

## What is a Hosted Agent?

A **hosted agent** is a containerized application that runs on Foundry's managed infrastructure:

| Property | Description |
|----------|-------------|
| **Runtime** | Your code in a Docker container, managed by Foundry |
| **Adapter** | Hosting adapter exposes your agent as a REST API |
| **Protocol** | OpenAI Responses API compatible |
| **Scaling** | Automatic (configurable min/max replicas) |
| **Lifecycle** | init → deploy → invoke → monitor → cleanup via azd |
| **Identity** | Project managed identity (auto-configured) |

Unlike the scripts in Labs 3-5 which run locally, a hosted agent is a **persistent, cloud-hosted service** accessible from the Foundry Playground, other agents, or any application.

---

## Architecture

!IMAGE[mermaid_diagram2.png](instructions343795/mermaid_diagram2.png)

---

## What's New in This Lab

Labs 3-4 were pure Python -- you wrote a script, ran it locally, and saw output in your terminal. This lab introduces **three new concepts**, but do not worry: azd handles the heavy lifting for all of them.

| New concept | What it means | What you actually do |
|---|---|---|
| **Docker container** | Your agent code is packaged into a portable image | **azd up** builds it for you -- you do not write or run any Docker commands |
| **Azure Container Registry (ACR)** | Cloud storage for container images | Already provisioned in Lab 2 -- azd pushes to it automatically |
| **Hosted agent on Foundry** | A persistent REST API running your moderation logic | **azd up** deploys it; **azd ai agent invoke** calls it |

The bottom line: you will edit zero infrastructure files. The commands are **azd up** (deploy) and **azd ai agent invoke** (test).

---

## Prerequisites

- Labs 1-4 completed (Foundry project provisioned, model deployed)
- Azure Developer CLI installed with the ai agent extension:
  ```bash
  azd ext install azure.ai.agents
  azd ext upgrade azure.ai.agents
  ```
- .env file with PROJECT_ENDPOINT and MODEL_DEPLOYMENT_NAME set

> **From Lab 4 to hosted agent:** In Labs 3-4, you built Zava's review moderation pipeline that runs locally -- you send a product review, the model classifies it, and your code applies business logic. In this lab, you take that same moderation logic and deploy it as a **hosted agent** on Foundry. The agent runs in a managed container, is accessible via REST API, and can be used from the Foundry Playground, other agents (like Cora, Zava's shopping assistant), or any application. Same intelligence, now as a persistent cloud service.

---

## Step 1: Review the Agent Code

The agent source code lives in src/agent/. Three files make up the hosted agent app.py, dockerfile and agent.yml:

### src/agent/app.py -- The Agent

```python
from agent_framework import Agent
from agent_framework_foundry import FoundryChatClient
from agent_framework_foundry_hosting import ResponsesHostServer
from azure.identity import DefaultAzureCredential
....

Do not include any text outside the JSON object."""

agent = Agent(
    client=FoundryChatClient(
        project_endpoint=PROJECT_ENDPOINT,
        model=MODEL_DEPLOYMENT_NAME,
        credential=DefaultAzureCredential(),
    ),
    name="zava-review-moderation-agent",
    instructions=SYSTEM_PROMPT,  # Same Zava review moderation prompt from Lab 4
)

if __name__ == "__main__":
    ResponsesHostServer(agent).run(port=8088)
```

Key components:
- **Agent** from Microsoft Agent Framework -- defines the agent's behavior
- **FoundryChatClient** -- connects to Foundry for model inference using the current Agent Framework sample pattern
- **ResponsesHostServer(agent).run(port=8088)** -- the Foundry hosting adapter wraps your agent as an HTTP server on port 8088

### src/agent/Dockerfile -- Container Definition

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8088
CMD ["python", "-u", "app.py"]
```

### src/agent/agent.yaml -- Agent Manifest

```yaml
kind: hosted
name: zava-review-moderation-agent
description: Product review moderation agent for Zava that classifies customer reviews
protocols:
    - protocol: responses
      version: "1.0.0"
environment_variables:
    - name: AZURE_AI_PROJECT_ENDPOINT
      value: ${AZURE_AI_PROJECT_ENDPOINT}
    - name: AZURE_AI_MODEL_DEPLOYMENT_NAME
      value: ${MODEL_DEPLOYMENT_NAME}
```

The manifest tells Foundry how to configure Zava's review moderation agent -- which protocols it supports and what environment variables to inject.

---

## Step 2: Initialize the Project (Optional -- Already Done)

> **Note:** The repo already includes the agent files and azure.yaml configuration. This step shows how it was set up, for reference.

If you were starting from scratch, you would run:

**Bash (Mac/Linux):**

```bash
azd ai agent init \
    --project-id "<your-foundry-project-resource-id>" \
    --model-deployment gpt-4.1-mini \
    --protocol responses \
    --src src/agent
```

**PowerShell (Windows):**

```powershell
azd ai agent init `
    --project-id "<your-foundry-project-resource-id>" `
    --model-deployment gpt-4.1-mini `
    --protocol responses `
    --src src/agent
```

This command:
1. Detects your existing Foundry project and ACR
2. Generates agent.yaml with the agent manifest
3. Registers the agent as a service in azure.yaml
4. Sets all required azd environment variables

---

## Step 3: Test the Agent Locally

Before deploying to the cloud, validate that the agent runs correctly on your machine. This catches import errors, configuration issues, and logic bugs early.

### Install Agent Dependencies

The agent uses packages that are separate from the main lab requirements. Install them first:

```powershell
pip install -r src/agent/requirements.txt
```

### Start the Agent

Open a terminal, activate your virtual environment, and run:

```powershell
cd src/agent
python app.py
```

You should see output like:

```output
Starting Zava product review moderation agent...
  Endpoint: https://<your-resource>.services.ai.azure.com/api/projects/<your-project>
  Model:    gpt-4.1-mini
Starting hosting adapter on port 8088...
INFO:     Uvicorn running on http://0.0.0.0:8088 (Press CTRL+C to quit)
```

### Send a Test Request

Open a **second terminal** and send a test comment to the locally running agent:

```powershell
Invoke-RestMethod -Uri "http://localhost:8088/responses" `
    -Method POST -ContentType "application/json" `
    -Body '{"input": "Love this cordless drill! Battery lasts all day and the torque is impressive.", "model": "gpt-4.1-mini"}' | ConvertTo-Json -Depth 10
```

### Expected Response

Look for the output_text field in the response -- it should contain a JSON classification:

```json
{
    "classification": "SAFE",
    "confidence": 1.0,
    "reason": "Positive and constructive product feedback about a cordless drill."
}
```

### Test an Unsafe Review

```powershell
Invoke-RestMethod -Uri "http://localhost:8088/responses" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"input":"Zava employees are the worst people on earth","model":"gpt-4.1-mini"}'
```

Expected: "classification": "UNSAFE"

### Alternatively, Use the CLI

If you prefer, use **azd ai agent invoke** with the **--local** flag:

```powershell
azd ai agent invoke --local "The cabinet hardware feels cheap for the price Zava is charging"
```

> **Troubleshooting:** If you see ImportError, make sure your virtual environment is activated and the packages from src/agent/requirements.txt are installed:
> ```powershell
> pip install -r src/agent/requirements.txt
> ```

Once you've confirmed the agent works locally, press **Ctrl+C** to stop it and proceed to cloud deployment.

---

## Step 4: Deploy the Agent

Run the following command to turn off additional tools installations for AZD

```powershell
azd config set tool.firstRunCompleted true
```

Build the container image in ACR and deploy the hosted agent to Foundry:

Run the following command to set your environment endpoint

```powershell
azd env set FOUNDRY_PROJECT_ENDPOINT "https://<your-foundry-project-endpoint>"
```

Then run the deployment using AZD up

```powershell
azd up
```
**Note** You may get 404 error when deploying the agent through azd up. You can ignore that error simply ensure the output console shows the following
!IMAGE[deploysuccess.png](instructions343795/deploysuccess.png)


**Troubleshooting Tips ** 
- If you get the error: "ERROR: FOUNDRY_PROJECT_ENDPOINT is required: environment variable was not found in the current azd environment" ensure you have run

```powershell
azd env set FOUNDRY_PROJECT_ENDPOINT "https://<your-foundry-project-endpoint>"
```

- If requested to Select recommended tools to install: simply deselect the all the tools or ctrl+c then run the azd config set command

You get your endpoint from the config page at https://ai.azure.com/ for the project. 

Now re-run to deploy

```powershell
azd up 
```

### What azd up Does

1. **Provisions** -- Creates/updates infrastructure (ACR, capability host, RBAC)
2. **Builds** -- Sends src/agent/ to ACR for a remote Docker build
3. **Deploys** -- Registers a hosted agent version on Foundry Agent Service
4. **Starts** -- Launches the container and waits for it to be ready

### Expected Output

```output
Provisioning Azure resources (azd provision)
...
(✓) Done: Resource group: rg-<your-resource-group>

Deploying services (azd deploy)
  Building container image...
  (✓) Done: Container image built and pushed to ACR
  Creating hosted agent version...
  (✓) Done: Agent deployed and started

SUCCESS: Your application was provisioned and deployed to Azure.
```

> The first deployment takes 3-5 minutes. Subsequent deployments are faster.

---

## Step 5: Check Agent Status

Verify the agent is running:

```powershell
azd ai agent show
```

Use table format for the clearest status view:

```powershell
azd ai agent show --output table
```

Expected output includes:

```output
FIELD    VALUE
-----    -----
Name     zava-review-moderation-agent
Version  <latest-version>
Status   active
```

---

## Step 6: Invoke the Agent

Send messages to your hosted agent directly from the CLI:

```powershell
azd ai agent invoke "Love this cordless drill! Battery lasts all day and the torque is impressive."
```

### Expected Output

```json
{
  "classification": "SAFE",
  "confidence": 1.0,
  "reason": "Positive and constructive product feedback."
}
```

Try more examples:

```powershell
azd ai agent invoke "This paint is garbage and whoever designed it should be fired"
```

```powershell
azd ai agent invoke "Zava employees are the worst people on earth"
```

```powershell
azd ai agent invoke "Does this deck stain work on pressure-treated lumber?"
```

### Conversations

By default, **azd ai agent invoke** reuses the same conversation session. To start fresh:

```powershell
azd ai agent invoke --new-session "Fresh conversation here"
```

---

## Step 7: Test in the Microsoft Foundry Playground

The Foundry Playground at +++https://ai.azure.com+++ lets you interact with your deployed agent through a chat-style UI -- no CLI or code required. This is useful for quick testing, demos, and validating prompt behavior.

### 7.1 -- Open the Playground

1. Open in the browser +++https://ai.azure.com+++ and sign in with the same account used for **azd**
2. In the top navigation, select your **build**. If you do not see it, click **All projects** and find it under your AI Services resource
3. In the left sidebar, click **Agents**
4. Find **zava-review-moderation-agent** in the agent list -- its status should show **Version** the version of the agent after running AZD up this should incremently increase as a new version is deployed **Type** = Hosted **Created on** Date and Time stamp of last update.
5. Click the agent name to open its detail page
6. Click the **Try in Playground** button (or the **Playground** tab) to open the interactive chat UI

> **Tip:** After **azd deploy**, the output includes a direct portal link. You can also get it with:
> 
```powershell
> azd ai agent show
```
> Look for the **playground** URL in the output.

### 7.2 -- Test Classification Prompts

In the Playground chat box, type a comment and press **Send**. The agent responds with a JSON classification.

Try these test prompts to validate each classification category:

| Prompt to send | Expected classification |
|---|---|
| Love this cordless drill! Battery lasts all day.` | **SAFE** |
| The tile cutter is mediocre, I expected more for the price. | **SAFE** |
| I think this review contains sensitive personal data: SSN 123-45-6789 | **NEEDS_REVIEW** |
| Zava employees are the worst people on earth | **UNSAFE** 
| Does this deck stain work on pressure-treated lumber? | **SAFE** |

Each response should contain a structured JSON object:

```json
{
    "classification": "SAFE",
    "confidence": 1.0,
    "reason": "Positive and constructive product feedback about a cordless drill."
}
```

### 7.3 -- Review the System Prompt

The Playground shows the agent's **system prompt** (instructions) that drives the classification behavior:

1. In the Playground view, look for the **System prompt** or **Instructions** panel (usually on the right side or in the agent settings)
2. Verify it contains the Zava review moderation instructions -- the rules for classifying reviews as SAFE, NEEDS_REVIEW, or UNSAFE
3. This is the same prompt defined in src/agent/app.py as SYSTEM_PROMPT

> **Note:** The system prompt is read-only in the Playground for hosted agents -- it is baked into the container code. To change it, edit app.py and redeploy with azd deploy.

### 7.4 -- Inspect Conversation History

The Playground maintains conversation history within a session:

1. Send several prompts in sequence -- the chat window shows the full exchange
2. Each agent response appears as a message with the JSON classification
3. Click **New conversation** (or the **+** button) to start a fresh session -- useful when testing the same prompt multiple times to check consistency
4. Previous sessions are listed in the left panel -- click any session to review past interactions

### 7.5 -- Validate Edge Cases

Use the Playground to quickly test edge cases and boundary conditions:

```testcases
Empty review:
(just press Send with no text)

Ambiguous tone:
"Wow, what a 'great' product selection you have here"

Mixed content:
"The drill is excellent but the store staff are completely useless and incompetent"

Non-English:
"Este taladro es terrible y la tienda es un desastre"
```

Check that the agent returns valid JSON for every input and that the **confidence** score reflects ambiguity (lower confidence for borderline cases).

> **Troubleshooting:** If the Playground shows the agent as **Stopped** or **Activating**, wait 1-2 minutes -- the container may still be starting. Check status with azd ai agent show --output table from the CLI.

---

## Step 8: Monitor Logs

To monitor a specific interaction, first create a session and invoke the agent:


**PowerShell (Windows):**

```powershell
$SESSION_ID = [System.Guid]::NewGuid().ToString()

azd ai agent invoke "Hello" --session-id $SESSION_ID
```

Then stream logs for that session in real time:

**PowerShell (Windows):**

```powershell
azd ai agent monitor --session-id $SESSION_ID
```

Additional Monitoring Options

Stream the agent's container logs:

```powershell
azd ai agent monitor 
```

For system events (container lifecycle):

```powershell
azd ai agent monitor --type system
```

To stream logs continuously:

```powershell
azd ai agent monitor --follow
```

> Open a second terminal for log monitoring while you invoke the agent in the first.


---

## CLI Command Reference

| Command | Purpose |
|---------|---------|
| azd ai agent init | Scaffold a new hosted agent project |
| azd up | Provision + build + deploy (all-in-one) |
| azd deploy | Rebuild and redeploy (skip provisioning) |
| azd ai agent show | Check agent status |
| azd ai agent invoke "msg" | Send a message to the agent |
| azd ai agent invoke --local "msg" | Test against a locally running agent |
| azd ai agent run | Run the agent locally for development |
| azd ai agent monitor | Stream container logs |
| azd down | Delete all resources |

---

## Stretch Goal: Add a SPAM Category

Want to extend the agent before wrapping up? Try adding a fourth classification category:

1. **Edit the system prompt** in src/agent/app.py -- add SPAM to the list of valid classifications, with a description like: *"SPAM: Promotional, advertising, or off-topic content unrelated to the product being reviewed."*
2. **Update the business logic** -- decide what action SPAM reviews should get (e.g., FLAGGED_FOR_REVIEW or a new QUARANTINED action)
3. **Redeploy** -- run azd deploy to push your changes to the hosted agent
4. **Test** -- invoke the agent with a spammy review:

   ```powershell
   azd ai agent invoke "Buy cheap sunglasses at www.example.com! 50% off today only!"
   ```
5. Verify the response includes "classification": "SPAM"`

This exercise reinforces the full edit → deploy → test cycle you'd use in production.

---

## Checkpoint

Before moving on, confirm:

- [ ] azd ai agent show --output table shows **Status: active**
- [ ] azd ai agent invoke "Love this cordless drill!" returns a JSON response with "classification": "SAFE"
- [ ] The agent is visible in the Foundry Playground at +++https://ai.azure.com+++

If the agent status shows an error, check the logs with azd **ai agent monitor** for details.

---

## What You Learned

- ✅ How hosted agents package your code as managed containers on Foundry
- ✅ How the Foundry hosting adapter (**ResponsesHostServer**) turns your agent into an API
- ✅ How **azd ai agent init** scaffolds and configures a hosted agent project
- ✅ How **azd up** handles the entire build → deploy → start lifecycle
- ✅ How to invoke, monitor, and manage hosted agents via the CLI

---

## Key Takeaway

> The Zava review moderation pipeline from Lab 4 is now a **production-ready hosted agent** on Microsoft Foundry. Using the **azd ai agent** CLI, the entire workflow -- from initialization to deployment to invocation -- is just a few terminal commands. No manual Docker builds, no SDK deployment scripts, no infrastructure management.

---

**Next:** Lab 7: Workshop Summary 

======
# Lab 7: Workshop Summary and Learning Outcomes

> **Duration:** ~10 minutes | **Phase:** Reflection and Review

## Objective

Review the complete journey from discovering a model in the Foundry catalog to deploying a production-ready hosted agent for Zava's product review moderation. This lab consolidates what you built, the skills you acquired, and where to go next.

---

## Total Workshop Duration

| Lab | Title | Duration |
|-----|-------|----------|
| 1 | Discover Models in Microsoft Foundry | ~10 min |
| 2 | Create and Configure a Foundry Project | ~15 min |
| 3 | Connect and Send Your First Inference | ~15 min |
| 4 | Build a Product Review Moderation Application for Zava | ~20 min |
| 5 | Compare Model Outputs *(optional)* | ~15 min |
| 6 | Deploy a Hosted Agent | ~20 min |
| 7 | Workshop Summary and Learning Outcomes | ~10 min |
| | **Core labs (1-4, 6-7)** | **~90 min** |
| | **All labs including optional Lab 5** | **~105 min** |

---

## What You Built

Across six labs, you -- as Serena, a developer at Zava -- constructed a **product review moderation pipeline** end-to-end, from a blank terminal to a cloud-hosted agent accessible via REST API:

!IMAGE[mermaid_diagram3.png](instructions343795/mermaid_diagram3.png)

---

## Lab-by-Lab Recap

### Lab 1: Discover Models in Microsoft Foundry

| | |
|---|---|
| **What you did** | Browsed the Foundry model catalog, evaluated model properties, tested Zava review moderation prompts in the Playground |
| **Key skill** | Selecting the right model for a task based on capabilities, pricing, and quotas |
| **Outcome** | Chose **gpt-4.1-mini** as the model for Zava's review moderation |

**Core concept:** Not all models are equal -- task type, latency, cost, and region availability all factor into model selection for enterprise workloads like Zava's.

---

### Lab 2: Create and Configure a Foundry Project

| | |
|---|---|
| **What you did** | Provisioned a complete Azure environment with **azd** -- AI Services account, Foundry project, model deployment, monitoring, and RBAC |
| **Key skill** | Infrastructure-as-Code with Bicep, environment configuration with **azd** |
| **Outcome** | A fully provisioned Foundry project with a deployed model and local **.env** configuration |

**Core concept:** **azd** manages the full lifecycle -- from infrastructure provisioning to environment variables -- so you never touch the portal for deployment.

---

### Lab 3: Connect and Send Your First Inference

| | |
|---|---|
| **What you did** | Wrote Python code to authenticate with **DefaultAzureCredential** and send a chat completion request |
| **Key skill** | Using the Azure AI Projects SDK for model inference, understanding message roles and token usage |
| **Outcome** | A working script (src/01_first_inference.py) that sends prompts and receives model responses |

**Core concept:** Chat completions use a message array with system/user roles. The system message shapes the model's behavior; the user message is the input.

---

### Lab 4: Build a Product Review Moderation Application for Zava

| | |
|---|---|
| **What you did** | Designed a system prompt for structured JSON classification of Zava product reviews, built a business logic layer with confidence thresholds, processed batches of reviews |
| **Key skill** | Prompt engineering for structured output, building decision logic around model responses |
| **Outcome** | A complete moderation app (src/02_comment_moderation.py) that classifies Zava product reviews as SAFE, NEEDS_REVIEW, or UNSAFE |

**Core concept:** The real value is in the system prompt + business logic combination. The model provides classification; your code makes the decisions.

---

### Lab 5: Compare Model Outputs

| | |
|---|---|
| **What you did** | Ran the same Zava review moderation prompts through gpt-4.1-mini and gpt-4.1, compared quality, latency, and cost |
| **Key skill** | Multi-model evaluation, cost-performance trade-off analysis, hybrid escalation patterns |
| **Outcome** | A comparison script (src/03_model_comparison.py) with side-by-side results and an optional hybrid routing mode |

**Core concept:** Cheaper models often perform well enough for most inputs. Reserve expensive models for low-confidence cases -- this reduces cost while maintaining quality.

---

### Lab 6: Deploy a Hosted Agent

| | |
|---|---|
| **What you did** | Packaged Zava's review moderation logic as a Docker container, deployed it to Foundry Agent Service with **azd up**, tested via CLI and the Foundry Playground |
| **Key skill** | Containerized agent deployment, the Agent Framework SDK, hosted agent lifecycle management |
| **Outcome** | A live, cloud-hosted Zava review moderation agent accessible via the OpenAI Responses API |

**Core concept:** A hosted agent turns Serena's local Python code into a managed, scalable service -- no infrastructure management, just azd up.

---

## Skills Acquired

By completing this workshop, you gained hands-on experience with:

### Azure & Infrastructure
- Navigating the Microsoft Foundry portal and model catalog
- Provisioning infrastructure with Bicep and **azd**
- Managing Azure resources (AI Services, ACR, RBAC, monitoring)
- Understanding Foundry project architecture (accounts, projects, deployments, capability hosts)

### Python & AI Development
- Authenticating with **DefaultAzureCredential** (no hardcoded keys)
- Sending chat completion requests via the Azure AI Projects SDK
- Engineering system prompts for structured JSON output
- Building business logic around model responses
- Comparing multiple models on identical tasks

### Agent Development & Deployment
- Using the Microsoft Agent Framework (Agent, FoundryChatClient)
- Writing a Dockerfile and agent.yaml manifest
- Local testing before cloud deployment
- Deploying containerized agents to Foundry Agent Service
- Invoking and monitoring agents via azd ai agent CLI
- Testing agents in the Foundry Playground

---

## Architecture Overview

The final system you built spans local development and Azure cloud services:

!IMAGE[mermaid_diagram4.png](instructions343795/mermaid_diagram4.png)
---

## Key Files You Created or Modified

| File | Purpose | Lab |
|------|---------|-----|
| src/01_first_inference.py | First chat completion request | Lab 3 |
| src/02_comment_moderation.py | Full moderation pipeline with batch + interactive modes | Lab 4 |
| src/03_model_comparison.py | Side-by-side model evaluation | Lab 5 |
| src/agent/app.py | Hosted agent with Agent Framework SDK | Lab 6 |
| src/agent/agent.yaml | Agent manifest (protocols, env vars) | Lab 6 |
| src/agent/Dockerfile | Container definition for the agent | Lab 6 |
| src/agent/requirements.txt | Python dependencies for the agent | Lab 6 |
| .env | Local environment configuration | Lab 2 |
| azure.yaml | azd project configuration | Lab 2 |
| infra/main.bicep | Infrastructure orchestration | Lab 2 |
| infra/modules/ai-services.bicep | AI Services, project, model, ACR, capability host | Lab 2 |

---

## Key Patterns and Takeaways

### 1. Prompt Engineering Drives Behavior

The system prompt is the most important piece of your application. A well-structured prompt with clear output format instructions (SAFE/NEEDS_REVIEW/UNSAFE with JSON schema) turns a general-purpose model into a specialized classifier.

### 2. Business Logic Wraps Model Output

Models provide probabilistic output -- your code makes deterministic decisions. The confidence threshold pattern (auto-approve above 0.85, auto-block below, flag for review in between) is reusable across many AI applications.

### 3. Start Cheap, Escalate Smart

The hybrid model pattern from Lab 5 applies broadly: use a fast, cheap model for the majority of requests and only route low-confidence cases to a more capable (and expensive) model. This can reduce costs by 60-80% with minimal quality impact.

### 4. Local First, Cloud Second

Always test locally before deploying. The python app.py → curl localhost:8088 workflow catches issues that are much harder to debug in the cloud.

### 5. Infrastructure as Code, Always

Every Azure resource in this workshop is defined in Bicep and managed by azd. This means the entire environment is reproducible, version-controlled, and deletable with a single command (azd down).

---

## CLI Commands Used

A complete reference of every CLI command used across the workshop:

| Command | Lab | Purpose |
|---------|-----|---------|
| azd init | 2 | Initialize the azd project |
| azd provision | 2 | Provision Azure infrastructure |
| azd env set | 2 | Set environment variables |
| azd env get-values | 2 | View current environment config |
| python src/01_first_inference.py | 3 | Run first inference script |
| python src/02_comment_moderation.py | 4 | Run moderation pipeline |
| python src/03_model_comparison.py | 5 | Run model comparison |
| python src/agent/app.py` | 6 | Run agent locally |
| azd up | 6 | Provision + build + deploy |
| azd deploy | 6 | Rebuild and redeploy |
| azd ai agent show | 6 | Check agent status |
| azd ai agent invoke | 6 | Send message to agent |
| azd ai agent monitor | 6 | Stream agent logs |
| azd down | Cleanup | Delete all resources |

---

## Next Steps

Now that you have a working hosted agent, here are ways to extend what you built:

### Add More Classification Categories

Expand the system prompt to handle additional categories like **SPAM**, **OFF_TOPIC**, or **COMPETITOR_MENTION**. Update the business logic layer to route each category differently -- for example, Zava might want competitor mentions flagged for their marketing team.

### Add Tools to the Agent

Use the Agent Framework's tool support to give the agent capabilities beyond text classification -- for example, looking up a customer's purchase history, checking a product blocklist, or notifying Zava's trust & safety team via a webhook.

### Build a Multi-Agent Workflow

Create a second agent (e.g., a response-drafting agent) and chain it with the moderation agent. The moderation agent classifies; the response agent drafts an appropriate reply based on the classification.

### Connect to a Frontend

The hosted agent exposes an OpenAI-compatible REST API. Connect it to a web application, Slack bot, or any frontend that can make HTTP requests to **/responses**.

### Set Up CI/CD

Use GitHub Actions with **azd** to automate deployments on every push to **main**. Create **.github/workflows/deploy.yml**:

```yml
name: Deploy Moderation Agent

on:
  push:
    branches: [main]
    paths: ["src/agent/**"]

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install azd
        uses: Azure/setup-azd@v2

      - name: Log in to Azure
        uses: azure/login@v2
        with:
          client-id: ${{ vars.AZURE_CLIENT_ID }}
          tenant-id: ${{ vars.AZURE_TENANT_ID }}
          subscription-id: ${{ vars.AZURE_SUBSCRIPTION_ID }}

      - name: Deploy agent
        run: azd deploy --no-prompt
        env:
          AZURE_ENV_NAME: ${{ vars.AZURE_ENV_NAME }}
```

This workflow triggers only when agent code changes, uses workload identity federation (no stored secrets), and redeploys via **azd deploy**.

### Monitor in Production

Use Application Insights (already provisioned) to track agent performance. Open the Azure portal → your Application Insights resource → **Logs**, and run this KQL query:

```kql
requests
| where timestamp > ago(1h)
| summarize
    RequestCount = count(),
    AvgDuration = avg(duration),
    FailureRate = countif(success == false) * 100.0 / count()
  by bin(timestamp, 5m)
| order by timestamp desc
```

This shows request volume, average response time, and failure rate in 5-minute buckets -- the three metrics you need to know your agent is healthy.

---

## Try It Yourself: Final Challenge

Put everything together by building a **new classifier** from scratch. Pick one of these (or invent your own):

| Challenge | System Prompt Idea | Test Data |
|-----------|-------------------|------------|
| **Sentiment analyzer** | Classify as POSITIVE, NEGATIVE, or NEUTRAL with a confidence score | Product reviews |
| **Support ticket router** | Classify as BILLING, TECHNICAL, FEATURE_REQUEST, or OTHER | Sample support emails |
| **Language detector** | Return the language name and ISO code for any input text | Sentences in different languages |

**Steps:**
1. Copy src/02_comment_moderation.py to a new file (e.g., src/04_my_classifier.py)
2. Rewrite the system prompt for your chosen task
3. Create a sample_data.json with 5-10 test inputs
4. Run it and verify the JSON output parses correctly
5. *(Bonus)* Wrap it as a hosted agent using the same pattern from Lab 6

This exercise proves you can apply the inference → structured output → business logic pattern to **any** classification problem, not just content moderation.

---

## Clean Up

If you have not already, remove all Azure resources to avoid ongoing charges:

```powershell
azd down --force --purge
```
## Step 9: Clean Up

When you are done, clean up all Azure resources:

```powershell
azd down
```

This removes:
- The hosted agent deployment
- The container image in ACR
- Any infrastructure provisioned by **azd up**

> To just stop the agent without deleting everything, use the Foundry portal or az cognitiveservices agent stop. AZD down deletes the resource group, all resources within it, and purges any soft-deleted AI Services accounts. See [Cleanup Guide](../cleanup/CLEANUP.md) for more options.

---

## Thank You

You started with a model in a catalog and finished with a production-ready hosted agent on Microsoft Foundry. The patterns you learned -- prompt engineering, structured output, confidence-based routing, containerized deployment -- apply to any AI application, not just content moderation.

Please leave feedback for the lab experience.
!IMAGE[feedback.png](instructions343795/feedback.png)

If you encountered any issues during this lab or would like to try it self paced see 
!IMAGE[issues.png](instructions343795/issues.png)

Join the Microsoft Foundry Discord 
!IMAGE[image.jpg](instructions343795/image.jpg)

- Connect with others building on Foundry
- Ask follow-up questions
- Share what they're building and get feedback

**Happy building!**
