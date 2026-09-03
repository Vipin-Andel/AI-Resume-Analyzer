import os
import streamlit as st

from config import (
    OPENAI_API_KEY,
    SUPPORTED_FILE_TYPES,
    APP_NAME,
    APP_ICON,
    APP_VERSION
)

from utils.file_handler import (
    extract_text_from_file,
    get_resume_statistics
)

from utils.prompts import (
    build_prompt,
    build_cover_letter_prompt,
    build_interview_prompt
)

from utils.analyzer import (
    analyze_resume,
    generate_cover_letter,
    generate_interview_questions
)

from utils.error_handler import (
    show_error,
    show_warning,
    show_success,
    handle_api_error
)

from utils.validators import validate_uploaded_file

from utils.score_utils import (
    get_dummy_scores,
    get_score_status
)

from utils.demo_data import (
    get_demo_resume_analysis,
    get_demo_cover_letter,
    get_demo_interview_questions
)

# =====================================================
# Page Config
# =====================================================

LOGO_PATH = "assets/ai_resume_analyzer_logo.png"

st.set_page_config(
    page_title=APP_NAME,
    page_icon=LOGO_PATH if os.path.exists(LOGO_PATH) else APP_ICON,
    layout="centered"
)

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=110)

    st.header(f"{APP_NAME}")

    st.markdown("---")

    st.subheader("Supported Files")

    st.markdown("""
- 📄 PDF
- 📝 TXT
""")

    st.markdown("---")

    st.subheader("AI Model")
    st.info("GPT-4o-mini")

    st.markdown("---")

    st.caption(f"Version {APP_VERSION}")

    st.markdown("---")

    st.subheader("🛠 Developer Options")

    developer_mode = st.toggle(
        "Enable Developer Mode",
        value=False
    )

    if developer_mode:
        st.success("Developer Mode Enabled")
    else:
        st.info("Live AI Mode Enabled")

    st.markdown("---")

    st.subheader("Features")

    st.markdown("""
- 📄 Resume Analysis
- 🎯 ATS Review
- 💼 Project Feedback
- 📄 Cover Letter
- 🚀 Action Plan
""")

# =====================================================
# API Key Check
# =====================================================

if not developer_mode and not OPENAI_API_KEY:
    st.error("❌ OpenAI API Key not found.")
    st.info("Please add your OPENAI_API_KEY to the .env file.")
    st.stop()

# =====================================================
# Main UI
# =====================================================

if os.path.exists(LOGO_PATH):
    col_logo, col_title = st.columns([1, 4])
    with col_logo:
        st.image(LOGO_PATH, width=80)
    with col_title:
        st.title(APP_NAME)
else:
    st.title(f"{APP_ICON} {APP_NAME}")

st.markdown("""
Upload your resume and receive AI-powered feedback.

The analyzer reviews:

- 📄 Resume Quality
- 🎯 ATS Compatibility
- 💼 Projects & Experience
- 🛠 Skills Presentation
- 🚀 Actionable Improvements
""")

uploaded_file = st.file_uploader(
    "Choose a resume (PDF or TXT)",
    type=SUPPORTED_FILE_TYPES
)

# =====================================================
# Resume Information
# =====================================================

