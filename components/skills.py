import altair as alt
import pandas as pd
import streamlit as st

from data.content import SKILLS_DATA


def render_skills_section():
    """Show skill descriptions and a chart of the current self-ratings."""
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.caption("03 / THE SKILL SHEET")
    st.markdown("## Skills and Tech Stack")
    st.write(
        "These are my own estimates of skills I have practiced through coursework, "
        "team projects, and game jams—not formal test results."
    )

    skill_columns = st.columns(2, gap="large")
    skill_groups = [
        [skill for skill in SKILLS_DATA if skill["category"] != "Non-technical"],
        [skill for skill in SKILLS_DATA if skill["category"] == "Non-technical"],
    ]
    group_titles = ("Technical Skills", "Non-technical Skills")

    for column, skills, title in zip(skill_columns, skill_groups, group_titles):
        with column:
            st.markdown(f"### {title}")
            for skill in skills:
                with st.container(border=True):
                    st.markdown(f"**{skill['skill']}**")
                    st.caption(skill["category"])
                    st.write(skill["description"])

    rating_table = pd.DataFrame(
        [
            {
                "Skill": skill["skill"],
                "Self-rating": skill["score"],
                "Category": skill["category"],
            }
            for skill in SKILLS_DATA
        ]
    )

    st.markdown("### My Self-Ratings")
    chart = (
        alt.Chart(rating_table)
        .mark_bar(cornerRadiusEnd=6, color="#D94F91")
        .encode(
            x=alt.X(
                "Self-rating:Q",
                title="Self-rating (0–100)",
                scale=alt.Scale(domain=[0, 100]),
            ),
            y=alt.Y("Skill:N", sort="-x", title=None),
            tooltip=["Skill:N", "Self-rating:Q", "Category:N"],
        )
        .properties(height=max(240, len(rating_table) * 30))
        .configure_axis(gridColor="#F1E4EB", labelColor="#514653")
        .configure_view(stroke=None)
    )
    st.altair_chart(chart, use_container_width=True)
    st.dataframe(rating_table, use_container_width=True, hide_index=True)

    st.markdown("### Tools I’ve Used")
    tools_col1, tools_col2 = st.columns(2, gap="medium")
    tool_groups = (
        ("Languages and Web", "JavaScript, GDScript, PHP, Python, HTML/CSS"),
        ("Platforms and Data", "Godot, Node.js, Streamlit, MySQL, Microsoft Azure AI"),
    )
    for column, (label, tools) in zip((tools_col1, tools_col2), tool_groups):
        with column:
            with st.container(border=True):
                st.caption(label)
                st.write(tools)
