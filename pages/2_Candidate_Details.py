import streamlit as st
import os

from modules.parser import extract_text
from modules.ats_score import calculate_ats_score
from modules.resume_quality import calculate_resume_quality
from modules.overall_score import calculate_overall_score

st.set_page_config(
    page_title="Candidate Details",
    layout="wide"
)

# Check if a resume was selected
if "selected_resume" not in st.session_state:
    st.warning("No resume selected.")
    st.stop()

# Get selected resume
resume_name = st.session_state["selected_resume"]

# Get selected skills from Home page
selected_skills = st.session_state.get("selected_skills", [])

# Full path
file_path = os.path.join(
    "uploads",
    resume_name
)

# Extract resume text
resume_text = extract_text(file_path)

# Calculate scores
ats_score, matched_skills, missing_skills = calculate_ats_score(
    selected_skills,
    resume_text
)

quality_score = calculate_resume_quality(
    resume_text
)

overall_score = calculate_overall_score(
    ats_score,
    quality_score
)

# Title
st.title(f"📄 {resume_name}")

# Scores
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📊 ATS Score",
        f"{ats_score:.2f}%"
    )

with col2:
    st.metric(
        "📄 Resume Quality",
        f"{quality_score}%"
    )

with col3:
    st.metric(
        "⭐ Overall Score",
        f"{overall_score}%"
    )

# Skills
st.subheader("✅ Skills")

if matched_skills:
    st.write(matched_skills)
else:
    st.write("No matching skills found")

# Missing Skills
st.subheader("❌ Missing Skills")

if missing_skills:
    st.write(missing_skills)
else:
    st.write("No missing skills")

# Education
st.subheader("🎓 Education")

if "education" in resume_text.lower():
    st.success("Education section found")
else:
    st.error("Education section not found")

# Experience
st.subheader("💼 Experience")

if "experience" in resume_text.lower():
    st.success("Experience section found")
else:
    st.error("Experience section not found")

# Projects
st.subheader("🚀 Projects")

if "project" in resume_text.lower():
    st.success("Projects section found")
else:
    st.error("Projects section not found")

# Resume Content
st.subheader("📑 Resume Content")

st.text_area(
    "Resume",
    resume_text,
    height=400
)