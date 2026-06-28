import fitz

def extract_text(pdf_path):
    """
    Extract all text from a PDF resume.
    """

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text 

def extract_sections(text):

    lines = text.split("\n")

    sections = {
        "summary": "",
        "education": "",
        "skills": "",
        "projects": "",
        "experience": ""
    }

    current_section = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.upper() == "SUMMARY":
            current_section = "summary"

        elif line.upper() == "EDUCATION":
            current_section = "education"

        elif line.upper() == "SKILLS":
            current_section = "skills"

        elif line.upper() == "PROJECTS":
            current_section = "projects"

        elif line.upper() == "EXPERIENCE":
            current_section = "experience"

        elif current_section:
            sections[current_section] += line + "\n"
    return sections