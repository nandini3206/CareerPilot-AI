import re

def parse_job_description(job_text):
    """
    Parse a job description into structured information.
    """

    job = {
        "title": "",
        "skills": [],
        "requirements": "",
        "responsibilities": ""
    }

    return job