if uploaded_file:

    file_size_kb = uploaded_file.size / 1024

    st.subheader("📄 Resume Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("File", uploaded_file.name)

    with col2:
        st.metric(
            "Type",
            uploaded_file.type.split("/")[-1].upper()
        )

    with col3:
        st.metric(
            "Size",
            f"{file_size_kb:.1f} KB"
        )

    st.divider()

# =====================================================
# User Inputs
# =====================================================

job_role = st.text_input(
    "Enter the Job Role (Optional)"
)

st.markdown("### 💼 Job Description (Optional)")

job_description = st.text_area(
    "Paste the Job Description",
    height=180
)

col1, col2, col3 = st.columns(3)

with col1:
    analyze = st.button(
        "📊 Analyze Resume",
        use_container_width=True
    )

with col2:
    generate_letter = st.button(
        "📄 Generate Cover Letter",
        use_container_width=True
    )

with col3:
    interview_questions = st.button(
        "🎤 Interview Questions",
        use_container_width=True
    )

# =====================================================
# Processing
# =====================================================

if analyze or generate_letter or interview_questions:

    validation_error = validate_uploaded_file(uploaded_file)

    if validation_error:
        show_warning(validation_error)
        st.stop()

    try:

        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            show_error("Uploaded file is empty.")
            st.stop()

        stats = get_resume_statistics(file_content)

        # ==========================================
        # Developer Mode
        # ==========================================

        if developer_mode:

            if analyze:

                analysis = get_demo_resume_analysis()
                show_success("Demo Resume Analysis Loaded")

            elif generate_letter:

                analysis = get_demo_cover_letter()
                show_success("Demo Cover Letter Loaded")

            elif interview_questions:

                analysis = get_demo_interview_questions()
                show_success("Demo Interview Questions Loaded")

        # ==========================================
        # Live AI
        # ==========================================

        else:

            if analyze:

                prompt = build_prompt(
                    resume_text=file_content,
                    job_role=job_role,
                    job_description=job_description
                )

                with st.spinner("🤖 AI is analyzing your resume..."):
                    analysis = analyze_resume(prompt)

                show_success("Resume analyzed successfully!")

            elif generate_letter:

                prompt = build_cover_letter_prompt(
                    resume_text=file_content,
                    job_role=job_role,
                    job_description=job_description
                )

                with st.spinner("📄 Generating Cover Letter..."):
                    analysis = generate_cover_letter(prompt)

                show_success("Cover Letter generated successfully!")

            elif interview_questions:

                prompt = build_interview_prompt(
                    resume_text=file_content,
                    job_role=job_role
                )

                with st.spinner("🎤 Generating Interview Questions..."):
                    analysis = generate_interview_questions(prompt)

                show_success("Interview Questions generated successfully!")

        # ==========================================
        # Score Cards (Only for Resume Analysis)
        # ==========================================

        if analyze:

            scores = get_dummy_scores()

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "📊 Resume Score",
                    f"{scores['resume_score']}/100",
                    get_score_status(scores["resume_score"])
                )

            with col2:
                st.metric(
                    "🎯 ATS Score",
                    f"{scores['ats_score']}/100",
                    get_score_status(scores["ats_score"])
                )

            st.divider()

        # ==========================================
        # Resume Statistics (Only for Resume Analysis)
        # ==========================================

        if analyze:

            st.subheader("📊 Resume Statistics")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Words",
                    stats["word_count"]
                )

            with col2:
                st.metric(
                    "Characters",
                    stats["character_count"]
                )

            with col3:
                st.metric(
                    "Reading Time",
                    f"{stats['reading_time']} min"
                )

            st.divider()

        # ==========================================
        # Output
        # ==========================================

        if analyze:
            st.subheader("📋 Resume Analysis")

        elif generate_letter:
            st.subheader("📄 Cover Letter")

        else:
            st.subheader("🎤 Interview Questions")

        st.markdown(analysis)

        st.divider()

        # Download Button

        if analyze:

            download_label = "📥 Download Resume Analysis"
            download_file_name = "resume_analysis.md"

        elif generate_letter:

            download_label = "📥 Download Cover Letter"
            download_file_name = "cover_letter.md"

        else:

            download_label = "📥 Download Interview Questions"
            download_file_name = "interview_questions.md"

        st.download_button(
            label=download_label,
            data=analysis,
            file_name=download_file_name,
            mime="text/markdown",
            use_container_width=True
        )

    except Exception as e:
        handle_api_error(e)

# =====================================================
# CodeHype Launch Badge
# =====================================================

st.markdown("---")
badge_html = """
<div align="center" style="margin-top: 25px; margin-bottom: 25px;">
  <a href="https://codehype.ai/product/ai-resume-analyzer?utm_source=codehype_badge" target="_blank" rel="noopener noreferrer">
    <img src="https://codehype.ai/badges/ai-resume-analyzer.svg?variant=find-us&v=1" alt="Find us on CodeHype" width="380" height="100" style="display:block;border:0;width:100%;max-width:380px;height:auto;" />
  </a>
</div>
"""
st.markdown(badge_html, unsafe_allow_html=True)