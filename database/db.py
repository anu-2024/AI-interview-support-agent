# database functions placeholder
"""
AI Interview Agent Pro
Database Operations
"""

import sqlite3
from pathlib import Path

DB_PATH = Path("interview_agent.db")


class DatabaseManager:
    def __init__(self):
        self.db_path = DB_PATH
        self.create_database()

    # -----------------------------
    # Database Connection
    # -----------------------------
    def get_connection(self):
        return sqlite3.connect(self.db_path)

    # -----------------------------
    # Create Database
    # -----------------------------
    def create_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            question TEXT,
            difficulty TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            question_id INTEGER,
            ai_answer TEXT,
            user_answer TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer_id INTEGER,
            semantic_score REAL,
            keyword_score REAL,
            final_score REAL,
            percentage REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer_id INTEGER,
            strengths TEXT,
            weaknesses TEXT,
            missing_keywords TEXT,
            suggestions TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            mode TEXT,
            total_questions INTEGER,
            average_score REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

    # -----------------------------
    # User Operations
    # -----------------------------
    def add_user(self, name, email):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users(name,email)
            VALUES (?,?)
            """,
            (name, email)
        )

        conn.commit()
        conn.close()

    def get_users(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        conn.close()
        return data

    # -----------------------------
    # Question Operations
    # -----------------------------
    def add_question(self, category, question, difficulty="Medium"):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO questions(category,question,difficulty)
            VALUES (?,?,?)
            """,
            (category, question, difficulty)
        )

        conn.commit()
        conn.close()

    def get_questions(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM questions")
        rows = cursor.fetchall()

        conn.close()
        return rows

    # -----------------------------
    # Answer Operations
    # -----------------------------
    def save_answer(
        self,
        user_id,
        question_id,
        ai_answer,
        user_answer
    ):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO answers(
                user_id,
                question_id,
                ai_answer,
                user_answer
            )
            VALUES (?,?,?,?)
            """,
            (
                user_id,
                question_id,
                ai_answer,
                user_answer
            )
        )

        answer_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return answer_id

    # -----------------------------
    # Score Operations
    # -----------------------------
    def save_score(
        self,
        answer_id,
        semantic_score,
        keyword_score,
        final_score,
        percentage
    ):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO scores(
                answer_id,
                semantic_score,
                keyword_score,
                final_score,
                percentage
            )
            VALUES (?,?,?,?,?)
            """,
            (
                answer_id,
                semantic_score,
                keyword_score,
                final_score,
                percentage
            )
        )

        conn.commit()
        conn.close()

    def get_scores(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT final_score
            FROM scores
            """
        )

        scores = cursor.fetchall()

        conn.close()

        return scores

    # -----------------------------
    # Feedback Operations
    # -----------------------------
    def save_feedback(
        self,
        answer_id,
        strengths,
        weaknesses,
        missing_keywords,
        suggestions
    ):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO feedback(
                answer_id,
                strengths,
                weaknesses,
                missing_keywords,
                suggestions
            )
            VALUES (?,?,?,?,?)
            """,
            (
                answer_id,
                strengths,
                weaknesses,
                missing_keywords,
                suggestions
            )
        )

        conn.commit()
        conn.close()

    # -----------------------------
    # Dashboard Stats
    # -----------------------------
    def get_dashboard_stats(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM interviews"
        )
        total_interviews = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT AVG(final_score)
            FROM scores
            """
        )
        avg_score = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT MAX(final_score)
            FROM scores
            """
        )
        highest_score = cursor.fetchone()[0]

        conn.close()

        return {
            "total_interviews": total_interviews,
            "average_score": round(avg_score, 2)
            if avg_score else 0,
            "highest_score": round(highest_score, 2)
            if highest_score else 0
        }


# Singleton Instance
db = DatabaseManager()
