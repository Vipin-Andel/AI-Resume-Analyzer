def build_prompt(resume_text, job_role=None, job_description=None):
    """
    Build a structured AI prompt for resume analysis.
    """

    role = job_role if job_role else "General Job Applications"

    prompt = f"""
You are a Senior HR Manager, ATS (Applicant Tracking System) Specialist,
Technical Recruiter, and Career Coach with over 15 years of experience.

Your task is to perform a professional resume review exactly as a recruiter would.

Target Job Role:
{role}

Job Description:

{job_description if job_description else "Not Provided"}

Resume:
{resume_text}

Instructions:

- Be honest, constructive, and professional.
- Evaluate the resume as if it were submitted for a real job.
- Give realistic scores.
- Do not always give high scores.
- Explain WHY you gave each score.
- Focus on content quality rather than formatting.
- Use Markdown formatting.
- Do not skip any section.

Return your analysis using the EXACT structure below.

# 📊 Resume Score
Give an overall score out of 100.

Explain why.

---

# 🎯 ATS Score

Give an ATS compatibility score out of 100.

Mention:
- ATS Strengths
- ATS Weaknesses

---

# 📝 Executive Summary

Write a short 4-5 sentence summary.

---

# 💪 Strengths

Provide 5 bullet points.

---

# ⚠️ Areas for Improvement

Provide 5 bullet points.

---

# 🔑 Missing Skills / Keywords

List important missing skills and keywords that should be added for the target role.

---

# 🎯 Resume vs Job Description Match

If a Job Description is provided:

- Estimate the overall match percentage (0-100%).
- List the top matching skills.
- List the important missing skills.
- Explain why the resume matches or does not match the job description.

If no Job Description is provided, state that no comparison could be performed.

# 📁 Project Feedback

Review every project mentioned.

For each project mention:

- What is good
- What can be improved
- What recruiters will think

---

# 👀 Recruiter's First Impression

Imagine you are reviewing this resume for the first time.

Describe your first impression in 3-5 sentences.

---

# 🚀 Action Plan

Provide the TOP 5 improvements in priority order.

Use this format:

Priority 1
...

Priority 2
...

Priority 3
...

Priority 4
...

Priority 5
...
"""

    return prompt


def build_cover_letter_prompt(resume_text, job_role=None, job_description=None):
    """
    Build AI prompt for cover letter generation.
    """

    role = job_role if job_role else "the target position"

    prompt = f"""
You are an expert HR Manager and Professional Career Coach.

Write a professional, personalized cover letter.

Job Role:
{role}

Job Description:
{job_description if job_description else "Not Provided"}

Resume:
{resume_text}

Instructions:

- Keep it professional.
- Keep it between 250-350 words.
- Highlight the candidate's strongest skills.
- Mention relevant projects and experience.
- Match the tone to the target role.
- Do not invent experience not present in the resume.
- Return only the cover letter in Markdown format.
"""

    return prompt

def build_interview_prompt(resume_text, job_role=None):
    """
    Build AI prompt for interview question generation.
    """

    role = job_role if job_role else "the target position"

    prompt = f"""
You are an experienced Technical Interviewer.

Generate interview questions based on the candidate's resume.

Target Role:
{role}

Resume:
{resume_text}

Return the response in Markdown using this structure.

# Technical Questions
Generate 10 technical questions based on the skills mentioned.

# Project Based Questions
Generate 5 project-specific questions.

# HR Questions
Generate 5 behavioral interview questions.

# Bonus Preparation Tips
Give 5 interview preparation tips.
"""

    return prompt