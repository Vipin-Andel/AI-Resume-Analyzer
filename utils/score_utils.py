from config import (
    EXCELLENT_SCORE,
    GOOD_SCORE
)


def get_score_status(score: int) -> str:
    """
    Return a score category based on the score value.
    """

    if score >= EXCELLENT_SCORE:
        return "Excellent"

    if score >= GOOD_SCORE:
        return "Good"

    return "Needs Improvement"


def get_score_icon(score: int) -> str:
    """
    Return an emoji representing the score.
    """

    if score >= EXCELLENT_SCORE:
        return "🟢"

    if score >= GOOD_SCORE:
        return "🟡"

    return "🔴"


def get_dummy_scores() -> dict:
    """
    Demo scores used when Developer Mode is enabled.

    This function will later be replaced by real AI-generated
    scores once JSON parsing is implemented.
    """

    return {
        "resume_score": 88,
        "ats_score": 82
    }


def get_score_color(score: int) -> str:
    """
    Return a color name based on the score.
    Useful for future charts and dashboards.
    """

    if score >= EXCELLENT_SCORE:
        return "green"

    if score >= GOOD_SCORE:
        return "orange"

    return "red"