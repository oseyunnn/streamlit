import streamlit as st
import os
from data.content import Y2K_ARCHETYPES
from utils.helpers import get_image_base64, render_sticker


def render_arcade_section():
    """Render 05 / Y2K BONUS BOOTH: Interactive Bratz Quiz, Moodboard, and Retro Arcade."""
    
    st.markdown(
        """
        <div class="spread-title">
            <span>05 / THE Y2K LOUNGE: QUIZ & MOODBOARD</span>
            <span class="spread-category">BONUS MAGAZINE EDITORIAL • PASSION FOR FASHION & CODE</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    tab_quiz, tab_moodboard, tab_jukebox = st.tabs([
        "💖 Which Bratz Dev Are You?",
        "📸 The Y2K Inspiration Board",
        "💿 AJ's 2000s Coding Mixtape"
    ])
    
    # ---------------- TAB 1: BRATZ QUIZ ----------------
    with tab_quiz:
        st.markdown("### 👑 Interactive Quiz: Discover Your Y2K Developer Persona!")
        st.caption("Answer 3 quick questions to discover whether you align with Yasmin, Cloe, Sasha, or Jade in tech!")
        
        col_q, col_res = st.columns([1.3, 1.1], gap="large")
        
        with col_q:
            q1 = st.radio(
                "1. When starting a brand-new coding project, what is your first instinct?",
                options=[
                    "Ensure the project solves a real human problem and protects vulnerable users (Yasmin)",
                    "Dream up an emotional storyline, characters, and interactive game worlds (Cloe)",
                    "Set up the Git repo, organize sprint boards, and lead the team to victory (Sasha)",
                    "Craft the neon color palette, CSS micro-animations, and liquid chrome UI (Jade)"
                ],
                index=0
            )
            
            q2 = st.radio(
                "2. Your dream hacking session snack & aesthetic consists of:",
                options=[
                    "Herbal strawberry tea, flower pins, and intentional journaling (Yasmin)",
                    "Pink bubble tea, sketchpad, and indie game lo-fi beats (Cloe)",
                    "Iced espresso, designer blazer, and dual 4K command terminals (Sasha)",
                    "Glitter lip gloss, platform sneakers, and hyperpop remix playlist (Jade)"
                ],
                index=0
            )
            
            q3 = st.radio(
                "3. Which software achievement makes you feel most accomplished?",
                options=[
                    "Receiving feedback that an AI tool kept children safe online (Yasmin)",
                    "Watching players gasp at an unexpected narrative anomaly in a game jam (Cloe)",
                    "Holding a shiny 1st Runner-Up trophy at a national competition (Sasha)",
                    "Having recruiters and users rave about an unforgettable aesthetic UI (Jade)"
                ],
                index=0
            )
            
            calc_button = st.button("✨ Reveal My Bratz Dev Archetype! ✨", use_container_width=True)
            
        with col_res:
            # Determine result
            if "revealed_archetype" not in st.session_state:
                st.session_state.revealed_archetype = "Yasmin"
                
            if calc_button:
                # Count choices
                votes = {"Yasmin": 0, "Cloe": 0, "Sasha": 0, "Jade": 0}
                for q in [q1, q2, q3]:
                    if "Yasmin" in q: votes["Yasmin"] += 1
                    elif "Cloe" in q: votes["Cloe"] += 1
                    elif "Sasha" in q: votes["Sasha"] += 1
                    elif "Jade" in q: votes["Jade"] += 1
                winner = max(votes, key=votes.get)
                st.session_state.revealed_archetype = winner
                st.toast(f"You matched with {winner}! 💖", icon="👑")
                
            archetype = Y2K_ARCHETYPES[st.session_state.revealed_archetype]
            
            st.markdown(
                f"""
                <div class="retro-window" style="border-color: {archetype['color']};">
                    <div class="retro-window-header" style="background: linear-gradient(90deg, {archetype['color']}, #D81B60);">
                        <span>👑 RESULT: {archetype['title'].upper()}</span>
                        <div class="retro-window-controls">
                            <span class="retro-ctrl-btn retro-ctrl-min"></span>
                            <span class="retro-ctrl-btn retro-ctrl-max"></span>
                            <span class="retro-ctrl-btn retro-ctrl-close"></span>
                        </div>
                    </div>
                    <div class="retro-window-body">
                        <div style="font-size: 2.2rem; margin-bottom: 6px;">{archetype['icon']}</div>
                        <h3 style="color: #2B1020; font-family: 'Syne', sans-serif; margin-top: 0;">
                            {archetype['title']}
                        </h3>
                        <p style="font-size: 0.95rem; line-height: 1.6; color: #3A1828;">
                            {archetype['desc']}
                        </p>
                        <div style="margin-top: 14px;">
                            <span class="sticker-pill">Certified Bratz Dev ✨</span>
                            <span class="sticker-pill" style="border-color: #D81B60; color: #D81B60;">CIT-U Approved 💖</span>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    # ---------------- TAB 2: MOODBOARD ----------------
    with tab_moodboard:
        st.markdown("### 📸 The Original Inspiration Board")
        st.caption("The visual DNA that shaped this portfolio: 2000s glitter, Bratz dolls, Barbie pink, and retro Windows XP.")
        
        col_mb1, col_mb2 = st.columns([1.3, 1], gap="large")
        with col_mb1:
            mb_path = os.path.join("assets", "images", "identity_moodboard.png")
            if os.path.exists(mb_path):
                st.image(mb_path, caption="AJ's Original Y2K Identity Moodboard", use_container_width=True)
        with col_mb2:
            st.markdown(
                """
                <div class="retro-window">
                    <div class="retro-window-header">
                        <span>💖 DESIGN_MANIFESTO.TXT</span>
                        <div class="retro-window-controls">
                            <span class="retro-ctrl-btn retro-ctrl-min"></span>
                            <span class="retro-ctrl-btn retro-ctrl-max"></span>
                            <span class="retro-ctrl-btn retro-ctrl-close"></span>
                        </div>
                    </div>
                    <div class="retro-window-body">
                        <h4 style="margin-top: 0; color: #FF1493;">Why Y2K Magazine?</h4>
                        <p style="font-size: 0.9rem; line-height: 1.55; color: #3A1528;">
                            Technology doesn't have to be clinical, cold, or monochromatic gray. 
                            The early 2000s represented an era where personal computing was playful, 
                            expressive, and packed with personality.
                        </p>
                        <p style="font-size: 0.9rem; line-height: 1.55; color: #3A1528;">
                            By infusing <b>Bratz</b> boldness, <b>Barbie</b> vibrant confidence, and 
                            clean responsive Streamlit architecture, this portfolio proves that 
                            rigorous computer science and joyful creative expression belong together!
                        </p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # ---------------- TAB 3: RETRO MIXTAPE ----------------
    with tab_jukebox:
        st.markdown("### 💿 AJ's 2000s Coding Mixtape")
        st.caption("Curated soundtrack for late-night hackathons and Godot game jams.")
        
        tracks = [
            {"track": "01. So Good", "artist": "Bratz Rock Angelz", "vibe": "Hackathon Crunch Energy 🎸", "year": "2005"},
            {"track": "02. Barbie Girl", "artist": "Aqua", "vibe": "Frontend Glitter Mode 💖", "year": "1997"},
            {"track": "03. Toxic", "artist": "Britney Spears", "vibe": "Bug Extermination Groove ⚡", "year": "2003"},
            {"track": "04. So Yesterday", "artist": "Hilary Duff", "vibe": "Refactoring Deprecated Code 💿", "year": "2003"},
            {"track": "05. Complicated", "artist": "Avril Lavigne", "vibe": "Debugging Recursion Anomalies 🛹", "year": "2002"}
        ]
        
        selected_track = st.selectbox(
            "Select Mixtape Track to Play:",
            options=[f"{t['track']} • {t['artist']}" for t in tracks],
            index=0
        )
        
        track_info = next(t for t in tracks if f"{t['track']} • {t['artist']}" == selected_track)
        
        st.markdown(
            f"""
            <div style="background: #2B1020; border: 3px solid #FF85B3; border-radius: 16px; padding: 20px; color: #FFFFFF; max-width: 650px; margin: 10px 0; box-shadow: 0 10px 25px rgba(0,0,0,0.3);">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px dashed #FF85B3; padding-bottom: 8px; margin-bottom: 12px;">
                    <span style="font-family: 'Courier New', monospace; color: #FF85B3; font-weight: 700;">💿 WINAMP V2.91 // AJ_PLAYER</span>
                    <span style="background: #FF1493; padding: 2px 8px; border-radius: 10px; font-size: 0.72rem; font-weight: 800;">PLAYING</span>
                </div>
                <div style="display: flex; gap: 16px; align-items: center;">
                    <div style="font-size: 2.8rem;">🎵</div>
                    <div>
                        <div style="font-family: 'Syne', sans-serif; font-size: 1.3rem; font-weight: 800; color: #FF85B3;">
                            {track_info['track']}
                        </div>
                        <div style="font-size: 0.95rem; color: #E8D7FF;">
                            Artist: <b>{track_info['artist']}</b> ({track_info['year']})
                        </div>
                        <div style="font-size: 0.85rem; color: #FFC1D9; margin-top: 4px;">
                            Mood: <i>{track_info['vibe']}</i>
                        </div>
                    </div>
                </div>
                <div style="margin-top: 16px; background: rgba(255,255,255,0.1); border-radius: 6px; height: 6px; overflow: hidden;">
                    <div style="background: #FF1493; width: 68%; height: 100%;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
