# Hugging Face Spaces Deployment Guide

## Step 1: Create Hugging Face Account

Open:

https://huggingface.co

Create account.

---

## Step 2: Create New Space

Click:

Create New Space

Fill:

Name:
AI Interview Agent Pro

SDK:
Streamlit

Visibility:
Public

---

## Step 3: Upload Files

Upload:

```text
app.py
requirements.txt
runtime.txt
packages.txt

database/
models/
evaluation/
pages/
utils/
data/
```

---

## Step 4: Verify Runtime

runtime.txt

```text
python-3.11
```

---

## Step 5: Verify Dependencies

requirements.txt

contains all project dependencies.

---

## Step 6: Commit Changes

Commit uploaded files.

---

## Step 7: Automatic Build

Hugging Face will automatically:

- Install dependencies
- Build environment
- Start Streamlit application

---

## Build Time

Usually:

5–15 minutes

depending on model size.

---

## Recommended Models

For free deployment:

### TinyLlama

TinyLlama/TinyLlama-1.1B-Chat-v1.0

### Phi-3 Mini

microsoft/Phi-3-mini-4k-instruct

### Gemma

google/gemma-2b-it

---

## Large Models

Avoid:

- Mistral 7B
- Llama 3 8B

on free Spaces because of memory limits.

---

## Final Space URL

Example:

https://huggingface.co/spaces/USERNAME/ai-interview-agent-pro
