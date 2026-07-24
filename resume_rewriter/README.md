# Resume Rewriter Module

## Overview

The Resume Rewriter uses Groq LLMs to rewrite resumes into a more professional, ATS-friendly format while preserving the original meaning.

## Features

- ATS-friendly rewriting
- Professional language enhancement
- Strong action verbs
- Grammar improvement
- Better project descriptions
- Improved resume summary

## Project Structure

resume_rewriter/

- config.py
- prompt_templates.py
- rewriter.py
- inference.py

## Workflow

Resume Text
      │
      ▼
Prompt Template
      │
      ▼
Groq LLM
      │
      ▼
Rewritten Resume

## Future Improvements

- Role-specific rewriting
- Bullet point optimization
- Resume scoring after rewrite
- Multiple writing styles
- Section-wise rewriting