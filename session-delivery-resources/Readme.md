# LAB520 — Session Delivery Resources

**Get Started with Models in Microsoft Foundry: From First Inference to Deployed Agent**

This folder contains everything a trainer, proctor, or session deliverer needs to run **LAB520** at Microsoft Build 2026 or to re-deliver it at user groups, internal enablement sessions, MVP/community events, and customer workshops.

> 📄 The companion file [`LAB520-Train-the-Trainer.pdf`](LAB520-Train-the-Trainer.pdf) is the authoritative train-the-trainer deck. Read it end-to-end before you deliver this lab. This README is the quick reference that wraps around it.

---

## 👤 Who this guide is for

- **Lead presenters** delivering the 75-minute lab session on stage or in a hands-on lab room
- **Proctors** supporting attendees on the floor during the lab
- **Community speakers / MVPs** re-delivering this content at user groups, meetups, or internal events
- **Customer-facing engineers** running this as a customer workshop

If you are an **attendee** working through the lab, start at the root [README](../README.md) and [docs/lab1-discover-models.md](../docs/lab1-discover-models.md) instead.

---

## ⏱ Session at a glance

| Block | Duration | Content type | Notes |
|:------|:---------|:-------------|:------|
| Introduction — Zava scenario, what is Microsoft Foundry | 3 min | Speaker only | Set the story: attendees are "Serena" at Zava |
| Lab 1: Discover Models in Microsoft Foundry | 10 min | Demo | Foundry portal walk-through, model catalog, quota |
| Lab 2: Create and Configure a Foundry Project | 10 min | Demo | `setup.ps1` / `setup.sh` provisions everything via `azd` + Bicep |
| Lab 3: Connect and Send Your First Inference | 12 min | Demo | `AIProjectClient` + `get_openai_client()` |
| Lab 4: Build a Product Review Moderation Application | 20 min | Demo | Structured JSON prompt → business logic → batch run |
| Lab 6: Deploy a Hosted Agent | 15 min | Demo | `azd up` builds container, deploys to Foundry Agent Service |
| Lab 7: Summary, takeaways, Q&A, next steps | 5 min | Speaker only | Point to Lab 5 as self-paced extension |
| **Total** | **75 min** | | |

**Lab 5 (Model Comparison)** is intentionally **not** in the 75-minute flow. It is a self-paced extension attendees can complete at home — call it out at the end.

Full timing detail is in [`../session-outline.md`](../session-outline.md).

---

## 🎯 Learning outcomes you are delivering

Reinforce these three messages at the start, in the middle, and at the close:

1. Attendees can **discover, provision, and connect** to hosted models in Microsoft Foundry — zero to a working inference call in minutes.
2. Attendees can **build a production-quality moderation pipeline** that returns structured JSON, with business logic on top.
3. Attendees can **package and deploy a hosted agent** with `azd up` — no infrastructure management.

If an attendee leaves with only one of these, make it #1 (Foundry + OpenAI SDK pattern is the foundation).

---

## ✅ Pre-session checklist (do this 24–48 hours before delivery)

### Trainer environment
- [ ] Clone the repo locally and complete the full lab end-to-end yourself **at least once** on the exact machine you will demo from.
- [ ] Verify Python 3.10+, Azure CLI, Azure Developer CLI (`azd`), Docker (or the lab container host), and Git are installed and on PATH.
- [ ] Sign in: `az login` and `azd auth login` — confirm the subscription you are using has quota for **gpt-5.4-mini** in your chosen region (see [setup/SETUP.md](../setup/SETUP.md) and [setup/armsetup.md](../setup/armsetup.md)).
- [ ] Run `.\scripts\setup.ps1` (or `./scripts/setup.sh`) and confirm a clean provision. Capture the resource group name — you may want to leave it provisioned to skip Lab 2 wait time on stage.
- [ ] Run `src/01_first_inference.py`, `src/02_comment_moderation.py`, and the agent in `src/agent/` to confirm everything works.
- [ ] Pre-pull any container images and warm `azd` so the first `azd up` on stage is fast.

