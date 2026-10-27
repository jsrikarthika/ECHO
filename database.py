import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "echo.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                concept TEXT NOT NULL,
                selected_answer TEXT NOT NULL,
                is_correct INTEGER NOT NULL,
                attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_attempt(student_name, concept, selected_answer, is_correct):
    with get_connection() as connection:
        connection.execute("""
            INSERT INTO quiz_attempts
                (student_name, concept, selected_answer, is_correct)
            VALUES (?, ?, ?, ?)
        """, (
            student_name.strip(),
            concept,
            selected_answer,
            int(is_correct)
        ))


def get_student_history(student_name):
    with get_connection() as connection:
        return connection.execute("""
            SELECT concept, is_correct, attempted_at
            FROM quiz_attempts
            WHERE student_name = ?
            ORDER BY attempted_at DESC
        """, (student_name.strip(),)).fetchall()
