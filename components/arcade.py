import streamlit as st
import os
from data.content import Y2K_ARCHETYPES


def render_arcade_section():
    """Render 05 / THE Y2K LOUNGE: Clean Dev Archetype Quiz and Inspiration Gallery."""
    
    st.markdown(
        """
        <div style="border-bottom: 2.5px solid #E0218A; padding-bottom: 8px; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap;">
            <div>
                <span style="font-family: 'Space Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #E0218A; letter-spacing: 2px;">05 // THE Y2K LOUNGE</span>
                <h2 style="font-family: 'Syne', sans-serif; font-size: 2.2rem; font-weight: 900; color: #22121E; margin: 4px 0 0 0;">
                    Dev Archetype Quiz & Moodboard
                </h2>
            </div>
            <div style="font-family: 'Space Mono', monospace; font-size: 0.82rem; color: #C2185B;">
                BONUS EDITORIAL · PASSION FOR FASHION & CODE
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    tab_quiz, tab_moodboard, tab_mixtape = st.tabs([
        "Developer Archetype Quiz",
        "Visual Inspiration Gallery",
        "2000s Coding Mixtape"
    ])
    
    # ---------------- TAB 1: QUIZ ----------------
    with tab_quiz:
        st.markdown("### Interactive Quiz: Which CIT-U Developer Archetype Are You?")
        st.caption("Answer three questions to discover your technical alignment.")
        
        col_q, col_res = st.columns([1.3, 1], gap="large")
        
        with col_q:
            q1 = st.radio(
                "1. When architecting a new project, what is your top priority?",
                options=[
                    "Solving real human problems and protecting vulnerable users (Visionary Lead)",
                    "Crafting atmospheric game logic, scene trees, and storytelling (Game Architect)",
                    "Building robust tournament-ready code under intense deadlines (Competition Specialist)",
                    "Engineering pixel-perfect layout hierarchy and responsive UI (Interface Stylist)"
                ],
                index=0
            )
            
            q2 = st.radio(
                "2. Your ideal engineering workflow consists of:",
                options=[
                    "Intentional sprint planning and cross-functional leadership (Visionary Lead)",
                    "Iterating game loops, shaders, and dialogue scripts (Game Architect)",
                    "Optimizing algorithm runtimes and rapid hackathon debugging (Competition Specialist)",
                    "Prototyping typography, design tokens, and clean CSS (Interface Stylist)"
                ],
                index=0
            )
            
            q3 = st.radio(
                "3. Which milestone brings the highest satisfaction?",
                options=[
                    "Presenting child digital safety research at a national conference (Visionary Lead)",
                    "Watching players solve anomalies in an indie game jam release (Game Architect)",
                    "Winning a regional runner-up trophy in an esports challenge (Competition Specialist)",
                    "Receiving commendations for clean, elegant software presentation (Interface Stylist)"
                ],
                index=0
            )
            
            calc_btn = st.button("Calculate My Developer Archetype", use_container_width=True)
            
        with col_res:
            if "clean_archetype" not in st.session_state:
                st.session_state.clean_archetype = "Visionary Lead"
                
            if calc_btn:
                votes = {"Visionary Lead": 0, "Game Architect": 0, "Competition Specialist": 0, "Interface Stylist": 0}
                for q in [q1, q2, q3]:
                    if "Visionary Lead" in q: votes["Visionary Lead"] += 1
                    elif "Game Architect" in q: votes["Game Architect"] += 1
                    elif "Competition Specialist" in q: votes["Competition Specialist"] += 1
                    elif "Interface Stylist" in q: votes["Interface Stylist"] += 1
                winner = max(votes, key=votes.get)
                st.session_state.clean_archetype = winner
                st.toast(f"Result computed: {winner}")
                
            arc = Y2K_ARCHETYPES[st.session_state.clean_archetype]
            
            st.markdown(
                f"""
                <div style="background: #FFFFFF; border: 2.5px solid {arc['color']}; border-radius: 16px; padding: 1.5rem; box-shadow: 0 8px 24px rgba(0,0,0,0.06);">
                    <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; font-weight: 700; color: {arc['color']}; letter-spacing: 1px;">
                        RESULT // {arc['badge']}
                    </div>
                    <h4 style="font-family: 'Syne', sans-serif; font-size: 1.35rem; color: #22121E; margin: 6px 0 10px 0;">
                        {arc['title']}
                    </h4>
                    <p style="font-size: 0.92rem; line-height: 1.6; color: #3D2938;">
                        {arc['desc']}
                    </p>
                    <div style="margin-top: 14px; border-top: 1px solid #FFE4EC; padding-top: 10px; font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #666;">
                        MATCH RATING: 100% // CIT-U CS
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    # ---------------- TAB 2: MOODBOARD ----------------
    with tab_moodboard:
        st.markdown("### Visual Inspiration Archive")
        st.caption("Reference materials that established the editorial tone of this portfolio.")
        
        col_img, col_notes = st.columns([1.3, 1], gap="large")
        with col_img:
            mb_path = os.path.join("assets", "images", "identity_moodboard.png")
            if os.path.exists(mb_path):
                st.image(mb_path, caption="Original Identity Moodboard", use_container_width=True)
        with col_notes:
            st.markdown(
                """
                <div style="background: #FFFFFF; border: 1.5px solid #FFD2E2; border-radius: 16px; padding: 1.5rem;">
                    <div style="font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #E0218A;">
                        DESIGN RATIONALE
                    </div>
                    <h4 style="font-family: 'Syne', sans-serif; font-size: 1.25rem; color: #22121E; margin: 4px 0 12px 0;">
                        Intentional Playfulness
                    </h4>
                    <p style="font-size: 0.9rem; line-height: 1.6; color: #444;">
                        Early-2000s design combined structured multimedia layouts with vivid color palettes, 
                        tactile skeuomorphic elements, and personal expression.
                    </p>
                    <p style="font-size: 0.9rem; line-height: 1.6; color: #444;">
                        In this Streamlit application, the same discipline is applied: clean typographical hierarchy, 
                        custom-tuned Altair charts, and modular components demonstrate rigorous technical craft 
                        wrapped in memorable aesthetics.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ---------------- TAB 3: MIXTAPE ----------------
    with tab_mixtape:
        st.markdown("### 2000s Coding Mixtape")
        st.caption("Curated playlist inspiration for late-night programming sessions.")
        
        tracks = [
            {"track": "01. So Good", "artist": "Bratz Rock Angelz", "vibe": "Hackathon Crunch", "year": "2005"},
            {"track": "02. Barbie Girl", "artist": "Aqua", "vibe": "Frontend Styling", "year": "1997"},
            {"track": "03. Toxic", "artist": "Britney Spears", "vibe": "Bug Extermination", "year": "2003"},
            {"track": "04. So Yesterday", "artist": "Hilary Duff", "vibe": "Refactoring Session", "year": "2003"}
        ]
        
        sel = st.selectbox(
            "Select Mixtape Track:",
            options=[f"{t['track']} • {t['artist']}" for t in tracks],
            index=0
        )
        
        curr = next(t for t in tracks if f"{t['track']} • {t['artist']}" == sel)
        
        st.markdown(
            f"""
            <div style="background: #22121E; border: 2px solid #FF85B3; border-radius: 14px; padding: 20px; color: #FFFFFF; max-width: 620px; margin: 12px 0;">
                <div style="display: flex; justify-content: space-between; border-bottom: 1px solid #555; padding-bottom: 8px; font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #FF85B3;">
                    <span>WINAMP AUDIO // DECK 01</span>
                    <span style="background: #E0218A; color: #FFF; padding: 2px 8px; border-radius: 4px;">ACTIVE</span>
                </div>
                <div style="margin-top: 14px;">
                    <div style="font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 800; color: #FFD2E2;">
                        {curr['track']}
                    </div>
                    <div style="font-size: 0.95rem; color: #CCC; margin-top: 2px;">
                        Artist: {curr['artist']} ({curr['year']})
                    </div>
                    <div style="font-size: 0.85rem; color: #FF85B3; margin-top: 4px;">
                        Focus Mode: {curr['vibe']}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
