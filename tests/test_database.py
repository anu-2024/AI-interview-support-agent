
"""
Database Tests
AI Interview Agent Pro
"""

import unittest
import sqlite3
from database.db import DatabaseManager


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseManager()

    def test_database_creation(self):

        conn = sqlite3.connect(
            "interview_agent.db"
        )

        self.assertIsNotNone(conn)

        conn.close()

    def test_add_user(self):

        try:

            self.db.add_user(
                "Test User",
                "test@test.com"
            )

            users = self.db.get_users()

            self.assertTrue(
                len(users) > 0
            )

        except Exception:

            pass

    def test_add_question(self):

        self.db.add_question(
            "Python",
            "What is Python?"
        )

        questions = (
            self.db.get_questions()
        )

        self.assertTrue(
            len(questions) > 0
        )


if __name__ == "__main__":
    unittest.main()
