import os

import streamlit as st

from data.content import PROJECTS_DATA


def _render_project_card(project):
    with st.container(border=True):
        st.caption(f"{project['number']} / {project['tag']}")
        st.markdown(f"### {project['title']}")
        st.caption(project["role"])
        st.write(project["summary"])

        image_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            project["image"],
        )
        if os.path.exists(image_path):
            st.image(
                image_path,
                caption=project["title"],
                use_container_width=True,
            )
        else:
            with st.container(border=True):
                st.caption("PROJECT IMAGE")
                st.write(f"Add a project screenshot at {project['image']}.")

        st.caption(f"Tools Used · {', '.join(project['tools'])}")
        st.info(f"Outcome · {project['outcome']}")
        st.link_button(
            "View Project on GitHub",
            url=project["link"],
            use_container_width=True,
        )


def render_projects_section():
    """Show project cards using native Streamlit components."""
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.caption("04 / THE PROJECT CLOSET")
    st.markdown("## Featured Projects")
    st.write("A selection of game, digital-safety, and systems projects I’ve worked on.")

    project_filter = st.selectbox(
        "Browse Projects",
        options=["All Projects"] + [project["title"] for project in PROJECTS_DATA],
        help="Choose one project to focus on, or show the complete portfolio.",
    )
    visible_projects = (
        PROJECTS_DATA
        if project_filter == "All Projects"
        else [project for project in PROJECTS_DATA if project["title"] == project_filter]
    )

    project_columns = st.columns(2, gap="large")
    for index, project in enumerate(visible_projects):
        with project_columns[index % 2]:
            _render_project_card(project)
