"""
Speech to Text using Whisper
"""

import whisper


class SpeechToText:

    def __init__(self, model_name="base"):

        print("Loading Whisper model...")

        self.model = whisper.load_model(model_name)

        print("Whisper model loaded successfully!")

    def transcribe(self, audio_path):
        """
        Convert speech to text.
        """

        result = self.model.transcribe(
            audio_path,
            fp16=False
        )

        text = result["text"].strip()

        if not text:
            print("\n⚠ No speech detected.")

        return text


def main():

    stt = SpeechToText()

    audio_file = "user_answer.wav"

    text = stt.transcribe(audio_file)

    print("\n========== TRANSCRIPTION ==========\n")

    print(text)


if __name__ == "__main__":
    main()