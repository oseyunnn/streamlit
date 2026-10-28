"""
=============================================================================
AJ'S WORLD: A DEVELOPER'S DIARY • VOL. 01
CSIT 349 · Applied AI | Activity: Autobiography and Portfolio App
Student: Angela Jahziel Encabo
Section: Section F2 · Cebu Institute of Technology–University (CIT-U)
=============================================================================
"""

import streamlit as st

# Page setup
st.set_page_config(
    page_title="AJ's World | Portfolio",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Imports
from data.content import PERSONAL_INFO
from utils.helpers import load_css
from components.cover import render_cover_section
from components.story import render_story_section
from components.skills import render_skills_section
from components.projects import render_projects_section
from components.contact import render_contact_section

# Apply the shared theme
st.markdown(load_css(), unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        """
        <div class="portal-brand-title">AJ's World</div>
        <div class="portal-brand-sub">A little life, a little code.</div>
        """,
        unsafe_allow_html=True
    )
    st.caption("JUMP TO")
    for label, section_id in (
        ("About", "about"),
        ("My story", "story"),
        ("Skills", "skills"),
        ("Projects", "projects"),
        ("Contact & review", "contact"),
    ):
        st.markdown(
            f'<a class="sidebar-section-link" href="#{section_id}">{label}</a>',
            unsafe_allow_html=True
        )
    st.divider()
    st.caption(f"{PERSONAL_INFO['section']} · {PERSONAL_INFO['institution']}")
    st.link_button("Find me on GitHub", url=PERSONAL_INFO["github"], use_container_width=True)

render_cover_section()
st.divider()
render_story_section()
st.divider()
render_skills_section()
st.divider()
render_projects_section()
st.divider()
render_contact_section()

st.markdown(
    f"""
    <div style="text-align: center; margin-top: 3rem; padding: 1.5rem 1rem; border-top: 1px solid #eee5e9; color: #716873; font-size: .85rem;">
        <div style="font-size: 1.1rem; color: #d94f91; font-weight: 700;">AJ's World</div>
        <div style="margin-top: .35rem;">
            Made by <b>{PERSONAL_INFO['name']}</b> · {PERSONAL_INFO['institution']}
        </div>
        <div style="margin-top: .35rem;">Big ideas, a little glitter, and code with a purpose.</div>
    </div>
    """,
    unsafe_allow_html=True
)
