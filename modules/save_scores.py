import pandas as pd
import os


def save_candidate_score(
        resume_name,
        ats_score,
        quality_score,
        overall_score):

    file_path = "reports/candidate_scores.csv"

    # Create dataframe for current candidate
    new_data = pd.DataFrame({
        "Resume": [resume_name],
        "ATS Score": [round(ats_score, 2)],
        "Resume Quality": [quality_score],
        "Overall Score": [round(overall_score, 2)]
    })

    # If CSV exists, load it
    if os.path.exists(file_path):

        existing_data = pd.read_csv(file_path)

        # Remove old entry if same resume already exists
        existing_data = existing_data[
            existing_data["Resume"] != resume_name
        ]

        # Append new entry
        updated_data = pd.concat(
            [existing_data, new_data],
            ignore_index=True
        )

    else:
        updated_data = new_data

    # Save updated file
    updated_data.to_csv(
        file_path,
        index=False
    )