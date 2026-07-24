"""
Resume Rewriter Inference
"""

from .rewriter import ResumeRewriter


class ResumeRewriterInference:
    """
    Inference class for AI Resume Rewriter.
    """

    def __init__(self):
        self.rewriter = ResumeRewriter()

    def predict(self, resume_text):
        """
        Rewrite the resume.
        """
        return self.rewriter.rewrite_resume(resume_text)


def main():

    sample_resume = """
    Name: John Doe

    Skills:
    Python
    SQL
    Machine Learning

    Projects:
    Built a stock prediction application.

    Experience:
    Worked on machine learning projects.
    """

    inference = ResumeRewriterInference()

    rewritten = inference.predict(sample_resume)

    print("\n========== AI REWRITTEN RESUME ==========\n")
    print(rewritten)


if __name__ == "__main__":
    main()