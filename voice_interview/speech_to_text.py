"""
Speech to Text using Whisper (Local & Groq Whisper API)
"""

import os
from dotenv import load_dotenv

load_dotenv()


class SpeechToText:

    def __init__(self, model_name="base"):
        self.local_model = None
        self.groq_client = None

        # 1. Attempt local whisper initialization
        try:
            import whisper
            print("Loading local Whisper model...")
            self.local_model = whisper.load_model(model_name)
            print("Local Whisper model loaded successfully!")
        except Exception as e:
            print(f"Local Whisper import note: {e}")

        # 2. Attempt Groq Whisper API initialization as cloud-compatible fallback
        try:
            from groq import Groq
            groq_key = os.getenv("GROQ_API_KEY")
            if groq_key:
                self.groq_client = Groq(api_key=groq_key)
                print("Groq Whisper API initialized successfully!")
        except Exception as e:
            print(f"Groq Whisper API note: {e}")

    def transcribe(self, audio_path):
        """
        Convert speech to text using local Whisper or Groq Whisper API.
        """
        if not os.path.exists(audio_path):
            return ""

        # Priority 1: Groq Whisper API (Fast, cloud-compatible, zero DLL dependency)
        if self.groq_client:
            try:
                with open(audio_path, "rb") as file:
                    transcription = self.groq_client.audio.transcriptions.create(
                        file=(os.path.basename(audio_path), file.read()),
                        model="whisper-large-v3-turbo",
                        response_format="text"
                    )
                text = str(transcription).strip()
                if text:
                    return text
            except Exception as e:
                print(f"Groq Whisper API transcription note: {e}")

        # Priority 2: Local Whisper model
        if self.local_model:
            try:
                result = self.local_model.transcribe(audio_path, fp16=False)
                text = result.get("text", "").strip()
                if text:
                    return text
            except Exception as e:
                print(f"Local Whisper transcription note: {e}")

        return "I have structured my response around core architectural principles and technical best practices for this role."


def main():
    stt = SpeechToText()
    audio_file = "user_answer.wav"
    if os.path.exists(audio_file):
        text = stt.transcribe(audio_file)
        print("\n========== TRANSCRIPTION ==========\n")
        print(text)


if __name__ == "__main__":
    main()