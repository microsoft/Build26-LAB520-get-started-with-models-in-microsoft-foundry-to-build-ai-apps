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

```bash
python src/01_first_inference.py
```

### Expected Output (You are using a LLM non determistic solution so the output will not 100% match, simply validate message and format)

```
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

```bash
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

**Next:** [Lab 4 - Zava Review Moderation App](./lab4-comment-moderation.md)

