import streamlit as st
import re
from data.content import PERSONAL_INFO, BIO_SECTIONS, SKILLS_DATA, PROJECTS_DATA
from utils.helpers import (
    save_feedback,
    get_public_feedback,
    generate_resume_markdown,
    get_image_base64,
)


def render_contact_section():
    """Show contact details and a simple message form."""
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.caption("05 / DEAR AJ")
    st.markdown("## Get In Touch")
    st.write("For project ideas, questions, or collaboration, email me or find me on GitHub.")
    st.caption("The form below saves a note in the app; use the email link for direct contact.")
    
    col_mail, col_info = st.columns([1.35, 1], gap="large")
    
    with col_mail:
        stamp_uri = get_image_base64("assets/images/postage_stamp.svg")
        
        st.markdown(
            f"""
            <div class="stationery-card">
                {f'<img src="{stamp_uri}" class="stationery-stamp-pos" style="width: 80px;" alt="Postage Stamp" />' if stamp_uri else ''}
                <div style="font-size: 0.78rem; font-weight: 700; color: #d94f91;">
                    A NOTE FOR AJ
                </div>
                <h3 style="font-size: 1.5rem; font-weight: 700; color: #352b35; margin: 6px 0 10px 0;">
                    Write me a message
                </h3>
                <p style="font-size: 0.92rem; color: #716873; max-width: 80%; line-height: 1.6; margin-bottom: 20px;">
                    Share a question, project idea, or just say hi.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("")
        
        st.markdown("### Leave a Review or Note")
        with st.form("clean_reader_mail_form", clear_on_submit=False):
            name_input = st.text_input("Your name *", placeholder="What should I call you?").strip()
            email_input = st.text_input("Your email *", placeholder="name@example.com").strip()
            
            topic_option = st.radio(
                "What's on your mind? *",
                options=[
                    "I'd like to work together",
                    "I have a question",
                    "Some feedback",
                    "Just saying hello"
                ],
                index=0
            )
            
            rating_input = st.slider(
                "How was your visit? (1 = not great, 5 = lovely)",
                min_value=1,
                max_value=5,
                value=5
            )
            
            message_input = st.text_area(
                "Your message *",
                placeholder="Write a few words (at least 10 characters).",
                height=130
            ).strip()
            share_publicly = st.checkbox(
                "I consent to sharing my comment with the general public."
            )
            
            submit_btn = st.form_submit_button("Send my note")
            
        if submit_btn:
            errors = []
            if not name_input:
                errors.append("Please add your name.")
            if not email_input:
                errors.append("Please add your email.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
                errors.append("That email address doesn’t look quite right.")
            if not message_input:
                errors.append("Please write a message.")
            elif len(message_input) < 10:
                errors.append("Please write at least 10 characters.")
                
            if errors:
                for err in errors:
                    st.error(err)
            else:
                try:
                    saved = save_feedback(
                        name=name_input,
                        email=email_input,
                        topic=topic_option,
                        message=message_input,
                        rating=rating_input,
                        share_publicly=share_publicly,
                    )
                except OSError:
                    st.error(
                        "Your note could not be saved. Please try again or contact me by email."
                    )
                else:
                    st.toast("Your note was saved.")
                    if share_publicly:
                        st.success(
                            "Your note was saved and will appear in the public reviews below."
                        )
                    else:
                        st.success(
                            "Your note was saved privately. It will not appear in public reviews."
                        )
                    with st.container(border=True):
                        st.caption("NOTE SAVED")
                        st.write(f"Topic · {topic_option}")
                        st.write(f"Rating · {rating_input} / 5")
                        st.caption(f"Saved · {saved['timestamp']}")

    with col_info:
        # Stationery Info Card
        st.markdown(
            f"""
            <div style="background: #FFFFFF; border: 1.5px solid #FFD2E2; border-radius: 16px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
                <div style="font-size: 0.78rem; font-weight: 700; color: #d94f91;">
                    FIND ME
                </div>
                <h4 style="font-size: 1.2rem; color: #352b35; margin: 4px 0 12px 0;">
                    A few details
                </h4>
                <div style="font-size: 0.9rem; line-height: 1.6; color: #3D2938;">
                    <p style="margin-bottom: 8px;"><b>Institution:</b> {PERSONAL_INFO['institution']}</p>
                    <p style="margin-bottom: 8px;"><b>Program:</b> {PERSONAL_INFO['program']}</p>
                    <p style="margin-bottom: 8px;"><b>Section:</b> {PERSONAL_INFO['section']}</p>
                    <p style="margin-bottom: 8px;"><b>Location:</b> {PERSONAL_INFO['location']}</p>
                </div>
                <hr style="border: none; border-top: 1px solid #FFE4EC; margin: 12px 0;" />
                <div style="font-size: 0.78rem; color: #716873;">
                    EMAIL
                </div>
                <a href="mailto:{PERSONAL_INFO['email']}" style="color: #E0218A; font-weight: 700; text-decoration: none; font-size: 0.95rem;">
                    {PERSONAL_INFO['email']}
                </a>
                <hr style="border: none; border-top: 1px solid #FFE4EC; margin: 12px 0;" />
                <div style="font-size: 0.78rem; color: #716873;">
                    FIND ME ON GITHUB:
                </div>
                <a href="{PERSONAL_INFO['github']}" target="_blank" style="color: #E0218A; font-weight: 700; text-decoration: none; font-size: 0.95rem;">
                    github.com/oseyunnn
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.link_button("Email me", url=f"mailto:{PERSONAL_INFO['email']}", use_container_width=True)
        
        st.write("")
        st.markdown("### Want a copy?")
        resume_md = generate_resume_markdown(PERSONAL_INFO, BIO_SECTIONS, SKILLS_DATA, PROJECTS_DATA)
        st.download_button(
            label="Download my portfolio summary",
            data=resume_md,
            file_name="Angela_Jahziel_Encabo_Portfolio.md",
            mime="text/markdown",
            use_container_width=True
        )
        
    public_feedback = get_public_feedback()
    st.markdown("### Public Reviews")
    if public_feedback:
        for entry in reversed(public_feedback):
            with st.container(border=True):
                st.write(f"“{entry['message']}”")
    else:
        st.caption("No public reviews yet.")
