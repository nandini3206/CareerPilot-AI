import plotly.graph_objects as go
import plotly.express as px

def create_ats_score_gauge(score: float):
    """
    Renders a dark-themed Plotly gauge chart for ATS Match Score / Health Score.
    """
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            domain={"x": [0, 1], "y": [0, 1]},
            number={"suffix": "%", "font": {"color": "#F8FAFC", "size": 36, "family": "Inter"}},
            gauge={
                "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "#64748B"},
                "bar": {"color": "#6366F1", "thickness": 0.3},
                "bgcolor": "rgba(17, 24, 39, 0.6)",
                "borderwidth": 1,
                "bordercolor": "rgba(255, 255, 255, 0.08)",
                "steps": [
                    {"range": [0, 40], "color": "rgba(239, 68, 68, 0.2)"},
                    {"range": [40, 75], "color": "rgba(245, 158, 11, 0.2)"},
                    {"range": [75, 100], "color": "rgba(16, 185, 129, 0.2)"},
                ],
            },
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"color": "#94A3B8", "family": "Inter"},
        height=220,
        margin=dict(l=20, r=20, t=30, b=20),
    )
    return fig


def create_keyword_match_donut(matched_count: int, missing_count: int):
    """
    Renders a Donut Chart showing Matched vs Missing Keyword Ratio.
    """
    labels = ["Matched Keywords", "Missing Keywords"]
    values = [max(1, matched_count), max(0, missing_count)]
    colors = ["#10B981", "#EF4444"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.6,
                marker=dict(colors=colors, line=dict(color="#090D16", width=2)),
                textinfo="label+value",
                textfont=dict(color="#F8FAFC", family="Inter", size=11),
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F8FAFC", family="Inter"),
        height=240,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
    )
    return fig


def create_skills_horizontal_bar(matching_skills: list, missing_skills: list):
    """
    Renders a horizontal bar chart comparing Matched Skills vs Missing Requirements.
    """
    skills = (matching_skills[:5] + missing_skills[:5])
    status = (["Matched"] * len(matching_skills[:5])) + (["Missing"] * len(missing_skills[:5]))
    scores = ([100] * len(matching_skills[:5])) + ([35] * len(missing_skills[:5]))
    colors = (["#10B981"] * len(matching_skills[:5])) + (["#EF4444"] * len(missing_skills[:5]))

    if not skills:
        skills = ["Python", "SQL", "Machine Learning", "AWS", "Docker"]
        scores = [100, 100, 100, 35, 35]
        colors = ["#10B981", "#10B981", "#10B981", "#EF4444", "#EF4444"]

    fig = go.Figure(
        go.Bar(
            x=scores,
            y=skills,
            orientation="h",
            marker=dict(color=colors, cornerradius=4),
            text=[f"{s}%" for s in scores],
            textposition="auto",
            textfont=dict(color="#F8FAFC", family="Inter", size=11),
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(range=[0, 110], gridcolor="rgba(255,255,255,0.08)", tickfont=dict(color="#64748B")),
        yaxis=dict(tickfont=dict(color="#F8FAFC"), autorange="reversed"),
        font=dict(color="#F8FAFC", family="Inter"),
        height=250,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig


def create_resume_composition_donut(sections: dict):
    """
    Renders a Donut Chart showing text proportion across resume sections.
    """
    labels = []
    values = []
    for sec, text in sections.items():
        wc = len(text.split())
        if wc > 0:
            labels.append(sec.capitalize())
            values.append(wc)

    if not values:
        labels = ["Summary", "Experience", "Skills", "Education", "Projects"]
        values = [50, 200, 80, 60, 100]

    colors = ["#6366F1", "#06B6D4", "#8B5CF6", "#10B981", "#F59E0B"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.55,
                marker=dict(colors=colors, line=dict(color="#090D16", width=2)),
                textinfo="label+percent",
                textfont=dict(color="#F8FAFC", family="Inter", size=11),
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F8FAFC", family="Inter"),
        height=260,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
    )
    return fig


def create_section_completeness_chart(sections: dict):
    """
    Renders a horizontal bar chart showing completeness score per section.
    """
    sec_names = ["Summary", "Education", "Skills", "Projects", "Experience"]
    scores = []
    colors = []

    for sec in ["summary", "education", "skills", "projects", "experience"]:
        text = sections.get(sec, "").strip()
        if text:
            wc = len(text.split())
            s = min(100, int((wc / 30) * 100)) if wc < 30 else 100
            scores.append(s)
            colors.append("#10B981" if s > 70 else "#F59E0B")
        else:
            scores.append(0)
            colors.append("#EF4444")

    fig = go.Figure(
        go.Bar(
            x=scores,
            y=sec_names,
            orientation="h",
            marker=dict(color=colors, cornerradius=4),
            text=[f"{s}%" for s in scores],
            textposition="auto",
            textfont=dict(color="#F8FAFC", family="Inter", size=11),
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(range=[0, 105], gridcolor="rgba(255,255,255,0.08)", tickfont=dict(color="#64748B")),
        yaxis=dict(tickfont=dict(color="#F8FAFC"), autorange="reversed"),
        font=dict(color="#F8FAFC", family="Inter"),
        height=240,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig


def create_skill_radar_chart(skills: list, match_scores: list = None):
    """
    Renders a Plotly Radar Chart of candidate skill distribution.
    """
    if not skills:
        skills = ["Python", "Machine Learning", "SQL", "APIs", "Data Structures"]
    
    if not match_scores or len(match_scores) != len(skills):
        match_scores = [85 + (i % 3)*5 for i in range(len(skills))]

    fig = go.Figure(
        data=go.Scatterpolar(
            r=match_scores[:7],
            theta=skills[:7],
            fill="toself",
            fillcolor="rgba(99, 102, 241, 0.25)",
            line=dict(color="#6366F1", width=2),
            marker=dict(size=6, color="#06B6D4"),
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="rgba(255,255,255,0.08)", tickfont=dict(color="#64748B")),
            angularaxis=dict(gridcolor="rgba(255,255,255,0.08)", tickfont=dict(color="#F8FAFC", size=11)),
            bgcolor="rgba(17, 24, 39, 0.5)",
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F8FAFC", family="Inter"),
        height=280,
        margin=dict(l=30, r=30, t=20, b=20),
        showlegend=False,
    )
    return fig


def create_salary_benchmark_chart(predicted_salary: float):
    """
    Renders a Plotly bar chart showing estimated salary vs market ranges.
    """
    roles = ["25th Percentile", "Predicted Salary", "75th Percentile", "Top Tier (90th)"]
    values = [
        predicted_salary * 0.75,
        predicted_salary,
        predicted_salary * 1.30,
        predicted_salary * 1.65,
    ]
    colors = ["#64748B", "#6366F1", "#8B5CF6", "#06B6D4"]

    fig = go.Figure(
        data=[
            go.Bar(
                x=roles,
                y=values,
                marker_color=colors,
                text=[f"${v:,.0f}" for v in values],
                textposition="auto",
                textfont=dict(color="#F8FAFC", family="Inter", size=12),
            )
        ]
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(gridcolor="rgba(255,255,255,0.08)", tickfont=dict(color="#64748B"), title="Salary (USD)"),
        xaxis=dict(tickfont=dict(color="#F8FAFC")),
        font=dict(color="#F8FAFC", family="Inter"),
        height=300,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    return fig
