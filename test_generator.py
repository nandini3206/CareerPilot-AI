from learning_roadmap.roadmap_generator import LearningRoadmapGenerator

generator = LearningRoadmapGenerator()

skills = [
    "Python",
    "SQL",
    "Pandas"
]

missing = generator.find_missing_skills(
    "Machine Learning Engineer",
    skills
)

print("Missing Skills:")
print(missing)

roadmap = generator.divide_into_weeks(missing)

print("\nRoadmap:")
print(roadmap)