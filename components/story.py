import streamlit as st
from data.content import BIO_SECTIONS, MILESTONES, PERSONAL_INFO


def render_story_section():
    """Share a little background and a few milestones."""
    st.markdown('<div id="story"></div>', unsafe_allow_html=True)
    st.caption("02 / THE STORY")
    st.markdown("## My Story")
    st.write("A few things that shaped how I learn, work, and build.")
    
    col_narrative, col_widget = st.columns([1.35, 1], gap="large")
    
    with col_narrative:
        for sec in BIO_SECTIONS:
            with st.container(border=True):
                st.caption(sec["tag"].title())
                st.markdown(f"### {sec['heading']}")
                st.write(sec["text"])
            
    with col_widget:
        st.markdown(
            f"""
            <div class="y2k-phone-widget">
                <div class="phone-antenna"></div>
                <div class="phone-screen">
                    <div class="phone-status-bar">
                        <span>AJ's notes</span>
                        <span>online</span>
                    </div>
                    <div style="text-align: center; margin: 10px 0 6px 0;">
                        <span style="font-size: 0.76rem; font-weight: 700; color: #d94f91; background: #FFF; padding: 2px 8px; border-radius: 8px; border: 1px solid #f0d7e3;">
                            A Quick Update
                        </span>
                    </div>
                    <div style="background: #FFFFFF; border: 1.5px solid #FF85B3; border-radius: 12px; padding: 12px; font-size: 0.85rem; line-height: 1.5; color: #22121E; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
                        <b>From AJ</b><br/>
                        <span style="color: #666; font-size: 0.72rem;">A note to self</span>
                        <hr style="margin: 6px 0; border: none; border-top: 1px dashed #FFAEC9;" />
                        "{PERSONAL_INFO['current_status']}"
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
        st.markdown("### A Few Milestones · 2024–Present")
        
        selected_year = st.select_slider(
            "Pick a year",
            options=["2024", "2025", "2026 · Present"],
            value="2026 · Present",
            help="Move through my school and project milestones."
        )
        
        selected_year_value = selected_year[:4]
        matching = [m for m in MILESTONES if m["year"] == selected_year_value]
        for m in matching:
            with st.container(border=True):
                st.caption(f"{m['year']} · {m['badge']}")
                st.markdown(f"**{m['title']}**")
                st.caption(m["subtitle"])
                st.write(m["details"])
            
        with st.expander("See all milestones"):
            for m in MILESTONES:
                st.write(f"**{m['year']} — {m['title']}** [{m['badge']}]")
                st.caption(f"{m['details']}")
