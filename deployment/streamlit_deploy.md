# Streamlit Cloud Deployment Guide

## Step 1: Create GitHub Repository

Go to GitHub and create a new repository:

Example:

ai-interview-agent-pro

---

## Step 2: Initialize Git

Open terminal inside project folder.

```bash
git init
```

---

## Step 3: Add Files

```bash
git add .
```

---

## Step 4: Commit Files

```bash
git commit -m "Initial Commit"
```

---

## Step 5: Create Main Branch

```bash
git branch -M main
```

---

## Step 6: Connect GitHub Repository

```bash
git remote add origin https://github.com/USERNAME/ai-interview-agent-pro.git
```

Replace USERNAME with your GitHub username.

---

## Step 7: Push Code

```bash
git push -u origin main
```

---

## Step 8: Login to Streamlit Cloud

Open:

https://share.streamlit.io

Login using GitHub.

---

## Step 9: Create New App

Click:

New App

Select:

- Repository
- Branch: main
- Main file path: app.py

---

## Step 10: Deploy

Click Deploy.

Deployment usually takes 2–5 minutes.

---

## Common Errors

### Missing Dependencies

Verify:

requirements.txt

contains all required packages.

---

### App Not Found

Verify:

app.py

exists in repository root.

---

### Database Error

SQLite database will be created automatically.

No manual action required.

---

## Final URL

Example:

https://ai-interview-agent-pro.streamlit.app
