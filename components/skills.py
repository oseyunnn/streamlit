import streamlit as st
import pandas as pd
import altair as alt
from data.content import SKILLS_DATA, TECH_STACK


def render_skills_section():
    """Render 02 / THE SKILL SHEET: Clean Dreamhouse Infographic (Inspired by Inspo 1)."""
    
    st.markdown(
        """
        <div style="border-bottom: 2.5px solid #68C7B5; padding-bottom: 8px; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap;">
            <div>
                <span style="font-family: 'Space Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #68C7B5; letter-spacing: 2px;">02 // THE SKILL SHEET</span>
                <h2 style="font-family: 'Syne', sans-serif; font-size: 2.2rem; font-weight: 900; color: #22121E; margin: 4px 0 0 0;">
                    Skills & Tech Stack Blueprint
                </h2>
            </div>
            <div style="font-family: 'Space Mono', monospace; font-size: 0.82rem; color: #C2185B;">
                DREAMHOUSE INFOGRAPHIC · 0-100 METRICS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Outer Dreamhouse Mint Teal Container
    st.markdown(
        """
        <div class="dreamhouse-roof">
            <span class="dreamhouse-roof-badge">THE CS DREAMHOUSE BLUEPRINT</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Filter Controls in Clean Room Container
    ctrl_col1, ctrl_col2 = st.columns([1.2, 1.2])
    with ctrl_col1:
        categories = ["All Categories"] + sorted(list(set(s["category"] for s in SKILLS_DATA)))
        selected_cat = st.selectbox(
            "Filter Competency Domain:",
            options=categories,
            index=0
        )
    with ctrl_col2:
        min_score = st.slider(
            "Minimum Score Threshold:",
            min_value=50,
            max_value=90,
            value=65,
            step=5,
            help="Filter competencies by self-assessed rating threshold"
        )
        
    # Prepare DataFrame
    df = pd.DataFrame(SKILLS_DATA)
    filtered_df = df[df["score"] >= min_score]
    if selected_cat != "All Categories":
        filtered_df = filtered_df[filtered_df["category"] == selected_cat]
        
    st.write("")
    
    # 2 Room Columns: Left Chart Room (Lipstick Bar Chart Style), Right Room (Data Table & Stats)
    room_col1, room_col2 = st.columns([1.35, 1.1], gap="medium")
    
    with room_col1:
        st.markdown(
            """
            <div class="dreamhouse-room-title">
                <span>Her Success // Proficiency Bars</span>
                <span class="dreamhouse-room-tag">ALTAIR METRIC</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if not filtered_df.empty:
            # Rounded lipstick/bullet-top horizontal bar chart
            chart = alt.Chart(filtered_df).mark_bar(
                cornerRadiusTopRight=10,
                cornerRadiusBottomRight=10,
                height=26
            ).encode(
                x=alt.X(
                    "score:Q",
                    title="Self-Assessment Score (0 - 100)",
                    scale=alt.Scale(domain=[0, 100])
                ),
                y=alt.Y(
                    "skill:N",
                    sort="-x",
                    title="Competency",
                    axis=alt.Axis(labelLimit=200, labelFont="Outfit", labelFontSize=12)
                ),
                color=alt.Color(
                    "score:Q",
                    scale=alt.Scale(
                        range=["#FF85B3", "#E0218A", "#C2185B"]
                    ),
                    legend=None
                ),
                tooltip=[
                    alt.Tooltip("skill:N", title="Skill"),
                    alt.Tooltip("score:Q", title="Rating"),
                    alt.Tooltip("category:N", title="Domain"),
                    alt.Tooltip("description:N", title="Application")
                ]
            ).properties(
                height=max(240, len(filtered_df) * 44)
            ).configure_axis(
                gridColor="#FCE4EC",
                tickColor="#FFAEC9"
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("No competencies match the current filter selection.")
            
    with room_col2:
        st.markdown(
            """
            <div class="dreamhouse-room-title">
                <span>Data Ledger & Stats</span>
                <span class="dreamhouse-room-tag">DATA TABLE</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        display_df = filtered_df[["skill", "highlight", "category"]].rename(
            columns={
                "skill": "Competency",
                "highlight": "Score",
                "category": "Domain"
            }
        )
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # Summary metrics
        avg_score = filtered_df["score"].mean() if not filtered_df.empty else 0
        top_skill = filtered_df.sort_values(by="score", ascending=False).iloc[0]["skill"] if not filtered_df.empty else "N/A"
        
        st.markdown(
            f"""
            <div style="background: #FFF5F8; border: 1.5px solid #FFD2E2; border-radius: 12px; padding: 12px; margin-top: 14px;">
                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 700; color: #C2185B;">
                    <span>TOP COMPETENCY:</span>
                    <span style="color: #22121E;">{top_skill}</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-weight: 700; color: #C2185B; margin-top: 6px;">
                    <span>DOMAIN AVERAGE:</span>
                    <span style="color: #22121E;">{avg_score:.1f} / 100</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Room: Skills in Words
    st.write("")
    st.markdown(
        """
        <div class="dreamhouse-room-title" style="margin-top: 1.5rem;">
            <span>Her Influence // Skills in Words</span>
            <span class="dreamhouse-room-tag">DESCRIPTIONS</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    desc_cols = st.columns(2)
    for idx, row in enumerate(filtered_df.itertuples()):
        c = desc_cols[idx % 2]
        with c:
            st.markdown(
                f"""
                <div style="background: #FFFFFF; border: 1px solid #FFE4EC; border-left: 3.5px solid #68C7B5; border-radius: 6px; padding: 10px 14px; margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; font-weight: 800; font-size: 0.92rem; color: #22121E;">
                        <span>{row.skill}</span>
                        <span style="color: #E0218A; font-family: 'Space Mono', monospace; font-size: 0.82rem;">{row.highlight}</span>
                    </div>
                    <div style="font-size: 0.86rem; color: #4A2838; margin-top: 4px; line-height: 1.45;">
                        {row.description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Bottom Room: Tech Wardrobe
    st.write("")
    st.markdown(
        """
        <div class="dreamhouse-room-title" style="margin-top: 1.2rem;">
            <span>The Tech Wardrobe // Stack Inspector</span>
            <span class="dreamhouse-room-tag">ACTIVE TOOLS</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    all_tech = [t["name"] for t in TECH_STACK]
    selected_tech = st.multiselect(
        "Filter and inspect technologies in the portfolio wardrobe:",
        options=all_tech,
        default=["Python", "Godot Engine", "GDScript", "Microsoft Azure AI", "Streamlit"]
    )
    
    tags_html = '<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">'
    for t in TECH_STACK:
        is_sel = t["name"] in selected_tech
        bg = "#E0218A" if is_sel else "#FFFFFF"
        color = "#FFFFFF" if is_sel else "#22121E"
        border = "2px solid #E0218A" if is_sel else "1.5px solid #FFD2E2"
        tags_html += f"""
        <div style="background: {bg}; color: {color}; border: {border}; padding: 6px 14px; border-radius: 8px; font-family: 'Space Mono', monospace; font-size: 0.78rem; font-weight: 700;">
            [{t['category'].upper()}] {t['name']}
        </div>
        """
    tags_html += '</div>'
    st.markdown(tags_html, unsafe_allow_html=True)
