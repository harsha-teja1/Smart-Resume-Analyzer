def calculate_overall_score(ats_score, quality_score):
    """
    Calculate overall candidate score
    using 70% ATS score and 30% resume quality score.
    """

    overall_score = (
        (ats_score * 0.7)
        + (quality_score * 0.3)
    )

    return round(overall_score, 2)