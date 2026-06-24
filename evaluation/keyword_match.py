# keyword matching placeholder
"""
Keyword Matching Module
"""

import re

STOP_WORDS = {
    "the",
    "a",
    "an",
    "is",
    "are",
    "was",
    "were",
    "and",
    "or",
    "to",
    "for",
    "of",
    "in",
    "on",
    "with",
    "by",
    "that",
    "this",
    "it",
    "as"
}


class KeywordMatcher:

    def __init__(self):
        pass

    def extract_keywords(
        self,
        text
    ):
        text = text.lower()

        words = re.findall(
            r"\b[a-zA-Z]{3,}\b",
            text
        )

        keywords = []

        for word in words:
            if word not in STOP_WORDS:
                keywords.append(word)

        return list(set(keywords))

    def keyword_coverage(
        self,
        reference_answer,
        user_answer
    ):
        reference_keywords = self.extract_keywords(
            reference_answer
        )

        user_keywords = self.extract_keywords(
            user_answer
        )

        matched = []

        missing = []

        for keyword in reference_keywords:

            if keyword in user_keywords:
                matched.append(keyword)
            else:
                missing.append(keyword)

        if len(reference_keywords) == 0:
            coverage = 0
        else:
            coverage = len(matched) / len(
                reference_keywords
            )

        return {
            "coverage": round(coverage, 4),
            "matched": matched,
            "missing": missing
        }


keyword_matcher = KeywordMatcher()
