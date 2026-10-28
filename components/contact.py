import streamlit as st
import re
from data.content import PERSONAL_INFO, BIO_SECTIONS, SKILLS_DATA, PROJECTS_DATA
from utils.helpers import save_feedback, get_all_feedback, generate_resume_markdown, get_image_base64


def render_contact_section():
    """Render 04 / DEAR AJ: Clean Airmail Stationery & Reader Mail (Inspired by Inspo 3)."""
    
    st.markdown(
        """
        <div style="border-bottom: 2.5px solid #E0218A; padding-bottom: 8px; margin-bottom: 1.5rem; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap;">
            <div>
                <span style="font-family: 'Space Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #E0218A; letter-spacing: 2px;">04 // READER MAIL</span>
                <h2 style="font-family: 'Syne', sans-serif; font-size: 2.2rem; font-weight: 900; color: #22121E; margin: 4px 0 0 0;">
                    Dear AJ...
                </h2>
            </div>
            <div style="font-family: 'Space Mono', monospace; font-size: 0.82rem; color: #C2185B;">
                STATIONERY & COLLABORATIONS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_mail, col_info = st.columns([1.35, 1], gap="large")
    
    with col_mail:
        stamp_uri = get_image_base64("assets/images/postage_stamp.svg")
        
        st.markdown(
            f"""
            <div class="stationery-card">
                {f'<img src="{stamp_uri}" class="stationery-stamp-pos" style="width: 80px;" alt="Postage Stamp" />' if stamp_uri else ''}
                <div style="font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #E0218A; letter-spacing: 1px;">
                    EDITORIAL AIRMAIL // POSTAGE PAID
                </div>
                <h3 style="font-family: 'Playfair Display', serif; font-size: 1.7rem; font-weight: 800; color: #22121E; margin: 6px 0 10px 0;">
                    Leave a Note in My Inbox
                </h3>
                <p style="font-size: 0.92rem; color: #555; max-width: 80%; line-height: 1.5; margin-bottom: 20px;">
                    Have a project inquiry, software collaboration, or feedback on this portfolio? 
                    Submit your message below.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("")
        
        with st.form("clean_reader_mail_form", clear_on_submit=False):
            name_input = st.text_input("Your Name *", placeholder="Enter your full name").strip()
            email_input = st.text_input("Your Email *", placeholder="e.g. name@domain.com").strip()
            
            topic_option = st.radio(
                "Inquiry Category *",
                options=[
                    "Project collaboration",
                    "Questions about my work",
                    "Feedback or just saying hello",
                    "Game Jam & Hackathon Invitation"
                ],
                index=0
            )
            
            rating_input = st.slider(
                "Portfolio Experience Rating (1 to 5 Stars):",
                min_value=1,
                max_value=5,
                value=5
            )
            
            message_input = st.text_area(
                "Your Message *",
                placeholder="Write your note here... (minimum 10 characters)",
                height=130
            ).strip()
            
            submit_btn = st.form_submit_button("Submit Note To AJ's Inbox")
            
        if submit_btn:
            errors = []
            if not name_input:
                errors.append("Please provide your name.")
            if not email_input:
                errors.append("Please provide your email address.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
                errors.append("Please provide a valid email address with an '@' and domain.")
            if not message_input:
                errors.append("Your message cannot be empty.")
            elif len(message_input) < 10:
                errors.append("Please write at least 10 characters in your message.")
                
            if errors:
                for err in errors:
                    st.error(f"Error: {err}")
            else:
                saved = save_feedback(
                    name=name_input,
                    email=email_input,
                    topic=topic_option,
                    message=message_input,
                    rating=rating_input
                )
                
                st.toast("Note delivered to AJ's Inbox.", icon="✉️")
                
                # Suggested success confirmation from user's guide
                st.success(
                    "“Your note is ready! Thanks for stopping by and taking the time to write. "
                    "I'll be in touch if a reply is needed.”"
                )
                
                st.markdown(
                    f"""
                    <div class="mail-receipt-box">
                        <div style="font-family: 'Space Mono', monospace; font-size: 0.72rem; font-weight: 700; color: #E0218A;">
                            DELIVERY RECEIPT // CITU-F2
                        </div>
                        <div style="font-size: 0.88rem; line-height: 1.55; color: #22121E; margin-top: 6px;">
                            <b>Recipient:</b> Angela Jahziel Encabo (CIT-U CS)<br/>
                            <b>Sender:</b> {name_input} ({email_input})<br/>
                            <b>Category:</b> {topic_option}<br/>
                            <b>Rating:</b> {rating_input} / 5 Stars<br/>
                            <b>Timestamp:</b> {saved['timestamp']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    with col_info:
        # Stationery Info Card
        st.markdown(
            f"""
            <div style="background: #FFFFFF; border: 1.5px solid #FFD2E2; border-radius: 16px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
                <div style="font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #E0218A; letter-spacing: 1px;">
                    STUDENT DISPATCH
                </div>
                <h4 style="font-family: 'Syne', sans-serif; font-size: 1.3rem; color: #22121E; margin: 4px 0 12px 0;">
                    Contact & Profiles
                </h4>
                <div style="font-size: 0.9rem; line-height: 1.6; color: #3D2938;">
                    <p style="margin-bottom: 8px;"><b>Institution:</b> {PERSONAL_INFO['institution']}</p>
                    <p style="margin-bottom: 8px;"><b>Program:</b> {PERSONAL_INFO['program']}</p>
                    <p style="margin-bottom: 8px;"><b>Section:</b> {PERSONAL_INFO['section']}</p>
                    <p style="margin-bottom: 8px;"><b>Location:</b> {PERSONAL_INFO['location']}</p>
                </div>
                <hr style="border: none; border-top: 1px solid #FFE4EC; margin: 12px 0;" />
                <div style="font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #666;">
                    OFFICIAL GITHUB:
                </div>
                <a href="{PERSONAL_INFO['github']}" target="_blank" style="color: #E0218A; font-weight: 700; text-decoration: none; font-size: 0.95rem;">
                    github.com/oseyunnn
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("")
        st.markdown("#### Portfolio Spec Sheet")
        resume_md = generate_resume_markdown(PERSONAL_INFO, BIO_SECTIONS, SKILLS_DATA, PROJECTS_DATA)
        st.download_button(
            label="Download AJ's Portfolio Summary (.md)",
            data=resume_md,
            file_name="Angela_Jahziel_Encabo_Portfolio.md",
            mime="text/markdown",
            use_container_width=True
        )
        
        # Feedback archive log
        history = get_all_feedback()
        if history:
            with st.expander(f"View Feedback Ledger ({len(history)} recorded)"):
                for entry in reversed(history[-5:]):
                    st.write(f"**{entry['name']}** ({entry['timestamp']}) — *{entry['topic']}*")
                    st.caption(f"\"{entry['message']}\"")
                    st.divider()
