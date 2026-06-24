"""
Helper Functions
"""

import pandas as pd
import os


def load_csv(file_path):
    """
    Load CSV safely
    """

    try:
        return pd.read_csv(file_path)

    except Exception as e:
        print(
            f"Error loading CSV: {e}"
        )
        return pd.DataFrame()


def format_score(score):
    """
    Format score
    """

    return f"{round(score, 2)}/10"


def percentage_color(score):

    if score >= 80:
        return "green"

    elif score >= 60:
        return "orange"

    return "red"


def safe_text(text):

    if text is None:
        return ""

    return str(text)


def get_average_score(scores):

    if len(scores) == 0:
        return 0

    return round(
        sum(scores) / len(scores),
        2
    )


def get_highest_score(scores):

    if len(scores) == 0:
        return 0

    return max(scores)


def file_exists(path):

    return os.path.exists(path)


def create_directory(path):

    os.makedirs(
        path,
        exist_ok=True
    )


def load_question_bank():

    datasets = {}

    files = {
        "Technical":
            "data/technical_questions.csv",

        "HR":
            "data/hr_questions.csv",

        "Behavioral":
            "data/behavioral_questions.csv",

        "Viva":
            "data/viva_questions.csv"
    }

    for key, value in files.items():

        if os.path.exists(value):

            datasets[key] = pd.read_csv(
                value
            )

    return datasets


def get_random_question(df):

    if len(df) == 0:
        return None

    return (
        df.sample(1)
        .iloc[0]["question"]
    )


def score_category(score):

    if score >= 8:
        return "Excellent"

    elif score >= 6:
        return "Good"

    elif score >= 4:
        return "Average"

    return "Needs Improvement"
