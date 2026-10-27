"""
=============================================================================
AJ'S WORLD: A DEVELOPER'S DIARY • VOL. 01
CSIT 349 · Applied AI | Activity: Autobiography and Portfolio App
Student: Angela Jahziel Encabo
Section: Section F2 · Cebu Institute of Technology–University (CIT-U)
=============================================================================
"""

import streamlit as st
import os

# 1. Page Configuration (Required by Professor)
st.set_page_config(
    page_title="Angela Jahziel Encabo | Portfolio",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Import Data and Components
from data.content import PERSONAL_INFO, BIO_SECTIONS, SKILLS_DATA, PROJECTS_DATA
from utils.helpers import load_css, render_sticker, get_image_base64
from components.cover import render_cover_section
from components.story import render_story_section
from components.skills import render_skills_section
from components.projects import render_projects_section
from components.contact import render_contact_section
from components.arcade import render_arcade_section

# 3. Inject Custom Y2K Bratz / Barbie Magazine CSS
st.markdown(load_css(), unsafe_allow_html=True)

# 4. Sidebar: Editorial Table of Contents & Quick Badges
with st.sidebar:
    # Sidebar Bratz / Barbie Sticker Badge
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <div style="display: inline-block; background: #FFFFFF; border: 3px solid #FF1493; border-radius: 18px; padding: 10px 16px; box-shadow: 0 6px 16px rgba(255,20,147,0.25);">
                <span style="font-family: 'Space Grotesk', sans-serif; font-size: 0.75rem; font-weight: 800; color: #D81B60; letter-spacing: 2px;">TABLE OF CONTENTS</span>
                <div style="font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 900; color: #FF1493; margin-top: 2px;">AJ'S WORLD</div>
                <div style="font-size: 0.72rem; color: #2B1020; font-weight: 700;">VOL. 01 • DEV EDITION</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Navigation Radio Component
    navigation_mode = st.radio(
        "Navigate Magazine Spreads:",
        options=[
            "✨ Full Magazine (Continuous)",
            "🌟 Cover Hero Spread",
            "📖 01 / The Story (Autobiography)",
            "📊 02 / The Skill Sheet",
            "👗 03 / The Project Closet",
            "💌 04 / Dear AJ (Reader Mail)",
            "🎮 05 / The Y2K Lounge & Arcade"
        ],
        index=0,
        help="Select a specific spread or view the full magazine issue"
    )
    
    st.divider()
    
    # Student Verification & Academic Credentials (Rubric requirement)
    st.markdown(
        f"""
        <div style="background: #FFFFFF; border-left: 4px solid #FF1493; border-radius: 0 10px 10px 0; padding: 10px 12px; margin-bottom: 12px; font-size: 0.84rem;">
            <div style="font-weight: 800; color: #D81B60;">STUDENT DETAILS</div>
            <div style="color: #2B1020; font-weight: 700; margin-top: 2px;">{PERSONAL_INFO['name']}</div>
            <div style="color: #4A1A32;">{PERSONAL_INFO['program']}</div>
            <div style="color: #FF1493; font-weight: 700; margin-top: 2px;">Section: {PERSONAL_INFO['section']}</div>
            <div style="color: #4A1A32; font-size: 0.78rem;">{PERSONAL_INFO['institution']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Quick Links
    st.link_button("🐙 Visit AJ's GitHub", url=PERSONAL_INFO["github"], use_container_width=True)
    
    # Interactive Music / Vibe Check
    st.write("")
    with st.expander("💖 Vibe Palette & Theme"):
        st.write("**Editorial Color Scheme:**")
        cols = st.columns(3)
        for idx, color in enumerate(PERSONAL_INFO["palette"]):
            c = cols[idx % 3]
            with c:
                st.markdown(
                    f"""
                    <div style="background: {color['hex']}; color: {'#FFF' if color['hex'] in ['#FF1493', '#D81B60', '#1A1A1A'] else '#2B1020'}; padding: 6px; border-radius: 6px; text-align: center; font-size: 0.68rem; font-weight: bold; margin-bottom: 6px; border: 1px solid #CCC;">
                        {color['name']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
    st.caption("✨ Built for CSIT 349 • Applied AI with Streamlit")

# 5. Main Canvas Display Routing
if navigation_mode == "✨ Full Magazine (Continuous)":
    render_cover_section()
    st.markdown("<hr style='border: 1px dashed #FF85B3; margin: 2.5rem 0;' />", unsafe_allow_html=True)
    render_story_section()
    st.markdown("<hr style='border: 1px dashed #FF85B3; margin: 2.5rem 0;' />", unsafe_allow_html=True)
    render_skills_section()
    st.markdown("<hr style='border: 1px dashed #FF85B3; margin: 2.5rem 0;' />", unsafe_allow_html=True)
    render_projects_section()
    st.markdown("<hr style='border: 1px dashed #FF85B3; margin: 2.5rem 0;' />", unsafe_allow_html=True)
    render_contact_section()
    st.markdown("<hr style='border: 1px dashed #FF85B3; margin: 2.5rem 0;' />", unsafe_allow_html=True)
    render_arcade_section()

elif navigation_mode == "🌟 Cover Hero Spread":
    render_cover_section()

elif navigation_mode == "📖 01 / The Story (Autobiography)":
    render_story_section()

elif navigation_mode == "📊 02 / The Skill Sheet":
    render_skills_section()

elif navigation_mode == "👗 03 / The Project Closet":
    render_projects_section()

elif navigation_mode == "💌 04 / Dear AJ (Reader Mail)":
    render_contact_section()

elif navigation_mode == "🎮 05 / The Y2K Lounge & Arcade":
    render_arcade_section()

# 6. Editorial Footer
st.write("")
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 3.5rem; padding: 2rem 1rem; border-top: 2px solid #FFE4EC; color: #6A3252; font-size: 0.85rem;">
        <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #FF1493;">
            AJ'S WORLD • {PERSONAL_INFO['edition']}
        </div>
        <div style="margin-top: 4px;">
            Designed & Authored by <b>{PERSONAL_INFO['name']}</b> ({PERSONAL_INFO['section']}) • {PERSONAL_INFO['institution']}
        </div>
        <div style="font-family: 'Space Grotesk', sans-serif; font-size: 0.78rem; color: #D81B60; margin-top: 6px; letter-spacing: 1px;">
            BIG IDEAS. A LITTLE GLITTER. CODE WITH A PURPOSE.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
