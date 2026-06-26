import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Shortlisted Candidates",
    layout="wide"
)

st.title("⭐ Shortlisted Candidates")

df = pd.read_csv(
    "reports/shortlisted_candidates.csv"
)

if len(df) == 0:

    st.info(
        "No shortlisted candidates."
    )

else:

    for index, row in df.iterrows():

        with st.container(border=True):

            st.subheader(
                f"📄 {row['Resume']}"
            )

            st.write(
                f"⭐ Overall Score : {row['Overall Score']}"
            )

            st.write(
                f"📊 ATS Score : {row['ATS Score']}"
            )

            col1, col2 = st.columns(2)

            # Open Profile
            with col1:

                if st.button(
                    "Open Profile",
                    key=f"open_{row['Resume']}"
                ):

                    st.session_state[
                        "selected_resume"
                    ] = row["Resume"]

                    st.switch_page(
                        "pages/2_Candidate_Details.py"
                    )

            # Remove from Shortlist
            with col2:

                if st.button(
                    "Remove",
                    key=f"remove_{row['Resume']}"
                ):

                    df = df[
                        df["Resume"] != row["Resume"]
                    ]

                    df.to_csv(
                        "reports/shortlisted_candidates.csv",
                        index=False
                    )

                    st.success(
                        f"{row['Resume']} removed from shortlist."
                    )

                    st.rerun()