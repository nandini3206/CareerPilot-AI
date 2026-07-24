"""
Audio Recorder for Voice Interview
"""

import sounddevice as sd
import soundfile as sf

from .config import (
    SAMPLE_RATE,
    CHANNELS,
    AUDIO_FILE
)


class AudioRecorder:

    def __init__(self):

        self.sample_rate = SAMPLE_RATE
        self.channels = CHANNELS

    def record(self, duration=10):
        """
        Record audio from microphone.
        """

        print(f"\n🎤 Recording for {duration} seconds...")
        print("Start speaking...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16"
        )

        sd.wait()

        sf.write(
            AUDIO_FILE,
            audio,
            self.sample_rate
        )

        print(f"\n✅ Audio saved as {AUDIO_FILE}")

        return AUDIO_FILE


def main():

    recorder = AudioRecorder()

    recorder.record(duration=10)


if __name__ == "__main__":
    main()