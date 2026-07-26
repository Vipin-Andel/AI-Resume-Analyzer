from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    TEMPERATURE,
    MAX_TOKENS
)

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_ai(prompt: str) -> str:
    """
    Send any prompt to OpenAI and return the generated response.

    Args:
        prompt (str): Prompt to send to the AI model.

    Returns:
        str: AI-generated response.
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced HR Manager, "
                    "ATS Specialist, Career Coach, "
                    "Resume Reviewer, and Technical Interviewer."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    return response.choices[0].message.content.strip()


def analyze_resume(prompt: str) -> str:
    """
    Analyze a resume using AI.
    """
    return ask_ai(prompt)


def generate_cover_letter(prompt: str) -> str:
    """
    Generate a professional cover letter using AI.
    """
    return ask_ai(prompt)


def generate_interview_questions(prompt: str) -> str:
    """
    Generate interview questions based on the resume.
    """
    return ask_ai(prompt)