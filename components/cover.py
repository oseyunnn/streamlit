import os

import streamlit as st

from data.content import HOME_BIOGRAPHY, PERSONAL_INFO, PROJECTS_DATA
from utils.helpers import get_image_base64


def render_cover_section():
    """Show the portfolio cover, profile photo, and concise student introduction."""
    logo_uri = get_image_base64("assets/images/barbie_logo.svg")
    logo = f'<img src="{logo_uri}" style="height: 34px;" alt="AJ’s World logo" />' if logo_uri else ""

    st.markdown(
        f"""
        <div class="myscene-portal-header">
            <div class="portal-brand">
                {logo}
                <div>
                    <div class="portal-brand-title">AJ’s World</div>
                    <div class="portal-brand-sub">A Little Life, A Little Code</div>
                </div>
            </div>
            <nav class="portal-nav-pills" aria-label="Page sections">
                <a class="portal-pill active" href="#about">About</a>
                <a class="portal-pill" href="#story">My Story</a>
                <a class="portal-pill" href="#skills">Skills</a>
                <a class="portal-pill" href="#projects">Projects</a>
                <a class="portal-pill" href="#contact">Contact</a>
            </nav>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    photo_col, intro_col = st.columns([0.85, 1.4], gap="large")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    portrait_path = os.path.join(base_dir, "assets", "images", "angela_portrait.jpg")

    with photo_col:
        with st.container(border=True):
            st.caption("PROFILE PHOTO")
            if os.path.exists(portrait_path):
                st.image(
                    portrait_path,
                    caption="Angela Jahziel Encabo · Computer Science Student",
                    use_container_width=True,
                )
            else:
                st.info("Add a current profile photo at assets/images/angela_portrait.jpg.")

    with intro_col:
        with st.container(border=True):
            st.caption("THIRD-YEAR COMPUTER SCIENCE · SECTION F2")
            st.title(PERSONAL_INFO["name"])
            st.markdown(f"**{PERSONAL_INFO['program']}**")
            st.caption(PERSONAL_INFO["institution"])
            st.caption(PERSONAL_INFO["location"])
            st.markdown("### A Little About Me")
            for paragraph in HOME_BIOGRAPHY["autobiography"]:
                st.write(paragraph)
            st.caption(
                "**Campus Organizations** · "
                + " · ".join(HOME_BIOGRAPHY["organizations"])
            )
            interests_col, dislikes_col = st.columns(2, gap="medium")
            with interests_col:
                st.caption("I’M INTO")
                st.write(", ".join(HOME_BIOGRAPHY["interests"]))
            with dislikes_col:
                st.caption("NOT A FAN OF")
                st.write(", ".join(HOME_BIOGRAPHY["dislikes"]))
            st.link_button(
                "Visit My GitHub",
                url=PERSONAL_INFO["github"],
                use_container_width=True,
            )

    metric_cols = st.columns(3)
    summary_cards = (
        ("Year", "Third Year", "Computer Science"),
        ("Featured Work", f"{len(PROJECTS_DATA)} Projects", "Games, AI, and Systems"),
        ("Based In", "Cebu City", "Philippines"),
    )
    for column, (label, value, detail) in zip(metric_cols, summary_cards):
        with column:
            with st.container(border=True):
                st.caption(label)
                st.markdown(f"### {value}")
                st.caption(detail)
