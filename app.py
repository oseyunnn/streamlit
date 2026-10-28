"""
=============================================================================
AJ'S WORLD: A DEVELOPER'S DIARY • VOL. 01
CSIT 349 · Applied AI | Activity: Autobiography and Portfolio App
Student: Angela Jahziel Encabo
Section: Section F2 · Cebu Institute of Technology–University (CIT-U)
=============================================================================
"""

import streamlit as st

# 1. Page Configuration (Required by Professor)
st.set_page_config(
    page_title="Angela Jahziel Encabo | Portfolio",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Imports
from data.content import PERSONAL_INFO
from utils.helpers import load_css, get_image_base64
from components.cover import render_cover_section
from components.story import render_story_section
from components.skills import render_skills_section
from components.projects import render_projects_section
from components.contact import render_contact_section
from components.arcade import render_arcade_section

# 3. Inject Clean Y2K Magazine CSS
st.markdown(load_css(), unsafe_allow_html=True)

# 4. Sidebar: Clean Navigation & Student Credentials
with st.sidebar:
    st.markdown(
        """
        <div style="background: #FFFFFF; border: 2px solid #E0218A; border-radius: 14px; padding: 12px 16px; margin-bottom: 15px; box-shadow: 0 4px 12px rgba(224, 33, 138, 0.1);">
            <div style="font-family: 'Space Mono', monospace; font-size: 0.7rem; font-weight: 700; color: #C2185B; letter-spacing: 1.5px;">
                TABLE OF CONTENTS
            </div>
            <div style="font-family: 'Syne', sans-serif; font-size: 1.35rem; font-weight: 900; color: #E0218A; margin-top: 2px;">
                AJ'S WORLD
            </div>
            <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; color: #22121E;">
                THE DEVELOPER EDITION · VOL. 01
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Navigation Radio Selector
    nav_option = st.radio(
        "Select Magazine Spread:",
        options=[
            "All Spreads (Continuous)",
            "00 // All About Me (Hero & Diary)",
            "01 // The Story (Autobiography)",
            "02 // The Skill Sheet (Infographic)",
            "03 // The Project Closet (Runway)",
            "04 // Dear AJ (Reader Mail)",
            "05 // The Y2K Lounge (Quiz & Archive)"
        ],
        index=0,
        help="Navigate between distinct magazine spreads"
    )
    
    st.divider()
    
    # Student Verification & Academic Credentials (Required by Rubric)
    st.markdown(
        f"""
        <div style="background: #FFF5F8; border-left: 3.5px solid #E0218A; border-radius: 0 8px 8px 0; padding: 10px 14px; font-size: 0.84rem; margin-bottom: 12px;">
            <div style="font-family: 'Space Mono', monospace; font-size: 0.7rem; font-weight: 700; color: #C2185B;">
                STUDENT RECORD
            </div>
            <div style="font-weight: 800; color: #22121E; margin-top: 2px;">{PERSONAL_INFO['name']}</div>
            <div style="color: #444; font-size: 0.82rem;">{PERSONAL_INFO['program']}</div>
            <div style="color: #E0218A; font-weight: 700; font-family: 'Space Mono', monospace; margin-top: 3px;">
                SECTION: {PERSONAL_INFO['section']}
            </div>
            <div style="color: #555; font-size: 0.78rem;">{PERSONAL_INFO['institution']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.link_button("Official GitHub Profile", url=PERSONAL_INFO["github"], use_container_width=True)
    
    st.write("")
    with st.expander("Design System Palette"):
        for color in PERSONAL_INFO["palette"]:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; font-size: 0.75rem;">
                    <span>{color['name']}</span>
                    <span style="background: {color['hex']}; width: 28px; height: 16px; border-radius: 4px; display: inline-block; border: 1px solid #CCC;"></span>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    st.caption("Built for CSIT 349 · Applied AI with Streamlit")

# 5. Main Canvas Display Routing
if nav_option == "All Spreads (Continuous)":
    render_cover_section()
    st.markdown("<hr style='border: none; border-top: 1.5px dashed #FFD2E2; margin: 3rem 0;' />", unsafe_allow_html=True)
    render_story_section()
    st.markdown("<hr style='border: none; border-top: 1.5px dashed #FFD2E2; margin: 3rem 0;' />", unsafe_allow_html=True)
    render_skills_section()
    st.markdown("<hr style='border: none; border-top: 1.5px dashed #FFD2E2; margin: 3rem 0;' />", unsafe_allow_html=True)
    render_projects_section()
    st.markdown("<hr style='border: none; border-top: 1.5px dashed #FFD2E2; margin: 3rem 0;' />", unsafe_allow_html=True)
    render_contact_section()
    st.markdown("<hr style='border: none; border-top: 1.5px dashed #FFD2E2; margin: 3rem 0;' />", unsafe_allow_html=True)
    render_arcade_section()

elif nav_option == "00 // All About Me (Hero & Diary)":
    render_cover_section()

elif nav_option == "01 // The Story (Autobiography)":
    render_story_section()

elif nav_option == "02 // The Skill Sheet (Infographic)":
    render_skills_section()

elif nav_option == "03 // The Project Closet (Runway)":
    render_projects_section()

elif nav_option == "04 // Dear AJ (Reader Mail)":
    render_contact_section()

elif nav_option == "05 // The Y2K Lounge (Quiz & Archive)":
    render_arcade_section()

# 6. Clean Editorial Footer
st.write("")
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 3.5rem; padding: 2rem 1rem; border-top: 1.5px solid #FFD2E2; color: #555; font-size: 0.85rem;">
        <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.1rem; color: #E0218A;">
            AJ'S WORLD • {PERSONAL_INFO['edition']}
        </div>
        <div style="margin-top: 4px;">
            Authored by <b>{PERSONAL_INFO['name']}</b> ({PERSONAL_INFO['section']}) • {PERSONAL_INFO['institution']}
        </div>
        <div style="font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #C2185B; margin-top: 4px;">
            BIG IDEAS. A LITTLE GLITTER. CODE WITH A PURPOSE.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
