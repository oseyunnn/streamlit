import streamlit as st
import os
from data.content import BIO_SECTIONS, MILESTONES, PERSONAL_INFO
from utils.helpers import get_image_base64, render_sticker


def render_story_section():
    """Render 01 / THE STORY: Autobiography, background, education, and milestones."""
    
    st.markdown(
        """
        <div class="spread-title">
            <span>01 / THE STORY: A LITTLE ABOUT ME</span>
            <span class="spread-category">AUTOBIOGRAPHY • CIT-U CS</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_text, col_interactive = st.columns([1.3, 1.1], gap="large")
    
    with col_text:
        st.markdown(
            f"""
            <div style="margin-bottom: 1rem;">
                <span class="sticker-pill">🌸 Angela Jahziel Encabo</span>
                <span class="sticker-pill">🎓 {PERSONAL_INFO['program']}</span>
                <span class="sticker-pill">📌 {PERSONAL_INFO['section']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Display each autobiography section with styled headers and badges
        for sec in BIO_SECTIONS:
            st.markdown(
                f"""
                <div style="background: #FFFFFF; border-left: 4px solid #FF1493; border-radius: 0 12px 12px 0; padding: 14px 18px; margin-bottom: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03);">
                    <div style="font-family: 'Space Grotesk', sans-serif; font-size: 0.72rem; font-weight: 800; color: #FF1493; letter-spacing: 1.5px; text-transform: uppercase;">
                        {sec['badge']}
                    </div>
                    <div style="font-family: 'Syne', sans-serif; font-size: 1.15rem; font-weight: 800; color: #2B1020; margin: 3px 0 6px 0;">
                        {sec['icon']} {sec['heading']}
                    </div>
                    <div style="font-size: 0.94rem; line-height: 1.6; color: #3E1E31;">
                        {sec['text']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        # Optional reading mode toggle via checkbox
        st.write("")
        show_philosophy_memo = st.checkbox("💖 Reveal Developer Motto & Notebook Note", value=True)
        if show_philosophy_memo:
            st.info(
                "💡 **AJ's Core Belief:** \"I do not believe growth comes from having everything figured out; "
                "I believe it comes from being intentional about the choices we make and remaining willing to learn from them.\""
            )

    with col_interactive:
        # Retro Window Card: Interactive Milestone Journey
        st.markdown(
            f"""
            <div class="retro-window">
                <div class="retro-window-header">
                    <span>⏳ TIMELINE_EXPLORER.EXE</span>
                    <div class="retro-window-controls">
                        <span class="retro-ctrl-btn retro-ctrl-min"></span>
                        <span class="retro-ctrl-btn retro-ctrl-max"></span>
                        <span class="retro-ctrl-btn retro-ctrl-close"></span>
                    </div>
                </div>
                <div class="retro-window-body">
                    <p style="font-size: 0.88rem; color: #4A1A32; margin-top: 0;">
                        Slide through my academic and competition journey from my first lines of C++ code to 
                        hackathon trophies and published game jams!
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Interactive Slider component from lecture
        selected_year = st.select_slider(
            "Select Journey Milestone Year:",
            options=["2023", "2024", "2025", "2026"],
            value="2025"
        )
        
        # Filter and display milestones matching or relevant to that year
        matching_milestones = [m for m in MILESTONES if m["year"] == selected_year]
        
        st.markdown(f"#### 📅 Milestones for **{selected_year}**")
        for m in matching_milestones:
            st.markdown(
                f"""
                <div class="timeline-card">
                    <div style="display: flex; justify-content: space-between; align-items: baseline;">
                        <span class="timeline-year">{m['year']}</span>
                        <span class="sticker-tag">{m['badge']}</span>
                    </div>
                    <div style="font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 800; color: #2B1020; margin-top: 4px;">
                        {m['title']}
                    </div>
                    <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 0.88rem; color: #D81B60; margin-bottom: 6px;">
                        {m['subtitle']}
                    </div>
                    <div style="font-size: 0.9rem; line-height: 1.5; color: #4A2035;">
                        {m['details']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        # Cher Horowitz Y2K aesthetic sticker feature
        cher_uri = get_image_base64("assets/images/cher_as_if.png")
        if cher_uri:
            st.markdown(
                f"""
                <div style="text-align: center; margin-top: 1.5rem; background: #FFF0F5; border: 2px dashed #FF85B3; border-radius: 16px; padding: 14px;">
                    <img src="{cher_uri}" style="max-width: 170px; border-radius: 12px; box-shadow: 0 4px 12px rgba(255,20,147,0.25);" alt="Cher As If" />
                    <div style="font-family: 'Space Grotesk', sans-serif; font-size: 0.78rem; font-weight: 700; color: #D81B60; margin-top: 8px;">
                        "As IF any bug is going to stay in production!" ✨
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        # All milestones in an expander for complete review
        with st.expander("📚 View Complete Chronological History (2023 - Present)"):
            for m in MILESTONES:
                st.write(f"**{m['year']} — {m['title']}** ({m['badge']})")
                st.caption(f"{m['subtitle']} • {m['details']}")
