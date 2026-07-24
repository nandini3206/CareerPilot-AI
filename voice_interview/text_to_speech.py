"""
Text-to-Speech using pyttsx3
"""

import pyttsx3


class TextToSpeech:

    def __init__(self):

        self.rate = 170
        self.volume = 1.0

    def speak(self, text):

        print(f"\n🔊 AI: {text}\n")

        # Create a fresh engine every time
        engine = pyttsx3.init()

        engine.setProperty("rate", self.rate)
        engine.setProperty("volume", self.volume)

        engine.say(text)
        engine.runAndWait()
        engine.stop()


def main():

    tts = TextToSpeech()

    tts.speak("Tell me about yourself.")
    tts.speak("Explain overfitting.")