"""
Voice Interview Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ===========================
# Groq
# ===========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.3-70b-versatile"

# ===========================
# Audio
# ===========================

SAMPLE_RATE = 16000

CHANNELS = 1

AUDIO_FILE = "user_answer.wav"

# ===========================
# Interview
# ===========================

TOTAL_QUESTIONS = 5
