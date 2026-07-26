import streamlit as st

from openai import (
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APITimeoutError,
    BadRequestError
)


def show_error(message: str) -> None:
    """
    Display an error message.
    """
    st.error(f"❌ {message}")


def show_warning(message: str) -> None:
    """
    Display a warning message.
    """
    st.warning(f"⚠️ {message}")


def show_success(message: str) -> None:
    """
    Display a success message.
    """
    st.success(f"✅ {message}")


def show_info(message: str) -> None:
    """
    Display an informational message.
    """
    st.info(f"ℹ️ {message}")


def handle_api_error(error) -> None:
    """
    Display user-friendly messages for OpenAI API errors.
    """

    if isinstance(error, AuthenticationError):

        show_error("Invalid OpenAI API Key.")
        show_info("Please check your .env file and verify your API key.")

    elif isinstance(error, RateLimitError):

        show_error("OpenAI API quota exceeded.")
        show_info(
            "Enable Developer Mode or add API credits to continue using AI features."
        )

    elif isinstance(error, APIConnectionError):

        show_error("Unable to connect to OpenAI.")
        show_info("Please check your internet connection.")

    elif isinstance(error, APITimeoutError):

        show_error("The request timed out.")
        show_info("Please try again after a few seconds.")

    elif isinstance(error, BadRequestError):

        show_error("Invalid request sent to the AI model.")
        show_info("Please verify the uploaded resume and try again.")

    else:

        show_error("An unexpected error occurred.")
        st.exception(error)