-- SQLite schema placeholder
-- ==========================================
-- AI Interview Agent Pro Database Schema
-- ==========================================

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS feedback;
DROP TABLE IF EXISTS interviews;

-- ==========================================
-- USERS
-- ==========================================

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- QUESTIONS
-- ==========================================

CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    question TEXT NOT NULL,
    difficulty TEXT DEFAULT 'Medium',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- ANSWERS
-- ==========================================

CREATE TABLE answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    question_id INTEGER,
    ai_answer TEXT,
    user_answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(question_id) REFERENCES questions(id)
);

-- ==========================================
-- SCORES
-- ==========================================

CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    answer_id INTEGER,
    semantic_score REAL,
    keyword_score REAL,
    final_score REAL,
    percentage REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(answer_id) REFERENCES answers(id)
);

-- ==========================================
-- FEEDBACK
-- ==========================================

CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    answer_id INTEGER,
    strengths TEXT,
    weaknesses TEXT,
    missing_keywords TEXT,
    suggestions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(answer_id) REFERENCES answers(id)
);

-- ==========================================
-- INTERVIEWS
-- ==========================================

CREATE TABLE interviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    mode TEXT,
    total_questions INTEGER,
    average_score REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)
);
