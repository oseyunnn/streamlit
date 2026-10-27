import streamlit as st
import pandas as pd
import altair as alt
from data.content import SKILLS_DATA, TECH_STACK
from utils.helpers import render_sticker


def render_skills_section():
    """Render 02 / THE SKILL SHEET: Interactive chart, data table, and skill narratives."""
    
    st.markdown(
        """
        <div class="spread-title">
            <span>02 / THE SKILL SHEET: METRICS & TECH STACK</span>
            <span class="spread-category">SELF-ASSESSED SKILLS • 0-100 SCALE</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="font-size: 0.95rem; color: #4A1A32; line-height: 1.6;">
            The ratings below reflect proposed self-assessments on a <b>0–100 scale</b>, balancing core computer science foundations,
            game development architecture, AI system integration, and collaborative leadership.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Filter controls in columns
    col_filter_cat, col_filter_slider = st.columns([1.2, 1.2])
    
    with col_filter_cat:
        categories = ["All Categories"] + sorted(list(set(s["category"] for s in SKILLS_DATA)))
        selected_cat = st.selectbox(
            "Filter by Domain Category:",
            options=categories,
            index=0
        )
        
    with col_filter_slider:
        min_score = st.slider(
            "Minimum Proficiency Rating:",
            min_value=50,
            max_value=90,
            value=65,
            step=5,
            help="Filter competencies based on minimum self-assessment rating"
        )
        
    # Prepare DataFrame
    df = pd.DataFrame(SKILLS_DATA)
    filtered_df = df[df["score"] >= min_score]
    if selected_cat != "All Categories":
        filtered_df = filtered_df[filtered_df["category"] == selected_cat]
        
    # 2 Columns: Chart on Left, Interactive Table on Right
    col_chart, col_table = st.columns([1.3, 1.1], gap="large")
    
    with col_chart:
        st.markdown("#### 📊 Interactive Proficiency Chart")
        if not filtered_df.empty:
            chart = alt.Chart(filtered_df).mark_bar(
                cornerRadiusTopRight=8,
                cornerRadiusBottomRight=8,
                height=24
            ).encode(
                x=alt.X(
                    "score:Q",
                    title="Self-Rating (0 - 100)",
                    scale=alt.Scale(domain=[0, 100])
                ),
                y=alt.Y(
                    "skill:N",
                    sort="-x",
                    title="Competency Area",
                    axis=alt.Axis(labelLimit=200)
                ),
                color=alt.Color(
                    "score:Q",
                    scale=alt.Scale(range=["#FF85B3", "#FF1493", "#D81B60"]),
                    legend=None
                ),
                tooltip=[
                    alt.Tooltip("skill:N", title="Skill"),
                    alt.Tooltip("score:Q", title="Rating"),
                    alt.Tooltip("category:N", title="Category"),
                    alt.Tooltip("description:N", title="Focus")
                ]
            ).properties(
                height=max(220, len(filtered_df) * 40)
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=13
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("No skills match the selected filter criteria.")
            
    with col_table:
        st.markdown("#### 📋 Skills Data Table")
        display_df = filtered_df[["skill", "highlight", "category"]].rename(
            columns={
                "skill": "Competency",
                "highlight": "Rating",
                "category": "Domain"
            }
        )
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )
        
        # Summary pill highlights
        avg_score = filtered_df["score"].mean() if not filtered_df.empty else 0
        top_skill = filtered_df.sort_values(by="score", ascending=False).iloc[0]["skill"] if not filtered_df.empty else "N/A"
        
        st.markdown(
            f"""
            <div style="background: #FFFFFF; border: 2px dashed #FF1493; border-radius: 12px; padding: 12px; margin-top: 10px;">
                <div style="display: flex; justify-content: space-between; font-size: 0.88rem; font-weight: 700; color: #D81B60;">
                    <span>🌟 Top Competency:</span>
                    <span>{top_skill}</span>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.88rem; font-weight: 700; color: #2B1020; margin-top: 4px;">
                    <span>📈 Average Score:</span>
                    <span>{avg_score:.1f} / 100</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Skills in Words - Full Descriptions Grid
    st.write("")
    st.markdown("#### 💬 Skills in Words & Practical Applications")
    
    desc_cols = st.columns(2)
    for i, row in enumerate(filtered_df.itertuples()):
        c = desc_cols[i % 2]
        with c:
            st.markdown(
                f"""
                <div style="background: #FFFFFF; border-left: 3px solid #FF85B3; border-radius: 0 10px 10px 0; padding: 10px 14px; margin-bottom: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                    <div style="font-weight: 800; font-size: 0.95rem; color: #D81B60; display: flex; justify-content: space-between;">
                        <span>{row.skill}</span>
                        <span style="color: #FF1493; font-size: 0.85rem;">{row.highlight}</span>
                    </div>
                    <div style="font-size: 0.86rem; color: #3A1828; margin-top: 4px; line-height: 1.45;">
                        {row.description}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Tech Stack Strip & Interactive Multiselect
    st.write("")
    st.markdown("#### 💄 The Tech Stack Strip")
    
    # Multiselect component from lecture
    all_tech_names = [t["name"] for t in TECH_STACK]
    selected_tech = st.multiselect(
        "Highlight technologies you want to inspect:",
        options=all_tech_names,
        default=["Python", "Godot Engine", "GDScript", "Azure AI Services", "Streamlit"],
        help="Filter the tech wardrobe tags"
    )
    
    # Render interactive tags
    tags_html = '<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px;">'
    for t in TECH_STACK:
        is_highlighted = t["name"] in selected_tech
        border_style = "2px solid #FF1493" if is_highlighted else "1px solid #FFE4EC"
        bg_style = "linear-gradient(135deg, #FF1493, #D81B60)" if is_highlighted else "#FFFFFF"
        text_color = "#FFFFFF" if is_highlighted else "#2B1020"
        shadow = "0 4px 10px rgba(255, 20, 147, 0.35)" if is_highlighted else "none"
        
        tags_html += f"""
        <div style="background: {bg_style}; border: {border_style}; color: {text_color}; padding: 6px 14px; border-radius: 20px; font-size: 0.82rem; font-weight: 700; display: flex; align-items: center; gap: 6px; box-shadow: {shadow};">
            <span>{t['icon']}</span>
            <span>{t['name']}</span>
        </div>
        """
    tags_html += '</div>'
    st.markdown(tags_html, unsafe_allow_html=True)
