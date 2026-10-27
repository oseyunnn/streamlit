import streamlit as st
import os
from data.content import PERSONAL_INFO, Y2K_QUOTES
from utils.helpers import render_sticker, get_image_base64


def render_cover_section():
    """Render the magazine cover hero section."""
    
    # Top Ticker / Marquee
    st.markdown(
        """
        <div class="y2k-ticker">
            <span>💖 THE DEVELOPER EDITION • VOL. 01</span>
            <span>⭐ CEBU INSTITUTE OF TECHNOLOGY–UNIVERSITY</span>
            <span>✨ SECTION F2 • BSCS</span>
            <span>💋 BIG IDEAS. A LITTLE GLITTER. CODE WITH A PURPOSE.</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Magazine Masthead Container
    st.markdown(
        f"""
        <div class="masthead-container">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div>
                    <span class="magazine-badge">{PERSONAL_INFO["edition"]}</span>
                    <h1 class="masthead-title">AJ'S WORLD</h1>
                    <div class="masthead-tagline">{PERSONAL_INFO["tagline"]}</div>
                    <div class="masthead-sub">{PERSONAL_INFO["subtitle"]}</div>
                </div>
                <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 6px;">
                    <span class="sticker-pill">📍 {PERSONAL_INFO["location"]}</span>
                    <span class="sticker-pill">🎓 {PERSONAL_INFO["institution"]}</span>
                    <span class="sticker-pill" style="border-color: #D81B60; color: #D81B60;">💻 {PERSONAL_INFO["section"]}</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 2-Column Cover Layout: Left Column = Editorial Feature & Profile Photo, Right Column = Magazine Features & Quick Stats
    col_photo, col_intro = st.columns([1.1, 1.4], gap="large")
    
    with col_photo:
        photo_path = os.path.join("assets", "images", "angela_portrait.jpg")
        photo_uri = get_image_base64(photo_path)
        
        # Bratz Logo / Badge
        bratz_logo_path = os.path.join("assets", "images", "bratz_cover_header.png")
        bratz_logo_uri = get_image_base64(bratz_logo_path)
        
        st.markdown(
            f"""
            <div class="photo-frame-y2k">
                <div style="position: absolute; top: -18px; left: -14px; z-index: 10;">
                    {render_sticker("assets/images/sparkle_star.svg", width="48px", rotate="-15deg")}
                </div>
                <div style="position: absolute; top: -15px; right: -12px; z-index: 10;">
                    {render_sticker("assets/images/chrome_heart.svg", width="46px", rotate="12deg")}
                </div>
                {f'<div style="text-align: center; margin-bottom: 6px;"><img src="{bratz_logo_uri}" style="max-height: 55px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);" alt="Bratz Magazine" /></div>' if bratz_logo_uri else ''}
                <img src="{photo_uri}" style="width: 100%; border-radius: 14px; object-fit: cover; max-height: 440px; display: block;" alt="Angela Jahziel Encabo" />
                <div class="photo-caption-tag">
                    🌸 <b>{PERSONAL_INFO["name"]}</b> • {PERSONAL_INFO["avatar_caption"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.caption("📸 Authentic portrait of Angela • Certified Y2K Developer & Game Creator")
        
    with col_intro:
        # Retro Window Card: Cover Story Preview
        st.markdown(
            f"""
            <div class="retro-window">
                <div class="retro-window-header">
                    <span>🌸 AJ_PROFILE.EXE — COVER STORY INTRO</span>
                    <div class="retro-window-controls">
                        <span class="retro-ctrl-btn retro-ctrl-min"></span>
                        <span class="retro-ctrl-btn retro-ctrl-max"></span>
                        <span class="retro-ctrl-btn retro-ctrl-close"></span>
                    </div>
                </div>
                <div class="retro-window-body">
                    <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px;">
                        <span class="sticker-tag">👑 Third-Year BSCS</span>
                        <span class="sticker-tag">🏆 Hackathon 1st Runner-Up</span>
                        <span class="sticker-tag">🎮 Game Developer</span>
                        <span class="sticker-tag">🛡️ AI Digital Safety</span>
                    </div>
                    <h3 style="font-family: 'Syne', sans-serif; font-size: 1.45rem; color: #2B1020; margin-top: 0;">
                        Welcome to My Developer's Diary! 💖
                    </h3>
                    <p style="font-size: 0.96rem; line-height: 1.6; color: #3A1528;">
                        I am <b>Angela Jahziel Encabo</b>, a third-year Computer Science student at 
                        <b>Cebu Institute of Technology–University (CIT-U)</b>, Section F2. 
                        This portfolio is built like a 2000s glossy magazine spread celebrating intentional 
                        problem-solving, interactive games, AI child protection, and unapologetic creativity!
                    </p>
                    <div style="background: #FFF0F5; border: 2px dashed #FF1493; border-radius: 12px; padding: 12px; margin-top: 10px;">
                        <span style="font-weight: 800; color: #FF1493; font-size: 0.82rem; text-transform: uppercase;">Current Status:</span>
                        <div style="font-style: italic; color: #2B1020; font-size: 0.92rem; margin-top: 2px;">
                            "{PERSONAL_INFO["current_status"]}"
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Editorial Metrics Row
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        with m_col1:
            st.metric(label="Academic Year", value="3rd Year", delta="CIT-U")
        with m_col2:
            st.metric(label="Featured Projects", value="4", delta="2 Wins 🏆")
        with m_col3:
            st.metric(label="Top Skill", value="90 / 100", delta="Problem Solving")
        with m_col4:
            st.metric(label="Vibe Level", value="100%", delta="Y2K Glitter ✨")
            
        # Interactive Quote of the Day
        st.write("")
        col_q_btn, col_q_text = st.columns([1, 2.5])
        with col_q_btn:
            if "quote_idx" not in st.session_state:
                st.session_state.quote_idx = 0
            if st.button("✨ Flip Quote ✨", use_container_width=True):
                st.session_state.quote_idx = (st.session_state.quote_idx + 1) % len(Y2K_QUOTES)
        with col_q_text:
            curr_quote = Y2K_QUOTES[st.session_state.quote_idx]
            st.markdown(
                f"""
                <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.9rem; color: #D81B60; border-left: 3px solid #FF1493; padding-left: 10px;">
                    "{curr_quote['quote']}" — <b>{curr_quote['author']}</b>
                </div>
                """,
                unsafe_allow_html=True
            )
