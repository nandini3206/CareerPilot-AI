"""
====================================================
CareerPilot AI V2
Role Prediction Explanation Engine
====================================================
"""

ROLE_DESCRIPTIONS = {

    "ACCOUNTANT":
        "Strong analytical and financial skills suitable for accounting and auditing roles.",

    "ADVOCATE":
        "Profile indicates knowledge of legal documentation, research and advocacy.",

    "AGRICULTURE":
        "Resume reflects agricultural practices, farming and related technologies.",

    "APPAREL":
        "Skills indicate experience in apparel, textile or fashion-related work.",

    "ARTS":
        "Creative profile with experience in arts, design or visual content.",

    "AUTOMOBILE":
        "Knowledge of automobile engineering, manufacturing or maintenance.",

    "AVIATION":
        "Profile matches aviation, aerospace or airline related domains.",

    "BANKING":
        "Suitable for banking, finance and financial operations.",

    "BPO":
        "Communication and customer support skills suitable for BPO roles.",

    "BUSINESS-DEVELOPMENT":
        "Profile indicates sales strategy, client acquisition and business growth.",

    "CHEF":
        "Experience and skills indicate culinary expertise and food preparation.",

    "CONSTRUCTION":
        "Knowledge related to civil, construction and infrastructure projects.",

    "CONSULTANT":
        "Strong analytical and consulting capabilities across business domains.",

    "DESIGNER":
        "Creative design profile with UI/UX, graphics or product design skills.",

    "DIGITAL-MEDIA":
        "Experience in digital marketing, social media and online branding.",

    "ENGINEERING":
        "Strong technical background with programming, software or engineering skills.",

    "FINANCE":
        "Suitable for financial analysis, investment and corporate finance roles.",

    "FITNESS":
        "Profile demonstrates health, wellness and fitness expertise.",

    "HEALTHCARE":
        "Medical or healthcare related experience and domain knowledge.",

    "HR":
        "Experience in recruitment, employee management and human resources.",

    "INFORMATION-TECHNOLOGY":
        "Excellent match for IT, software development and technology roles.",

    "PUBLIC-RELATIONS":
        "Communication and branding skills suitable for PR roles.",

    "SALES":
        "Strong sales, negotiation and customer relationship skills.",

    "TEACHER":
        "Experience in education, mentoring and academic instruction.",
}


def explain_prediction(role):

    description = ROLE_DESCRIPTIONS.get(
        role,
        "No description available."
    )

    return {
        "predicted_role": role,
        "description": description,
    }


if __name__ == "__main__":

    result = explain_prediction("ENGINEERING")

    print(result)