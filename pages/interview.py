# interview page placeholder
import streamlit as st

from models.llm_loader import llm_loader
from models.answer_generator import (
    answer_generator
)

from evaluation.scorer import scorer


SUPPORTED_MODELS = [
    "TinyLlama",
    "Phi-3 Mini",
    "Gemma"
]


def show_interview():

    st.title("💼 Interview Simulator")

    model_choice = st.selectbox(
        "Select Model",
        SUPPORTED_MODELS
    )

    question = st.text_area(
        "Enter Interview Question"
    )

    if st.button("Load Model"):

        with st.spinner(
            "Loading Model..."
        ):

            llm_loader.load_model(
                model_choice
            )

        st.success(
            "Model Loaded Successfully"
        )

    if st.button(
        "Generate AI Answers"
    ):

        if not question:

            st.warning(
                "Enter Question"
            )

        else:

            answers = (
                answer_generator
                .generate_all_levels(
                    question
                )
            )

            st.session_state[
                "ai_answers"
            ] = answers

    if "ai_answers" in st.session_state:

        st.subheader(
            "Beginner Answer"
        )

        st.write(
            st.session_state[
                "ai_answers"
            ]["beginner"]
        )

        st.subheader(
            "Intermediate Answer"
        )

        st.write(
            st.session_state[
                "ai_answers"
            ]["intermediate"]
        )

        st.subheader(
            "Expert Answer"
        )

        st.write(
            st.session_state[
                "ai_answers"
            ]["expert"]
        )

    user_answer = st.text_area(
        "Enter Your Answer"
    )

    if st.button(
        "Evaluate Answer"
    ):

        if (
            "ai_answers"
            not in st.session_state
        ):

            st.warning(
                "Generate AI Answer First"
            )

        else:

            result = scorer.evaluate(
                st.session_state[
                    "ai_answers"
                ]["expert"],
                user_answer
            )

            st.subheader(
                "Evaluation Report"
            )

            st.metric(
                "Score",
                result[
                    "final_score"
                ]
            )

            st.metric(
                "Percentage",
                f"{result['percentage']}%"
            )

            st.write(
                "### Strengths"
            )

            st.write(
                result["strengths"]
            )

            st.write(
                "### Weaknesses"
            )

            st.write(
                result["weaknesses"]
            )

            st.write(
                "### Missing Keywords"
            )

            st.write(
                result[
                    "missing_keywords"
                ]
            )

            st.write(
                "### Suggestions"
            )

            st.write(
                result[
                    "suggestions"
                ]
            )
