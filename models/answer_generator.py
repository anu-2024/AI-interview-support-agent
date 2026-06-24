# answer generator placeholder
"""
Answer Generation Module
"""

from models.llm_loader import llm_loader


class AnswerGenerator:

    def __init__(self):
        pass

    def generate_answer(
        self,
        question,
        level="expert"
    ):

        prompt = f"""
You are an interview expert.

Question:
{question}

Generate a {level} level answer.

Answer:
"""

        generator = llm_loader.get_generator()

        result = generator(
            prompt,
            max_new_tokens=250
        )

        generated_text = result[0]["generated_text"]

        answer = generated_text.replace(
            prompt,
            ""
        ).strip()

        return answer

    def generate_all_levels(
        self,
        question
    ):

        beginner = self.generate_answer(
            question,
            "beginner"
        )

        intermediate = self.generate_answer(
            question,
            "intermediate"
        )

        expert = self.generate_answer(
            question,
            "expert"
        )

        return {
            "beginner": beginner,
            "intermediate": intermediate,
            "expert": expert
        }


answer_generator = AnswerGenerator()
