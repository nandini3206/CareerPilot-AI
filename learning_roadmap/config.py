"""
Learning Roadmap Configuration
"""

from pathlib import Path

# ===========================
# Base Directory
# ===========================

BASE_DIR = Path(__file__).resolve().parent

# ===========================
# Roadmap Settings
# ===========================

DEFAULT_WEEKS = 8

DEFAULT_PROJECTS = 3

DEFAULT_RESOURCES = 3

# ===========================
# Difficulty
# ===========================

LEVELS = [
    "Beginner",
    "Intermediate",
    "Advanced"
]