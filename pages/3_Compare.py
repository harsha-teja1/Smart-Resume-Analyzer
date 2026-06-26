import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Compare Candidates",
    layout="wide"
)

st.title("⚔️ Compare Candidates")

# Load candidate scores
df = pd.read_csv(
    "reports/candidate_scores.csv"
)

if len(df) == 0:

    st.info(
        "No candidates available for comparison."
    )

else:

    candidates = df["Resume"].tolist()

    st.subheader("Candidate Selection")

    candidate1 = st.selectbox(
        "🔍 Candidate 1",
        candidates,
        key="candidate1"
    )

    candidate2 = st.selectbox(
        "🔍 Candidate 2",
        candidates,
        key="candidate2"
    )

    if st.button("Compare"):

        if candidate1 == candidate2:

            st.warning(
                "Please select two different candidates."
            )

        else:

            data1 = df[
                df["Resume"] == candidate1
            ].iloc[0]

            data2 = df[
                df["Resume"] == candidate2
            ].iloc[0]

            st.subheader(
                "📊 Comparison Results"
            )

            col1, col2 = st.columns(2)

            with col1:

                with st.container(border=True):

                    st.markdown(
                        f"### 📄 {candidate1}"
                    )

                    st.write(
                        f"📊 ATS Score : {data1['ATS Score']}"
                    )

                    st.write(
                        f"📄 Resume Quality : {data1['Resume Quality']}"
                    )

                    st.write(
                        f"⭐ Overall Score : {data1['Overall Score']}"
                    )

            with col2:

                with st.container(border=True):

                    st.markdown(
                        f"### 📄 {candidate2}"
                    )

                    st.write(
                        f"📊 ATS Score : {data2['ATS Score']}"
                    )

                    st.write(
                        f"📄 Resume Quality : {data2['Resume Quality']}"
                    )

                    st.write(
                        f"⭐ Overall Score : {data2['Overall Score']}"
                    )

            st.divider()

            if data1["Overall Score"] > data2["Overall Score"]:

                st.success(
                    f"💡 Candidate Insight\n\n"
                    f"{candidate1} currently appears to be a stronger match "
                    f"based on ATS Score, Resume Quality, and Overall Score."
                )

            elif data2["Overall Score"] > data1["Overall Score"]:

                st.success(
                    f"💡 Candidate Insight\n\n"
                    f"{candidate2} currently appears to be a stronger match "
                    f"based on ATS Score, Resume Quality, and Overall Score."
                )

            else:

                st.info(
                    "💡 Candidate Insight\n\n"
                    "Both candidates currently have similar evaluation scores."
                )