import streamlit as st
import pandas as pd
import os

from modules.shortlist import add_to_shortlist

st.set_page_config(
    page_title="Candidates",
    layout="wide"
)

st.title("📂 Candidates")

# Load scores file
df = pd.read_csv(
    "reports/candidate_scores.csv"
)

if len(df) == 0:

    st.info(
        "No resumes analyzed yet."
    )

else:

    # Search
    search_text = st.text_input(
        "🔍 Search Candidate",
        placeholder="Type candidate name..."
    )

    # Sort
    sort_order = st.selectbox(
        "🔀 Sort By Overall Score",
        [
            "Descending",
            "Ascending"
        ]
    )

    if sort_order == "Descending":

        df = df.sort_values(
            by="Overall Score",
            ascending=False
        )

    else:

        df = df.sort_values(
            by="Overall Score",
            ascending=True
        )

    # Candidate Cards
    for index, row in df.iterrows():

        resume_name = str(
            row["Resume"]
        )

        # Search Filter
        if search_text:

            if search_text.lower() not in resume_name.lower():
                continue

        with st.container(border=True):

            st.subheader(
                f"📄 {resume_name}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"⭐ Overall Score : {row['Overall Score']}"
                )

            with col2:

                st.write(
                    f"📊 ATS Score : {row['ATS Score']}"
                )

            btn1, btn2, btn3, btn4 = st.columns(4)

            # Open Profile
            with btn1:

                if st.button(
                    "Open Profile",
                    key=f"open_{resume_name}"
                ):

                    st.session_state[
                        "selected_resume"
                    ] = resume_name

                    st.switch_page(
                        "pages/2_Candidate_Details.py"
                    )

            # Download Resume
            with btn2:

                file_path = os.path.join(
                    "uploads",
                    resume_name
                )

                if os.path.exists(
                    file_path
                ):

                    with open(
                        file_path,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="Download",
                            data=file,
                            file_name=resume_name,
                            key=f"download_{resume_name}"
                        )

            # Shortlist
            with btn3:

                if st.button(
                    "Shortlist",
                    key=f"shortlist_{resume_name}"
                ):

                    add_to_shortlist(
                        resume_name,
                        row["ATS Score"],
                        row["Resume Quality"],
                        row["Overall Score"]
                    )

                    st.success(
                        f"{resume_name} added to shortlist."
                    )

            # Delete Resume
            with btn4:

                if st.button(
                    "Delete",
                    key=f"delete_{resume_name}"
                ):

                    file_path = os.path.join(
                        "uploads",
                        resume_name
                    )

                    if os.path.exists(
                        file_path
                    ):
                        os.remove(
                            file_path
                        )

                    df = df[
                        df["Resume"] != resume_name
                    ]

                    df.to_csv(
                        "reports/candidate_scores.csv",
                        index=False
                    )

                    st.success(
                        f"{resume_name} deleted successfully."
                    )

                    st.rerun()