"""
Voice Interview Inference Pipeline
"""

import json

from .question_engine import VoiceQuestionEngine
from .interview_manager import InterviewManager
from .audio_recorder import AudioRecorder
from .speech_to_text import SpeechToText
from .text_to_speech import TextToSpeech
from .answer_evaluator import AnswerEvaluator
RECORDING_DURATION = 10


class VoiceInterviewPipeline:

    def __init__(self):

        self.question_engine = VoiceQuestionEngine()

        self.manager = InterviewManager()

        self.recorder = AudioRecorder()

        self.stt = SpeechToText()

        self.tts = TextToSpeech()

        self.evaluator = AnswerEvaluator()

    def run(
        self,
        role="Machine Learning Engineer"
    ):

        print("\n" + "=" * 60)
        print("🎤 CareerPilot AI Voice Interview")
        print("=" * 60)

        # ----------------------------
        # Generate Questions
        # ----------------------------

        self.question_engine.start_interview(
            role=role,
            total_questions=5
        )

        questions = self.question_engine.questions

        self.manager.start(
            role,
            questions
        )

        # ----------------------------
        # Interview Loop
        # ----------------------------

        while self.manager.has_next_question():

            question = self.manager.get_next_question()

            print("\n" + "=" * 60)
            print(
                f"Question {self.manager.current_question}/{len(questions)}"
            )
            print("=" * 60)

            print("\n", question)

            # Speak Question
            ("\n========== SPEAKING ==========")
            print(question)
            print("==============================")
 
            self.tts.speak(question)

            print("Speech finished.")

            input(
                "\nPress ENTER when you are ready to answer..."
            )

            # Record
            audio_path = self.recorder.record(
                RECORDING_DURATION
            )

            # Transcribe
            answer = self.stt.transcribe(audio_path)

            print("\nYour Answer:\n")

            print(answer)

            # Evaluate
            evaluation = self.evaluator.evaluate(
                role=role,
                question=question,
                answer=answer
            )

            # Store
            self.manager.save_answer(
                question,
                answer,
                evaluation
            )

            # Next Question Voice
            if self.manager.has_next_question():

                print("Transition speech")

                self.tts.speak(
                    "Thank you. Here is your next question."
                )

                print("Transition finished")

        # ----------------------------
        # Final Report
        # ----------------------------

        report = self.manager.generate_report()

        print("\n" + "=" * 60)
        print("🎉 INTERVIEW COMPLETED")
        print("=" * 60)

        print()

        print(f"Overall Score : {report['overall_score']}/100")
        print()

        print(f"Technical Accuracy : {report['technical_accuracy']}")
        print(f"Communication      : {report['communication']}")
        print(f"Confidence         : {report['confidence']}")
        print(f"Completeness       : {report['completeness']}")

        print("\n==============================")
        print("Strengths")
        print("==============================")

        for item in report["strengths"]:
            print("✔", item)

        print("\n==============================")
        print("Areas to Improve")
        print("==============================")

        for item in report["improvements"]:
            print("•", item)

        print("\n==============================")
        print("Question-wise Feedback")
        print("==============================")

        for i, evaluation in enumerate(report["evaluations"], start=1):

            print("\n--------------------------------")

            print(f"Question {i}")

            print(
                "Overall Score :",
                evaluation["overall_score"]
            )

            print()

            print("Better Answer:")

            print(
                evaluation.get(
                    "better_answer",
                    ""
                )
            )

            print()

            print(
                "Follow-up Question:"
            )

            print(
                evaluation.get(
                    "follow_up_question",
                    ""
                )
            )

        print("\n" + "=" * 60)

        self.tts.speak(
            "Congratulations. Your interview has been completed."
        )

        return report


def main():

    pipeline = VoiceInterviewPipeline()

    report = pipeline.run(
        role="Machine Learning Engineer"
    )

    print("\n")

    print(json.dumps(report, indent=4))


if __name__ == "__main__":
    main()