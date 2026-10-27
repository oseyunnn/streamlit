import streamlit as st
from data.content import PROJECTS_DATA
from utils.helpers import render_sticker


def render_projects_section():
    """Render 03 / THE PROJECT CLOSET: Featured engineering and game development projects."""
    
    st.markdown(
        """
        <div class="spread-title">
            <span>03 / THE PROJECT CLOSET: RUNWAY OF CODE</span>
            <span class="spread-category">PORTFOLIO SHOWCASE • 4 EDITIONS</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="font-size: 0.95rem; color: #4A1A32; line-height: 1.6;">
            Step into my project closet! Each piece represents intentional problem-solving, from competitive game development
            with the <b>DOST</b> and <b>UPCSG</b> to AI-assisted child digital safety with <b>IBPAP</b> and <b>Microsoft Azure</b>.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Filter Controls (Radio / Selectbox)
    col_filter_type, col_stat = st.columns([2, 1.2])
    
    with col_filter_type:
        project_categories = ["All Runway Looks", "AI / Safety", "Game Dev", "Systems & Database"]
        selected_category = st.radio(
            "Filter Closet Category:",
            options=project_categories,
            horizontal=True
        )
        
    with col_stat:
        st.markdown(
            """
            <div style="background: #FFE4EC; border: 1.5px solid #FF85B3; border-radius: 12px; padding: 10px; text-align: center;">
                <span style="font-size: 0.8rem; font-weight: 800; color: #D81B60; text-transform: uppercase;">Podium Record</span>
                <div style="font-size: 1.05rem; font-weight: 900; color: #2B1020;">2 Regional Hackathon Titles 🏆</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    # Filter projects list
    if selected_category == "All Runway Looks":
        display_projects = PROJECTS_DATA
    else:
        display_projects = [p for p in PROJECTS_DATA if p["category"] == selected_category]
        
    st.write("")
    
    # Render project cards in a 2-column magazine spread grid
    cols = st.columns(2, gap="medium")
    
    for idx, proj in enumerate(display_projects):
        c = cols[idx % 2]
        with c:
            tools_badges = "".join([f'<span class="sticker-tag">{t}</span>' for t in proj["tools"]])
            award_html = ""
            if proj.get("awards"):
                awards_text = " • ".join(proj["awards"])
                award_html = f'<div class="project-award-box">🏆 <b>Recognition:</b> {awards_text}</div>'
                
            st.markdown(
                f"""
                <div class="project-closet-card" style="border-top-color: {proj['accent']};">
                    <div>
                        <div class="project-tag-badge">{proj['tag']}</div>
                        <h3 class="project-title">{proj['title']}</h3>
                        <div class="project-role">{proj['role']}</div>
                        <div class="project-summary">{proj['summary']}</div>
                        <div style="margin-bottom: 12px;">
                            <span style="font-size: 0.76rem; font-weight: 800; color: #D81B60; text-transform: uppercase;">Tech Wardrobe:</span><br/>
                            <div style="margin-top: 4px;">{tools_badges}</div>
                        </div>
                        {award_html}
                        <div style="font-size: 0.85rem; color: #3A1828; margin-bottom: 14px; background: #FFF9FA; border-left: 3px solid {proj['accent']}; padding: 6px 10px;">
                            <b>Outcome:</b> {proj['outcome']}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Interactive Project Action Bar with clickable Link and Inspector
            col_link, col_inspect = st.columns([1.2, 1])
            with col_link:
                st.link_button(
                    f"🔗 Open {proj['title']} Repo",
                    url=proj["link"],
                    use_container_width=True
                )
            with col_inspect:
                with st.expander("🔍 Deep Dive"):
                    st.write(f"**Architecture & Tools:** {', '.join(proj['tools'])}")
                    st.write(f"**Role Breakdown:** {proj['role']}")
                    st.write(f"**Verification Link:** [{proj['link']}]({proj['link']})")
            st.write("")
