"""
Demo responses used when Developer Mode is enabled.

This allows the application to be tested without consuming
OpenAI API credits.
"""


def get_demo_resume_analysis() -> str:
    """
    Return a sample AI-generated resume analysis.
    """

    return """
# 📊 Resume Score
**88 / 100**

# 🎯 ATS Score
**84 / 100**

# 📝 Summary

This resume demonstrates a solid foundation for a Data Analyst role.
The candidate has relevant technical skills, good project experience,
and a clean resume structure.

---

# 💪 Strengths

- Strong SQL and Python knowledge
- Relevant Power BI projects
- Clear resume formatting
- Good analytical thinking
- Well-organized project section

---

# ⚠️ Areas for Improvement

- Add measurable achievements
- Use stronger action verbs
- Include certifications near the top
- Add GitHub & Portfolio links
- Tailor the resume for each application

---

# 🔑 Missing Skills / Keywords

- Machine Learning
- Statistics
- Azure
- Docker
- Data Warehousing

---

# 🎯 Resume vs Job Description Match

**Overall Match:** **82%**

### Matching Skills

- SQL
- Python
- Power BI
- Excel

### Missing Skills

- Azure
- Machine Learning
- ETL Pipelines

---

# 📁 Project Feedback

Projects are relevant and demonstrate technical capability.

To improve:

- Add business impact.
- Mention datasets used.
- Include measurable outcomes.
- Add GitHub repository links.

---

# 🚀 Action Plan

1. Improve project descriptions.
2. Add quantified achievements.
3. Include GitHub and portfolio links.
4. Highlight certifications.
5. Customize the resume for every job application.
"""


def get_demo_cover_letter() -> str:
    """
    Return a sample AI-generated cover letter.
    """

    return """
# 📄 Cover Letter

Dear Hiring Manager,

I am excited to apply for the Data Analyst position at your organization.

My experience with SQL, Python, Excel, and Power BI has enabled me to build data-driven projects, create insightful dashboards, and solve analytical problems using real-world datasets.

I enjoy transforming raw data into meaningful business insights and continuously improving my technical skills through hands-on projects.

I am confident that my analytical mindset, willingness to learn, and passion for data make me a strong candidate for this role.

Thank you for your time and consideration.

I look forward to the opportunity to discuss how I can contribute to your team.

Sincerely,

**Your Name**
"""


def get_demo_interview_questions() -> str:
    """
    Return sample interview questions.
    """

    return """
# 🎤 Technical Questions

## SQL

1. Explain different types of SQL JOINs.
2. What is the difference between WHERE and HAVING?
3. Explain Window Functions.
4. What are Common Table Expressions (CTEs)?
5. What is normalization?

---

## Python

1. Difference between List and Tuple.
2. Explain Dictionaries.
3. What is Pandas?
4. Explain lambda functions.
5. What are Python decorators?

---

## Power BI

1. What is DAX?
2. Difference between Measure and Calculated Column.
3. Explain Star Schema.
4. What are Relationships?
5. Explain Row-Level Security (RLS).

---

## HR Questions

1. Tell me about yourself.
2. Why should we hire you?
3. Describe a challenging project.
4. What are your strengths and weaknesses?
5. Where do you see yourself in five years?

---

# 🚀 Interview Tips

- Revise SQL fundamentals.
- Practice Python coding daily.
- Know every project in detail.
- Prepare STAR-method answers.
- Practice mock interviews.
"""