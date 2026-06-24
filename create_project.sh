#!/bin/bash

echo "Creating AI Interview Agent Pro..."

mkdir -p ai-interview-agent-pro

cd ai-interview-agent-pro

mkdir -p database
mkdir -p models
mkdir -p evaluation
mkdir -p pages
mkdir -p utils
mkdir -p deployment
mkdir -p tests
mkdir -p data
mkdir -p assets

touch app.py
touch requirements.txt
touch runtime.txt
touch packages.txt
touch README.md
touch .gitignore

touch database/schema.sql
touch database/db.py

touch models/llm_loader.py
touch models/answer_generator.py

touch evaluation/semantic_similarity.py
touch evaluation/keyword_match.py
touch evaluation/scorer.py

touch utils/prompts.py
touch utils/helpers.py

touch pages/home.py
touch pages/interview.py
touch pages/dashboard.py
touch pages/history.py

touch data/technical_questions.csv
touch data/hr_questions.csv
touch data/behavioral_questions.csv
touch data/viva_questions.csv

touch deployment/streamlit_deploy.md
touch deployment/huggingface_deploy.md

touch tests/test_database.py
touch tests/test_scoring.py

echo "Project structure created successfully."
