
"""
Scoring Engine Tests
"""

import unittest

from evaluation.scorer import (
    scorer
)


class TestScoring(unittest.TestCase):

    def test_similarity_score(self):

        ai_answer = """
Python is a programming language.
"""

        user_answer = """
Python is a popular programming language.
"""

        result = scorer.evaluate(
            ai_answer,
            user_answer
        )

        self.assertGreater(
            result["final_score"],
            0
        )

    def test_percentage(self):

        ai_answer = """
Machine learning allows systems
to learn from data.
"""

        user_answer = """
Machine learning learns from data.
"""

        result = scorer.evaluate(
            ai_answer,
            user_answer
        )

        self.assertTrue(
            result["percentage"] >= 0
        )

    def test_keywords(self):

        ai_answer = """
Python uses functions,
classes and modules.
"""

        user_answer = """
Python uses classes.
"""

        result = scorer.evaluate(
            ai_answer,
            user_answer
        )

        self.assertIn(
            "functions",
            result["missing_keywords"]
        )

    def test_strengths(self):

        ai_answer = """
SQL is used to manage databases.
"""

        user_answer = """
SQL is used to manage databases.
"""

        result = scorer.evaluate(
            ai_answer,
            user_answer
        )

        self.assertTrue(
            len(result["strengths"]) >= 1
        )


if __name__ == "__main__":
    unittest.main()