### Slides, screen, network
- [ ] Confirm the slide deck version matches the lab version (check the title slide against `session-outline.md`).
- [ ] Increase terminal and editor font size — aim for back-of-room readability (16pt+ terminal, 18pt+ editor).
- [ ] Hide secrets: scrub `.env`, browser tabs, and shell history. Use a fresh terminal profile if possible.
- [ ] Have the Foundry portal ([ai.azure.com](https://ai.azure.com)) signed in on a separate tab/window.
- [ ] Test your microphone, screen share, and recording (if applicable).

### Attendee environment (hands-on lab rooms)
- [ ] Confirm with the lab venue that each attendee VM/seat has: Python 3.10+, Azure CLI, `azd`, Git, VS Code, Docker.
- [ ] Confirm each attendee has a pre-assigned Azure subscription or pass-through credentials with **Contributor** + **Cognitive Services Contributor** on the target subscription/RG.
- [ ] Confirm model quota is available in the region used by the seat assignments.
- [ ] Print or pin the [setup guide](../setup/SETUP.md) and [Lab 1 link](../docs/lab1-discover-models.md) on every seat.

### Proctors
- [ ] Make sure every proctor has done the lab themselves at least once.
- [ ] Share the [troubleshooting cheat sheet](#-troubleshooting-cheat-sheet-for-proctors) below.
- [ ] Agree on a hand-signal / raised-card system so attendees can flag for help without interrupting the speaker.

---

## 🧭 Delivery flow — what to say and do, lab by lab

### Introduction (3 min) — set the scene

- Introduce **Zava** (fictional global home-improvement retailer) and the role attendees play: **Serena**, a developer building review moderation.
- Customer persona: **Bruno**, renovating his kitchen, leaves reviews that need to be classified before they go live.
- One-line definition of Microsoft Foundry: *production-ready hosted models with managed infrastructure, no fine-tuning required, OpenAI SDK compatible.*
- Show the end state on a slide: a deployed agent answering moderation requests. "By the end of this lab, you'll build this."

### Lab 1 — Discover Models (10 min)

- Open [ai.azure.com](https://ai.azure.com), navigate the **Model Catalog**.
- Talk through filters: provider, capability (chat, embeddings), modality, deployment options.
- Compare **gpt-5.4-mini**, **gpt-5.4**, and **Phi-4** — frame as "cost, latency, quality" trade-off.
- Show **quota** and **regional availability** — call out that quota is per region per model.
- Optional: paste a Zava-style review into the **Playground** and show a classification response.

**Common attendee question:** *"How do I know which model to choose?"* — Answer: start with the cheapest model that meets your quality bar, then measure. Lab 5 shows the comparison workflow.

### Lab 2 — Create and Configure a Foundry Project (10 min)

- Show what the `setup.ps1` / `setup.sh` script does at a high level before running:
  - AI Services account
  - Foundry project
  - Model deployment (gpt-5.4-mini)
  - Monitoring (App Insights / Log Analytics)
  - RBAC role assignments
  - Local `.env` file
- Run the script live **only if** you have time and a fast network. Otherwise, run it on a pre-staged subscription and walk through the output.
- Open `infra/main.bicep` and `azure.yaml` — explain why Infrastructure-as-Code matters (reproducibility, review, source control).
- Show the resulting resource group in the Azure portal — point out the named resources.

**Time saver:** Pre-provision a resource group on a side subscription so if the live `azd up` is slow, you can flip to it and keep moving.

### Lab 3 — First Inference (12 min)

- Open [`src/01_first_inference.py`](../src/01_first_inference.py).
- Walk through line by line:
  - `DefaultAzureCredential()` — explain the credential chain
  - `AIProjectClient(...)` — the project endpoint pattern
  - `project.inference.get_openai_client()` — call out *"this is just the OpenAI SDK"*
  - `client.chat.completions.create(...)` — same API everyone already knows
- Run it. Show the response, then point out `response.usage` (tokens) — set up the cost conversation.
- Bump `temperature` from 0.0 → 1.5 and re-run. Show how output changes. Land the point: *moderation = deterministic, creative writing = higher temp.*

### Lab 4 — Build the Moderation Application (20 min)

- Open [`src/02_comment_moderation.py`](../src/02_comment_moderation.py).
- Show the **structured JSON system prompt** — explain why structured output is the difference between a demo and a production app.
- Show the classification schema: `SAFE` / `NEEDS_REVIEW` / `UNSAFE` with `confidence` and `reason`.
- Walk through the **business logic layer**:
  - High-confidence `SAFE` → auto-approve
  - High-confidence `UNSAFE` → auto-block
  - Anything else → human review queue
- Run against [`src/sample_comments.json`](../src/sample_comments.json) in batch mode.
- Run an interactive review (let an attendee suggest one if you have time).
- Show [`src/tests/test_moderation.py`](../src/tests/test_moderation.py) — reinforce that *real apps have tests*.

**Don't skip:** the confidence threshold conversation. This is the most-cited takeaway from previous deliveries.

### Lab 6 — Deploy a Hosted Agent (15 min)

- Open the [`src/agent/`](../src/agent/) folder and walk through the three files:
  - `app.py` — the agent logic using Microsoft Agent Framework SDK
  - `Dockerfile` — standard Python container
  - `agent.yaml` — the manifest that tells Foundry what to host
- Run `azd up` (or `azd deploy` if already provisioned). While it runs:
  - Explain what `azd` is doing (build → push to ACR → create/update agent → wire RBAC).
  - Reinforce: *the developer didn't write any infra — `azd` did.*
- When deployment finishes, invoke the agent:
  - Via CLI: `azd ai agent invoke`
  - Via the Foundry **Playground** in the portal — show the live request/response
- Optional: tail logs from the agent to show observability.

**If `azd up` is slow:** keep the narrative going — talk about why managed agents matter (no Kubernetes, no scaling code, no patch management).

### Lab 7 — Wrap, takeaways, Q&A (5 min)

- Recap the journey in one breath: *catalog → project → first call → moderation pipeline → hosted agent.*
- Call out **Lab 5** as a self-paced extension — attendees compare gpt-5.4-mini vs gpt-5.4 at home, including the hybrid "cheap first, escalate when uncertain" pattern.
- Point to related Build 2026 sessions (have 2–3 specific session codes on a slide).
- Direct attendees to:
  - [Lab GitHub repo](https://github.com/microsoft/Build26-LAB520-get-started-with-models-in-microsoft-foundry-to-build-ai-apps)
  - [Microsoft Foundry docs](https://learn.microsoft.com/azure/ai-foundry/)
  - [Build 2026 next steps](https://aka.ms/build26-next-steps)
- Take questions in chat / Q&A — don't run over.

---

## 🧯 Troubleshooting cheat sheet (for proctors)

The vast majority of attendee issues fall into one of these buckets. Triage in this order:

| Symptom | Most likely cause | Fix |
|:--------|:------------------|:----|
| `az login` / `azd auth login` loops or fails | Wrong tenant or stale token | `az logout` then `az login --tenant <tenant-id>`; same for `azd auth logout` / `login` |
| `setup.ps1` fails on resource provider not registered | Subscription is missing `Microsoft.CognitiveServices` | `az provider register --namespace Microsoft.CognitiveServices` |
| Model deployment fails with quota error | No quota for **gpt-5.4-mini** in chosen region | Switch to a region with quota (see [armsetup.md](../setup/armsetup.md)) or request quota |
| `DefaultAzureCredential` fails in Python | Not signed in, or wrong tenant active | `az login`; verify `az account show` matches the project's subscription |
| `401`/`403` on first inference call | RBAC role assignment hasn't propagated yet | Wait 1–2 minutes; re-run. If still failing, confirm role assignment in the portal |
| `ModuleNotFoundError` | Virtual env not activated or `pip install -r requirements.txt` not run | Activate venv; reinstall |
| `azd up` fails on container build | Docker not running | Start Docker Desktop / lab container host |
| `azd up` is very slow | First-time ACR build | Expected; keep narrating |
| Agent invoke returns empty / weird response | Wrong deployment name in `.env` | Re-run setup script or manually align `MODEL_DEPLOYMENT_NAME` |
| Attendee can't find the lab | Sent to wrong tab | Direct to [docs/lab1-discover-models.md](../docs/lab1-discover-models.md) |

If you hit something **not** on this list, write it down — we want to add it. File an issue against the repo (see [AGENTS.md](../AGENTS.md) for the issue process).

---

## 🛠 Tips for proctors on the floor

- Stand at the back/side; scan for raised hands or stuck attendees (frozen screens, confused expressions).
- When helping: ask "what error are you seeing?" — read the error, then act. Don't drive their keyboard unless they ask.
- If multiple attendees hit the same problem, flag the lead presenter — they can address it once for the room.
- Don't get stuck on one attendee for more than 5 minutes. Get them past the blocker (even by sharing a working `.env`) so the rest of the room keeps moving.
- For quota / subscription issues that can't be fixed in-room, pair them with a neighbour or point them to the [self-paced setup](../setup/SETUP.md) so they can finish later.

---

## 🔁 Re-delivering this lab (community events, internal training)

You are welcome and encouraged to re-deliver this content. A few asks:

- **Keep the Zava narrative** — it ties this lab to the broader Microsoft demo storyline (Cora, Bruno, Serena).
- **Use the latest version** of the repo from GitHub. Lab steps and SDK calls evolve; pin yourself to `main`.
- **Don't commit secrets** to forks. Every demo subscription has its own `.env`. See [AGENTS.md](../AGENTS.md).
- **Cite the source** on your title slide: *Adapted from Microsoft Build 2026 LAB520*, with a link back to the repo.
- **Adapt the timing** as needed:
  - **30-min lightning version:** Intro + Lab 1 + Lab 3 + Lab 7 (skip provisioning, use a pre-built project)
  - **60-min meetup version:** Intro + Labs 1–4 + Lab 7
  - **Full 75-min Build version:** as documented above
  - **Half-day workshop:** all labs including Lab 5 (model comparison), with longer hands-on time per section

---

## 📚 Related resources

- [`LAB520-Train-the-Trainer.pdf`](LAB520-Train-the-Trainer.pdf) — full train-the-trainer deck (read first)
- [`../session-outline.md`](../session-outline.md) — official session outline with timing per block
- [`../techspec.md`](../techspec.md) — technical specification for the lab
- [`../setup/SETUP.md`](../setup/SETUP.md) — attendee setup guide
- [`../setup/armsetup.md`](../setup/armsetup.md) — ARM-based setup and region/quota notes
- [`../cleanup/CLEANUP.md`](../cleanup/CLEANUP.md) — resource cleanup instructions
- [`../AGENTS.md`](../AGENTS.md) — repo contribution and issue-filing guidelines

---

## ❓ Questions or feedback on delivery

If you spot a gap in this guide, or you want to share what worked / didn't work when you delivered this lab, please **open an issue** on the repo using the issue templates in [`.github/ISSUE_TEMPLATE/`](../.github/ISSUE_TEMPLATE/). Tag it with the `train-the-trainer` label (or request the label if it doesn't exist yet).

Good luck — and have fun delivering LAB520. 🚀
