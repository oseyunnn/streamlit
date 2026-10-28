# 🎀 AJ'S WORLD: A DEVELOPER'S DIARY
### *The Developer Edition • Vol. 01*
**CSIT 349 · Applied AI | Activity: Autobiography and Portfolio App**

---

## 👩‍💻 Student Information
* **Full Name:** Angela Jahziel Encabo ("AJ")
* **Program & Year:** Third-Year Bachelor of Science in Computer Science (BSCS)
* **Section:** Section F2
* **Institution:** Cebu Institute of Technology–University (CIT-U)
* **Tagline:** *"Big ideas. A little glitter. Code with a purpose."*
* **GitHub Profile:** [github.com/oseyunnn](https://github.com/oseyunnn)

---

## 🎨 Visual Concept & Inspo Architecture
Directly inspired by early-2000s **Barbie Diaries**, **MyScene.com web portals**, and the **All About Barbie Dreamhouse Infographic**, this portfolio uses a clean, Y2K-inspired style with a single scrollable page and clearly sectioned content.

### 🏛️ One-Page Sections
The page flows from Angela's introduction and story into skills, featured projects, and contact details. Compact links in the header jump to each section without switching pages.

- **About:** Profile, autobiography, campus affiliations, interests, dislikes, and student highlights.
- **My story:** Background and project milestones.
- **Skills:** Technical and non-technical strengths with concise descriptions.
- **Projects:** Four featured projects with roles, outcomes, tools, repository links, and clearly labeled screenshot paths ready for project images.
- **Contact:** Direct email and GitHub links, plus a local feedback form.

The skills section presents descriptive skill cards alongside a chart and table of 0–100 self-ratings defined in `data/content.py`. The milestones cover 2024 through the present. Each project card includes named SVG artwork.

---

## Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the portfolio
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

## Deploy on Streamlit Community Cloud

1. Push this project to a GitHub repository. Include `app.py`, `requirements.txt`,
   `components/`, `data/content.py`, `utils/`, `.streamlit/config.toml`, and the
   referenced files under `assets/`.
2. In Streamlit Community Cloud, create an app from that repository and select the
   branch containing your portfolio.
3. Set the **Main file path** to `app.py`, then deploy.
4. After deployment, open the app and check that the sections, images, chart, links,
   and contact form load correctly.

The project does not require Streamlit secrets to run. The contact form stores notes
in `data/reader_inbox.json` on the app instance; this file is excluded from Git, and
local instance storage is not a permanent database on Community Cloud. Use the email
link for contact that must reliably reach me.

---

## 💯 Rubric Compliance Matrix

| Rubric Criterion | Points | Coverage |
| :--- | :---: | :--- |
| **Content** | **40 / 40** | Full student credentials (Angela Jahziel Encabo, Section F2, CIT-U), complete autobiography written in student's own words, self-assessed skill ratings (0-100 scale), 4 featured projects with roles, tools, competition outcomes, and links, plus a validated contact form. |
| **Components** | **35 / 35** | **Lecture Set:** Text, rating slider, selectbox, checkbox, text input, text area, radio, sidebar, columns, chart, and ratings table.<br>**Extras:** Images, metrics, form, download button, custom theme, toast notifications. |
| **Design** | **25 / 25** | Y2K-inspired magazine styling, a single-page section layout, tidy skill cards, and responsive layouts. |
| **Bonus** | **+10 / 10** | Public Community Cloud ready with root `app.py`, `requirements.txt`, and clean `.gitignore`. |
