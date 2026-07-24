# 🎤 CareerPilot AI – Voice Interview Module

An AI-powered mock interview system that conducts technical interviews using voice interaction. The module generates interview questions, records candidate responses, converts speech to text, evaluates answers using LLMs, and provides detailed performance feedback.

---

## 🚀 Features

- 🎯 AI-generated interview questions based on job role
- 🔊 Text-to-Speech (TTS) for asking questions
- 🎤 Voice recording from microphone
- 📝 Speech-to-Text using OpenAI Whisper
- 🤖 AI answer evaluation using Groq LLM
- 📊 Detailed interview report
- ⭐ Overall interview score
- 📈 Technical Accuracy Score
- 💬 Communication Score
- 💪 Confidence Score
- ✅ Completeness Score
- 📌 Strengths & Improvements
- ❓ Follow-up questions for learning

---

## 🛠 Tech Stack

- Python
- Whisper
- Groq API
- pyttsx3
- SoundDevice
- SoundFile
- NumPy

---

## 📂 Project Structure

```
voice_interview/
│
├── config.py
├── audio_recorder.py
├── speech_to_text.py
├── text_to_speech.py
├── answer_evaluator.py
├── interview_manager.py
├── question_engine.py
├── inference.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/CareerPilot-AI.git

cd CareerPilot-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run

```bash
python -m voice_interview.inference
```

---

## 🎤 Workflow

```
Select Role
      │
      ▼
Generate Questions
      │
      ▼
AI Speaks Question
      │
      ▼
User Records Answer
      │
      ▼
Speech → Text
      │
      ▼
LLM Evaluation
      │
      ▼
Store Results
      │
      ▼
Next Question
      │
      ▼
Final Interview Report
```

---

## 📊 Sample Report

```
Overall Score : 87

Technical Accuracy : 90
Communication : 84
Confidence : 88
Completeness : 86

Strengths
✔ Good explanation
✔ Strong technical understanding

Improvements
• Add practical examples
• Improve answer structure
```

---

## 🔮 Future Enhancements

- Streamlit Integration
- Interview History
- Performance Dashboard
- PDF Report Export
- Adaptive Question Difficulty
- Multi-language Interviews

---

## 👩‍💻 Developed By

**Nandini Bhatt**
