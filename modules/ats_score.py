def calculate_ats_score(selected_skills, resume_text):

    # Convert resume text to lowercase
    resume_text = resume_text.lower()

    matched_skills = []
    missing_skills = []

    # Check each required skill
    for skill in selected_skills:

        if skill.lower() in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    # Calculate ATS score
    if len(selected_skills) > 0:
        ats_score = (len(matched_skills) / len(selected_skills)) * 100
    else:
        ats_score = 0

    return ats_score, matched_skills, missing_skills