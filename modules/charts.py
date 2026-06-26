import plotly.express as px

def create_pie_chart(matched_skills, missing_skills):

    labels = ["Matched Skills", "Missing Skills"]
    values = [len(matched_skills), len(missing_skills)]

    fig = px.pie(
        names=labels,
        values=values,
        title="Skill Match Analysis"
    )

    return fig