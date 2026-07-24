"""
Interview Preparation Configuration
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

QUESTION_TYPES = [
    "Technical",
    "HR",
    "Coding"
]

DEFAULT_QUESTIONS_PER_CATEGORY = 5

DIFFICULTY_LEVELS = [
    "Easy",
    "Medium",
    "Hard"
]