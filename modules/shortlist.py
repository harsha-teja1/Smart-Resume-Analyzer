import pandas as pd
import os


def add_to_shortlist(
        resume_name,
        ats_score,
        quality_score,
        overall_score):

    file_path = "reports/shortlisted_candidates.csv"

    # Create file if it doesn't exist
    if not os.path.exists(file_path):

        pd.DataFrame(
            columns=[
                "Resume",
                "ATS Score",
                "Resume Quality",
                "Overall Score"
            ]
        ).to_csv(
            file_path,
            index=False
        )

    # Read existing data
    existing_data = pd.read_csv(file_path)

    # Fix corrupted file with missing columns
    if "Resume" not in existing_data.columns:

        existing_data = pd.DataFrame(
            columns=[
                "Resume",
                "ATS Score",
                "Resume Quality",
                "Overall Score"
            ]
        )

    # Prevent duplicate entries
    if (
        len(existing_data) > 0
        and resume_name in existing_data["Resume"].values
    ):
        return

    # New shortlisted candidate
    new_data = pd.DataFrame({
        "Resume": [resume_name],
        "ATS Score": [ats_score],
        "Resume Quality": [quality_score],
        "Overall Score": [overall_score]
    })

    # Append candidate
    updated_data = pd.concat(
        [existing_data, new_data],
        ignore_index=True
    )

    # Save
    updated_data.to_csv(
        file_path,
        index=False
    )