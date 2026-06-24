# AI Interview Agent Pro

## Overview

AI Interview Agent Pro is an AI-powered interview preparation platform that helps students and professionals prepare for:

- Technical Interviews
- HR Interviews
- Behavioral Interviews
- MCA Viva Examinations

The system uses open-source Large Language Models (LLMs) and Natural Language Processing techniques to:

- Generate ideal answers
- Evaluate user responses
- Score interview performance
- Identify missing concepts
- Suggest improvements
- Track interview history

---

## Features

### AI Answer Generation

Supports:

- TinyLlama
- Phi-3 Mini
- Gemma
- Mistral
- Llama 3

Generates:

- Beginner Answer
- Intermediate Answer
- Expert Answer

---

### Interview Evaluation

Evaluates:

- Technical Accuracy
- Concept Coverage
- Communication Quality
- Completeness

Provides:

- Score out of 10
- Percentage
- Missing Keywords
- Strengths
- Weaknesses
- Improvement Suggestions

---

### Dashboard

Displays:

- Total Interviews
- Average Score
- Highest Score
- Progress Tracking
- Topic Performance

---

### Database

SQLite Database

Tables:

- users
- questions
- answers
- scores
- feedback
- interviews

---

## Project Structure

```text
ai-interview-agent-pro/

├── app.py
├── requirements.txt
├── runtime.txt
├── packages.txt
├── README.md

├── database/
│   ├── schema.sql
│   └── db.py

├── models/
│   ├── llm_loader.py
│   └── answer_generator.py

├── evaluation/
│   ├── semantic_similarity.py
│   ├── keyword_match.py
│   └── scorer.py

├── pages/
│   ├── home.py
│   ├── interview.py
│   ├── dashboard.py
│   └── history.py

├── utils/
│   ├── prompts.py
│   └── helpers.py

├── data/
│   ├── technical_questions.csv
│   ├── hr_questions.csv
│   ├── behavioral_questions.csv
│   └── viva_questions.csv

├── deployment/
│   ├── streamlit_deploy.md
│   └── huggingface_deploy.md

└── tests/
    ├── test_database.py
    └── test_scoring.py
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Application:

```text
http://localhost:8501
```

---

## GitHub Deployment

```bash
git init

git add .

git commit -m "Initial Commit"

git branch -M main

git remote add origin YOUR_REPOSITORY_URL

git push -u origin main
```

---

## Streamlit Cloud

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Select repository
4. Choose app.py
5. Deploy

---

## Hugging Face Spaces

1. Create Space
2. Select Streamlit SDK
3. Upload repository
4. Deploy

---

## Author

MCA Final Year Project

AI Interview Agent Pro
