import streamlit as st
import pandas as pd
import os

from modules.parser import extract_text
from modules.ats_score import calculate_ats_score
from modules.resume_quality import calculate_resume_quality
from modules.overall_score import calculate_overall_score
from modules.charts import create_pie_chart
from modules.save_scores import save_candidate_score

# Page settings
st.set_page_config(
    page_title="Smart Resume Analyzer",
    layout="wide"
)

# Title
st.title("📄 Smart Resume Analyzer")

# Load skills
skills_df = pd.read_csv("skills.csv")
skills_list = skills_df["Skill"].tolist()

# Skill selection
selected_skills = st.multiselect(
    "🎯 Select Required Skills",
    skills_list
)

# Save selected skills for other pages
st.session_state["selected_skills"] = selected_skills

# Resume upload
uploaded_file = st.file_uploader(
    "📂 Upload Resume",
    type=["pdf", "docx"]
)

# Process uploaded file
if uploaded_file is not None:

    # Create uploads folder
    os.makedirs("uploads", exist_ok=True)

    # Save uploaded file
    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Resume uploaded and saved successfully!")

    # Extract text
    resume_text = extract_text(file_path)

    # Show extracted text
    st.subheader("📑 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

    if selected_skills:

        # ATS Score
        ats_score, matched_skills, missing_skills = calculate_ats_score(
            selected_skills,
            resume_text
        )

        # Resume Quality Score
        quality_score = calculate_resume_quality(
            resume_text
        )

        # Overall Score
        overall_score = calculate_overall_score(
            ats_score,
            quality_score
        )

        # Save candidate scores
        save_candidate_score(
            uploaded_file.name,
            ats_score,
            quality_score,
            overall_score
        )

        # Score cards
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📊 ATS Score",
                f"{ats_score:.2f}%"
            )
            st.progress(int(ats_score))

        with col2:
            st.metric(
                "📄 Resume Quality",
                f"{quality_score}%"
            )
            st.progress(quality_score)

        with col3:
            st.metric(
                "⭐ Overall Score",
                f"{overall_score}%"
            )
            st.progress(int(overall_score))

        # Matched Skills
        st.subheader("✅ Matched Skills")

        if matched_skills:
            st.write(matched_skills)
        else:
            st.write("No matching skills found.")

        # Missing Skills
        st.subheader("❌ Missing Skills")

        if missing_skills:
            st.write(missing_skills)
        else:
            st.write("No missing skills.")

        # Pie Chart
        st.subheader("📈 Skill Match Analysis")

        fig = create_pie_chart(
            matched_skills,
            missing_skills
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# Show selected skills
if selected_skills:
    st.subheader("🎯 Required Skills")
    st.write(selected_skills)