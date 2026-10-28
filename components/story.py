import streamlit as st
from data.content import BIO_SECTIONS, MILESTONES, PERSONAL_INFO


def render_story_section():
    """Render 01 / THE STORY: Clean editorial autobiography & interactive timeline."""
    
    st.markdown(
        """
        <div style="border-bottom: 2.5px solid #E0218A; padding-bottom: 8px; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap;">
            <div>
                <span style="font-family: 'Space Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #E0218A; letter-spacing: 2px;">01 // THE STORY</span>
                <h2 style="font-family: 'Syne', sans-serif; font-size: 2.2rem; font-weight: 900; color: #22121E; margin: 4px 0 0 0;">
                    A Little About Me
                </h2>
            </div>
            <div style="font-family: 'Space Mono', monospace; font-size: 0.82rem; color: #C2185B;">
                AUTOBIOGRAPHY · CIT-U CS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_narrative, col_widget = st.columns([1.35, 1], gap="large")
    
    with col_narrative:
        # Lined Diary Narrative Blocks (Clean, structured, zero emojis)
        for sec in BIO_SECTIONS:
            st.markdown(
                f"""
                <div style="background: #FFFFFF; border-left: 3.5px solid #E0218A; border-radius: 0 10px 10px 0; padding: 14px 18px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
                    <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; font-weight: 700; color: #E0218A; letter-spacing: 1px;">
                        {sec['badge']}
                    </div>
                    <div style="font-family: 'Syne', sans-serif; font-size: 1.15rem; font-weight: 800; color: #22121E; margin: 3px 0 6px 0;">
                        {sec['heading']}
                    </div>
                    <div style="font-size: 0.94rem; line-height: 1.65; color: #3D2938;">
                        {sec['text']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.write("")
        show_full_quote = st.checkbox("Display Developer Guiding Principle", value=True)
        if show_full_quote:
            st.info(
                "“I am a firm believer in the power of being intentional in how we think, act, and respond to others. "
                "Knowing what you want and making the choice to do what it takes to achieve or overcome it has been "
                "the compass that guides the decisions I make for myself.”"
            )

    with col_widget:
        # Y2K Pink Mobile Phone Widget (Directly inspired by Image 2 "My Phone")
        st.markdown(
            f"""
            <div class="y2k-phone-widget">
                <div class="phone-antenna"></div>
                <div class="phone-screen">
                    <div class="phone-status-bar">
                        <span>CIT-U NET</span>
                        <span>[|||||] 88%</span>
                    </div>
                    <div style="text-align: center; margin: 10px 0 6px 0;">
                        <span style="font-family: 'Space Mono', monospace; font-size: 0.7rem; font-weight: 700; color: #E0218A; background: #FFF; padding: 2px 8px; border-radius: 8px; border: 1px solid #FFAEC9;">
                            INCOMING SMS
                        </span>
                    </div>
                    <div style="background: #FFFFFF; border: 1.5px solid #FF85B3; border-radius: 12px; padding: 12px; font-size: 0.85rem; line-height: 1.5; color: #22121E; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
                        <b>From: AJ Encabo</b><br/>
                        <span style="color: #666; font-size: 0.72rem;">Status Dispatch // CIT-U F2</span>
                        <hr style="margin: 6px 0; border: none; border-top: 1px dashed #FFAEC9;" />
                        "{PERSONAL_INFO['current_status']}"
                    </div>
                    <div style="margin-top: 10px; font-family: 'Space Mono', monospace; font-size: 0.7rem; color: #880E4F; text-align: center;">
                        REF: CSIT349-PORTFOLIO
                    </div>
                </div>
                <div class="phone-keypad">
                    <div class="phone-key">1</div>
                    <div class="phone-key">2</div>
                    <div class="phone-key">3</div>
                    <div class="phone-key">4</div>
                    <div class="phone-key">5</div>
                    <div class="phone-key">6</div>
                    <div class="phone-key">7</div>
                    <div class="phone-key">8</div>
                    <div class="phone-key">9</div>
                    <div class="phone-key">*</div>
                    <div class="phone-key">0</div>
                    <div class="phone-key">#</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("")
        st.markdown("#### Journey Milestones")
        
        # Interactive Milestone Slider (lecture requirement)
        selected_year = st.select_slider(
            "Select Milestone Year:",
            options=["2023", "2024", "2025", "2026"],
            value="2025",
            help="Explore key milestones across academic years"
        )
        
        matching = [m for m in MILESTONES if m["year"] == selected_year]
        for m in matching:
            st.markdown(
                f"""
                <div style="background: #FFFFFF; border: 1.5px solid #FFAEC9; border-left: 4px solid #E0218A; border-radius: 8px; padding: 12px 14px; margin-top: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: baseline;">
                        <span style="font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 800; color: #E0218A;">{m['year']}</span>
                        <span style="font-family: 'Space Mono', monospace; font-size: 0.72rem; font-weight: 700; color: #FFFFFF; background: #C2185B; padding: 2px 8px; border-radius: 4px;">{m['badge']}</span>
                    </div>
                    <div style="font-weight: 800; font-size: 0.95rem; color: #22121E; margin-top: 4px;">{m['title']}</div>
                    <div style="font-size: 0.82rem; color: #666; margin-bottom: 6px;">{m['subtitle']}</div>
                    <div style="font-size: 0.88rem; line-height: 1.5; color: #3D2938;">{m['details']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with st.expander("View Full Chronological History"):
            for m in MILESTONES:
                st.write(f"**{m['year']} — {m['title']}** [{m['badge']}]")
                st.caption(f"{m['details']}")
