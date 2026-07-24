# Interview Preparation Module

## Overview

The Interview Preparation module generates interview questions based on the user's predicted job role.

It provides three categories of interview preparation:

- Technical Questions
- HR Questions
- Coding Questions

---

## Features

- Role-specific interview questions
- Technical preparation
- HR interview preparation
- Coding interview practice
- Easy to extend with additional roles

---

## Project Structure

interview_preparation/

- config.py
- knowledge_base.py
- question_generator.py
- inference.py

---

## Workflow

Resume
        │
        ▼
Role Prediction
        │
        ▼
Interview Preparation
        │
        ├── Technical Questions
        ├── HR Questions
        └── Coding Questions

---

## Future Improvements

- AI-generated personalized questions
- Difficulty levels
- Model answers
- Mock interview mode
- Interview scoring
- Voice interview integration