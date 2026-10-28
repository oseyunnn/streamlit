import streamlit as st
import os
from data.content import PERSONAL_INFO, DIARY_PROMPTS
from utils.helpers import get_image_base64


def render_cover_section():
    """Render Page 1 / Hero: Barbie Diaries & MyScene Portal Spread."""
    
    # 1. MyScene / Barbie Diaries Portal Header
    barbie_logo_uri = get_image_base64("assets/images/barbie_logo.svg")
    
    st.markdown(
        f"""
        <div class="myscene-portal-header">
            <div class="portal-brand">
                {f'<img src="{barbie_logo_uri}" style="height: 38px;" alt="Barbie" />' if barbie_logo_uri else ''}
                <div>
                    <div class="portal-brand-title">aj-world.com</div>
                    <div class="portal-brand-sub">THE DEVELOPER EDITION • VOL. 01 // CIT-U CS</div>
                </div>
            </div>
            <div class="portal-nav-pills">
                <span class="portal-pill active">All About AJ</span>
                <span class="portal-pill">The Skill Sheet</span>
                <span class="portal-pill">Project Runway</span>
                <span class="portal-pill">Reader Mail</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 2. Main 2-Column Spread: Left Polaroid & Phone, Right Ruled Diary Sheet
    col_visual, col_diary = st.columns([1.1, 1.4], gap="large")
    
    with col_visual:
        # Pinned Polaroid with Silver Paperclip
        photo_uri = get_image_base64("assets/images/angela_portrait.jpg")
        paperclip_uri = get_image_base64("assets/images/paperclip.svg")
        barcode_uri = get_image_base64("assets/images/barcode.svg")
        
        st.markdown(
            f"""
            <div style="position: relative; margin-top: 15px; margin-bottom: 25px;">
                {f'<img src="{paperclip_uri}" class="paperclip-pin" alt="Paperclip" />' if paperclip_uri else ''}
                <div class="polaroid-frame" style="transform: rotate(-2deg);">
                    <img src="{photo_uri}" style="width: 100%; border-radius: 2px; display: block; max-height: 380px; object-fit: cover;" alt="Angela Encabo" />
                    <div class="polaroid-caption">
                        Angela Jahziel Encabo
                        <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; color: #880E4F; font-weight: normal; margin-top: 4px;">
                            CIT-U CS · SECTION F2
                        </div>
                    </div>
                </div>
                {f'<div style="text-align: center; margin-top: 12px;"><img src="{barcode_uri}" style="height: 36px; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.06);" alt="Barcode" /></div>' if barcode_uri else ''}
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Subtle caption without emoji
        st.caption("Class of 2026 · Third-Year Bachelor of Science in Computer Science")
        
    with col_diary:
        # Ruled Notebook Sheet (Barbie Diaries Style from Inspo 3)
        prompts_html = ""
        for p in DIARY_PROMPTS:
            prompts_html += f"""
            <div class="diary-row">
                <span class="diary-label">{p['label']}:</span>
                <span class="diary-value">{p['value']}</span>
            </div>
            """
            
        st.markdown(
            f"""
            <div class="diary-sheet-container">
                <div class="diary-banner-header">
                    BARBIE DIARIES: ALL ABOUT ME
                </div>
                <div class="diary-lined-paper">
                    {prompts_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Clean Editorial Metrics Row (Zero Emojis)
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric(label="ACADEMIC YEAR", value="3rd Year", delta="CIT-U")
        with m2:
            st.metric(label="RUNWAY PROJECTS", value="4 Works", delta="2 Podiums")
        with m3:
            st.metric(label="TOP COMPETENCY", value="90 / 100", delta="Problem Solving")
        with m4:
            st.metric(label="CLASS COHORT", value="SEC F2", delta="Active 2026")
            
        st.write("")
        st.markdown(
            f"""
            <div style="background: #FFF5F8; border-left: 3px solid #E0218A; padding: 12px 16px; border-radius: 0 8px 8px 0; margin-top: 10px;">
                <div style="font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #E0218A; letter-spacing: 1px;">
                    EDITORIAL NOTE
                </div>
                <div style="font-size: 0.92rem; color: #22121E; font-style: italic; margin-top: 4px; line-height: 1.5;">
                    "{PERSONAL_INFO['subtitle']}"
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
