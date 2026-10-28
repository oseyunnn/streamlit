import os
import base64
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
CSS_FILE = os.path.join(ASSETS_DIR, "css", "magazine.css")
INBOX_FILE = os.path.join(BASE_DIR, "data", "reader_inbox.json")


def load_css():
    """Load and return the custom Y2K magazine CSS."""
    if os.path.exists(CSS_FILE):
        with open(CSS_FILE, "r", encoding="utf-8") as f:
            return f"<style>{f.read()}</style>"
    return ""


def get_image_base64(relative_path):
    """Convert an image or svg in assets/ to a data-URI string."""
    full_path = os.path.join(BASE_DIR, relative_path)
    if not os.path.exists(full_path):
        return ""
    
    ext = os.path.splitext(full_path)[1].lower().replace(".", "")
    mime = "image/svg+xml" if ext == "svg" else f"image/{ext}"
    if ext == "jpg":
        mime = "image/jpeg"
        
    with open(full_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def render_sticker(image_rel_path, alt="", width="60px", rotate="0deg", extra_class=""):
    """Render an HTML sticker tag with drop-shadow and rotation."""
    uri = get_image_base64(image_rel_path)
    if not uri:
        return ""
    style = f"width: {width}; transform: rotate({rotate}); display: inline-block; filter: drop-shadow(2px 4px 6px rgba(255,20,147,0.35));"
    return f'<img src="{uri}" alt="{alt}" class="y2k-sticker {extra_class}" style="{style}" />'


def save_feedback(name, email, topic, message, rating=None, share_publicly=False):
    """Save user submission to reader_inbox.json."""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": name.strip(),
        "email": email.strip(),
        "topic": topic,
        "message": message.strip(),
        "rating": rating,
        "share_publicly": share_publicly
    }
    
    submissions = []
    if os.path.exists(INBOX_FILE):
        try:
            with open(INBOX_FILE, "r", encoding="utf-8") as f:
                submissions = json.load(f)
        except Exception:
            submissions = []
            
    submissions.append(entry)
    with open(INBOX_FILE, "w", encoding="utf-8") as f:
        json.dump(submissions, f, indent=2, ensure_ascii=False)
    return entry


def get_all_feedback():
    """Retrieve all submitted feedback."""
    if os.path.exists(INBOX_FILE):
        try:
            with open(INBOX_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def get_public_feedback():
    """Return only comments whose authors explicitly consented to public sharing."""
    return [
        {"message": entry["message"]}
        for entry in get_all_feedback()
        if isinstance(entry, dict)
        and entry.get("share_publicly") is True
        and isinstance(entry.get("message"), str)
    ]


def generate_resume_markdown(personal_info, bio_sections, skills, projects):
    """Generate clean downloadable Markdown profile for recruiters / professor."""
    md = f"# {personal_info['title']}\n"
    md += f"**{personal_info['name']}** • {personal_info['program']}\n"
    md += f"*{personal_info['institution']}* • Section: {personal_info['section']}\n\n"
    md += f"**GitHub:** [{personal_info['github']}]({personal_info['github']})\n\n"
    md += "---\n\n"
    
    md += "## Autobiography & Background\n\n"
    for b in bio_sections:
        md += f"### {b['heading']}\n{b['text']}\n\n"
        
    md += "---\n\n"
    md += "## Skill Proficiency Breakdown\n\n"
    md += "| Skill | Self-Rating | Category |\n"
    md += "| :--- | :---: | :--- |\n"
    for s in skills:
        md += f"| {s['skill']} | {s['highlight']} | {s['category']} |\n"
        
    md += "\n---\n\n"
    md += "## Featured Engineering & Game Projects\n\n"
    for p in projects:
        md += f"### {p['title']} ({p['tag']})\n"
        md += f"- **Role:** {p['role']}\n"
        md += f"- **Tech Stack:** {', '.join(p['tools'])}\n"
        md += f"- **Outcome:** {p['outcome']}\n"
        md += f"- **Repository:** {p['link']}\n\n"
        
    return md
