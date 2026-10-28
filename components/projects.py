import streamlit as st
from data.content import PROJECTS_DATA


def render_projects_section():
    """Render 03 / THE PROJECT CLOSET: Clean Runway & Project Showcase (Inspired by Inspo 2 & 3)."""
    
    st.markdown(
        """
        <div style="border-bottom: 2.5px solid #E0218A; padding-bottom: 8px; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap;">
            <div>
                <span style="font-family: 'Space Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #E0218A; letter-spacing: 2px;">03 // THE PROJECT CLOSET</span>
                <h2 style="font-family: 'Syne', sans-serif; font-size: 2.2rem; font-weight: 900; color: #22121E; margin: 4px 0 0 0;">
                    Project Runway & Code Releases
                </h2>
            </div>
            <div style="font-family: 'Space Mono', monospace; font-size: 0.82rem; color: #C2185B;">
                PORTFOLIO CATALOG · 4 EDITIONS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Character/Project Tab Ribbon (Directly inspired by Image 3 character bar)
    project_names = [f"[{p['number']}] {p['title']}" for p in PROJECTS_DATA]
    selected_proj_label = st.radio(
        "Select Runway Look to Inspect:",
        options=project_names,
        index=0,
        horizontal=True
    )
    
    # Retrieve active project
    active_idx = project_names.index(selected_proj_label)
    p = PROJECTS_DATA[active_idx]
    
    st.write("")
    
    # Spotlight Feature Box
    col_main, col_specs = st.columns([1.3, 1], gap="large")
    
    with col_main:
        tools_tags = "".join([f'<span class="tech-tag-chic">{t}</span>' for t in p["tools"]])
        awards_html = ""
        if p.get("awards"):
            awards_text = " • ".join(p["awards"])
            awards_html = f"""
            <div style="background: #FFF5F8; border-left: 3px solid #E0218A; padding: 10px 14px; border-radius: 0 8px 8px 0; margin: 14px 0;">
                <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; font-weight: 700; color: #E0218A;">COMPETITION RECOGNITION</div>
                <div style="font-weight: 700; font-size: 0.92rem; color: #22121E; margin-top: 2px;">{awards_text}</div>
            </div>
            """
            
        st.markdown(
            f"""
            <div class="project-feature-box">
                <div class="project-badge-pill">{p['number']} // {p['tag']}</div>
                <h3 style="font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 900; color: #22121E; margin: 6px 0;">
                    {p['title']}
                </h3>
                <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 1rem; color: #C2185B; margin-bottom: 12px;">
                    {p['role']}
                </div>
                <div style="font-size: 0.95rem; line-height: 1.65; color: #3D2938; margin-bottom: 14px;">
                    {p['summary']}
                </div>
                <div style="margin-bottom: 10px;">
                    <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; font-weight: 700; color: #666; margin-bottom: 6px;">TECH WARDROBE</div>
                    {tools_tags}
                </div>
                {awards_html}
                <div style="background: #FAFAFA; border: 1px solid #ECECEC; border-radius: 8px; padding: 10px 14px; font-size: 0.88rem; color: #333; margin-top: 10px;">
                    <b>Official Outcome:</b> {p['outcome']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.link_button(
            f"Open {p['title']} GitHub Repository",
            url=p["link"],
            use_container_width=True
        )

    with col_specs:
        st.markdown(
            f"""
            <div style="background: #FFFFFF; border: 1.5px solid #FFD2E2; border-radius: 16px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
                <div style="font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #E0218A; letter-spacing: 1px;">
                    PROJECT RUNWAY DOSSIER
                </div>
                <h4 style="font-family: 'Syne', sans-serif; font-size: 1.25rem; color: #22121E; margin: 4px 0 14px 0;">
                    {p['title']} Specs
                </h4>
                <div style="font-size: 0.86rem; line-height: 1.6; color: #444;">
                    <p><b>Category:</b> {p['category']}</p>
                    <p><b>Lead Role:</b> {p['role']}</p>
                    <p><b>Primary Tools:</b> {', '.join(p['tools'])}</p>
                    <p><b>Verification:</b> Verified code repository on GitHub</p>
                </div>
                <hr style="border: none; border-top: 1px dashed #FFD2E2; margin: 14px 0;" />
                <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; color: #880E4F;">
                    DOCUMENT REF: CSIT349-PROJ-{p['number']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("")
        with st.expander("Explore Technical Architecture Details"):
            st.write(f"**Architecture Overview:** Built utilizing {', '.join(p['tools'])}.")
            st.write(f"**Contribution Context:** Authored as part of {p['role']} within collegiate competition standards.")
            st.write(f"**Repository Access:** [{p['link']}]({p['link']})")

    # Complete 4-Card Runway Grid Below
    st.write("")
    st.markdown("#### Complete Portfolio Runway")
    
    grid_cols = st.columns(2, gap="medium")
    for idx, item in enumerate(PROJECTS_DATA):
        c = grid_cols[idx % 2]
        with c:
            st.markdown(
                f"""
                <div style="background: #FFFFFF; border: 1.5px solid #FFE4EC; border-top: 4px solid {item['accent']}; border-radius: 12px; padding: 14px 16px; margin-bottom: 12px; height: 100%;">
                    <div style="font-family: 'Space Mono', monospace; font-size: 0.7rem; font-weight: 700; color: #888;">{item['number']} // {item['tag']}</div>
                    <div style="font-family: 'Syne', sans-serif; font-size: 1.15rem; font-weight: 800; color: #22121E; margin: 3px 0;">{item['title']}</div>
                    <div style="font-size: 0.85rem; color: #C2185B; font-style: italic; margin-bottom: 8px;">{item['role']}</div>
                    <div style="font-size: 0.88rem; line-height: 1.5; color: #3D2938; margin-bottom: 10px;">{item['summary']}</div>
                    <div style="font-size: 0.82rem; font-weight: 700; color: #22121E;">Outcome: {item['outcome']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.link_button(f"View {item['title']} Repo", url=item["link"], use_container_width=True)
            st.write("")
