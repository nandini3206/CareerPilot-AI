"""
Resume Rewriter Integration
"""

from resume_rewriter.inference import ResumeRewriterInference


class ResumeRewriterIntegration:
    """
    Integration layer for Resume Rewriter.
    """

    def __init__(self):
        self.model = ResumeRewriterInference()

    def rewrite_resume(self, resume_text: str) -> str:
        """
        Rewrite resume using backend inference.
        """

        if not resume_text:
            return "Resume text not found."

        return self.model.predict(resume_text)