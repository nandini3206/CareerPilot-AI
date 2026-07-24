# Learning Roadmap Module

## Overview

The Learning Roadmap module generates a personalized learning plan based on a user's predicted career role and existing skills.

It identifies missing skills, organizes them into a weekly roadmap, and recommends practical projects to help users prepare for their target role.

---

## Features

- Personalized learning roadmap
- Skill gap analysis
- Weekly learning plan
- Project recommendations
- Easily extensible knowledge base

---

## Project Structure

learning_roadmap/

- config.py
- knowledge_base.py
- roadmap_generator.py
- inference.py

---

## Workflow

Resume Skills
        │
        ▼
Role Prediction
        │
        ▼
Learning Roadmap
        │
        ▼
Missing Skills
        │
        ▼
Weekly Learning Plan
        │
        ▼
Recommended Projects

---

## Example Output

Target Role:
Machine Learning Engineer

Missing Skills

- Statistics
- TensorFlow
- Docker
- AWS

Weekly Plan

Week 1
- Statistics

Week 2
- TensorFlow

Week 3
- Docker

Week 4
- AWS

Projects

- House Price Prediction
- Resume Parser
- Stock Market Prediction

---

## Future Improvements

- Course recommendations
- YouTube learning resources
- Certification suggestions
- Dynamic roadmap generation using LLMs
- Progress tracking