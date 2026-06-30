def load_skills():
    """
    Load skills from skills.txt
    """

    with open("data/skills.txt", "r") as file:
        skills = file.read().splitlines()

    return skills


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    skills_database = load_skills()

    found_skills = []

    text = text.lower()

    for skill in skills_database:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills