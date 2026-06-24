# scoring placeholder
"""
Hybrid Scoring Engine

70% Semantic Similarity
30% Keyword Coverage
"""

from evaluation.semantic_similarity import (
    semantic_similarity
)

from evaluation.keyword_match import (
    keyword_matcher
)


class InterviewScorer:

    def __init__(self):
        pass

    def evaluate(
        self,
        ai_answer,
        user_answer
    ):

        semantic_score = (
            semantic_similarity.calculate_similarity(
                ai_answer,
                user_answer
            )
        )

        keyword_result = (
            keyword_matcher.keyword_coverage(
                ai_answer,
                user_answer
            )
        )

        keyword_score = (
            keyword_result["coverage"]
        )

        final_score = (
            (semantic_score * 0.7)
            +
            (keyword_score * 0.3)
        )

        score_out_of_ten = round(
            final_score * 10,
            2
        )

        percentage = round(
            final_score * 100,
            2
        )

        strengths = []

        weaknesses = []

        if semantic_score >= 0.8:
            strengths.append(
                "Good conceptual understanding"
            )
        else:
            weaknesses.append(
                "Concepts need improvement"
            )

        if keyword_score >= 0.7:
            strengths.append(
                "Strong keyword coverage"
            )
        else:
            weaknesses.append(
                "Important concepts missing"
            )

        suggestions = []

        if len(
            keyword_result["missing"]
        ) > 0:

            suggestions.append(
                "Include missing concepts in your answer"
            )

        if percentage < 60:

            suggestions.append(
                "Provide more detailed explanation"
            )

        return {

            "semantic_score":
                round(
                    semantic_score,
                    4
                ),

            "keyword_score":
                round(
                    keyword_score,
                    4
                ),

            "final_score":
                score_out_of_ten,

            "percentage":
                percentage,

            "strengths":
                strengths,

            "weaknesses":
                weaknesses,

            "missing_keywords":
                keyword_result[
                    "missing"
                ],

            "matched_keywords":
                keyword_result[
                    "matched"
                ],

            "suggestions":
                suggestions
        }


scorer = InterviewScorer()
