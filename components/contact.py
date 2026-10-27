import streamlit as st
import re
from data.content import PERSONAL_INFO, BIO_SECTIONS, SKILLS_DATA, PROJECTS_DATA
from utils.helpers import save_feedback, get_all_feedback, generate_resume_markdown, render_sticker


def render_contact_section():
    """Render 04 / READER MAIL: Contact/feedback form with validation and real responses."""
    
    st.markdown(
        """
        <div class="spread-title">
            <span>04 / READER MAIL: DEAR AJ...</span>
            <span class="spread-category">INBOX & COLLABORATIONS • CIT-U CS</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_form, col_links = st.columns([1.4, 1], gap="large")
    
    with col_form:
        st.markdown(
            """
            <div class="reader-mail-container">
                <div class="reader-mail-header">Dear AJ... 💌</div>
                <div class="reader-mail-sub">
                    Have a project idea, want to collaborate on game dev or AI safety, or just want to say hello? 
                    Leave a little note in my inbox below!
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("")
        
        # Streamlit Form Component with real submission state
        with st.form("reader_mail_form", clear_on_submit=False):
            name_input = st.text_input("Your Name *", placeholder="e.g. Cher Horowitz / Professor").strip()
            email_input = st.text_input("Your Email *", placeholder="e.g. cher@clueless.org").strip()
            
            topic_option = st.radio(
                "What's this about? *",
                options=[
                    "Project collaboration",
                    "Questions about my work",
                    "Feedback or just saying hello",
                    "Game Jam & Hackathon Invitation"
                ],
                index=0
            )
            
            vibe_rating = st.slider(
                "Rate AJ's World Magazine Vibe ✨",
                min_value=1,
                max_value=5,
                value=5,
                format="%d ⭐"
            )
            
            message_input = st.text_area(
                "Your Message *",
                placeholder="Write your note here... Tell me about your ideas, feedback, or inquiries!",
                height=140
            ).strip()
            
            submit_button = st.form_submit_button("💌 Send Note To AJ's Inbox")
            
        # Form Validation and Submission Processing
        if submit_button:
            errors = []
            if not name_input:
                errors.append("Please provide your name.")
            if not email_input:
                errors.append("Please provide your email address.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
                errors.append("Please enter a valid email address with an '@' and domain.")
            if not message_input:
                errors.append("Your message cannot be empty. Please leave a short note!")
            elif len(message_input) < 10:
                errors.append("Your message is a bit short. Please write at least 10 characters.")
                
            if errors:
                for err in errors:
                    st.error(f"⚠️ {err}")
            else:
                # Save submission to local storage
                saved_entry = save_feedback(
                    name=name_input,
                    email=email_input,
                    topic=topic_option,
                    message=message_input,
                    rating=vibe_rating
                )
                
                # Visual celebration extras
                st.balloons()
                st.toast("💌 Note sent successfully to AJ's Inbox!", icon="💖")
                
                # Suggested success message from user's guide
                st.success(
                    "✨ **“Your note is ready! Thanks for stopping by and taking the time to write. "
                    "I'll be in touch if a reply is needed.”**"
                )
                
                st.markdown(
                    f"""
                    <div style="background: #FFFFFF; border: 2px solid #FF85B3; border-radius: 12px; padding: 14px; margin-top: 10px;">
                        <span style="font-weight: 800; color: #D81B60; font-size: 0.85rem; text-transform: uppercase;">Sent Receipt:</span>
                        <div style="font-size: 0.9rem; color: #2B1020; margin-top: 4px;">
                            <b>To:</b> Angela Jahziel Encabo (CIT-U CS • Section F2)<br/>
                            <b>From:</b> {name_input} ({email_input})<br/>
                            <b>Topic:</b> {topic_option}<br/>
                            <b>Vibe:</b> {'⭐' * vibe_rating}<br/>
                            <b>Timestamp:</b> {saved_entry['timestamp']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    with col_links:
        # Retro Window Card: Quick Links & Contact Details
        st.markdown(
            f"""
            <div class="retro-window">
                <div class="retro-window-header">
                    <span>📫 AJ_CONNECT.EXE</span>
                    <div class="retro-window-controls">
                        <span class="retro-ctrl-btn retro-ctrl-min"></span>
                        <span class="retro-ctrl-btn retro-ctrl-max"></span>
                        <span class="retro-ctrl-btn retro-ctrl-close"></span>
                    </div>
                </div>
                <div class="retro-window-body">
                    <h4 style="margin-top: 0; color: #D81B60; font-family: 'Syne', sans-serif;">Connect With Me</h4>
                    <p style="font-size: 0.9rem; line-height: 1.5; color: #3E1E31;">
                        Whether you are an engineer, fellow student, professor, or recruiter, 
                        I'm always excited to discuss software systems, game dev, and AI safety!
                    </p>
                    <div style="margin-top: 12px;">
                        <span class="sticker-tag">🐙 GitHub</span>
                        <a href="{PERSONAL_INFO['github']}" target="_blank" style="color: #FF1493; font-weight: 700; text-decoration: none; font-size: 0.9rem;">
                            github.com/oseyunnn
                        </a>
                    </div>
                    <div style="margin-top: 8px;">
                        <span class="sticker-tag">🎓 Student Profile</span>
                        <span style="color: #2B1020; font-size: 0.88rem; font-weight: 600;">CIT-U • Section F2</span>
                    </div>
                    <div style="margin-top: 8px;">
                        <span class="sticker-tag">📍 Location</span>
                        <span style="color: #2B1020; font-size: 0.88rem; font-weight: 600;">Cebu City, Philippines</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Download Button extra for resume / portfolio summary
        st.write("")
        st.markdown("#### 📄 Developer Resume & Spec Sheet")
        resume_md = generate_resume_markdown(PERSONAL_INFO, BIO_SECTIONS, SKILLS_DATA, PROJECTS_DATA)
        st.download_button(
            label="💖 Download AJ's Portfolio Summary (.md)",
            data=resume_md,
            file_name="Angela_Jahziel_Encabo_Portfolio_Summary.md",
            mime="text/markdown",
            use_container_width=True
        )
        
        # Feedback archive expander
        existing_notes = get_all_feedback()
        if existing_notes:
            with st.expander(f"📬 View Inbox Log ({len(existing_notes)} notes recorded)"):
                for n in reversed(existing_notes[-5:]):
                    st.write(f"**{n['name']}** ({n['timestamp']}) — *{n['topic']}*")
                    st.caption(f"\"{n['message']}\"")
                    st.divider()
