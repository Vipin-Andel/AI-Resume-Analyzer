from config import (
    MAX_FILE_SIZE,
    SUPPORTED_FILE_TYPES
)


def validate_uploaded_file(uploaded_file) -> str | None:
    """
    Validate the uploaded resume file.

    Returns:
        None:
            If the file is valid.

        str:
            Error message if validation fails.
    """

    if uploaded_file is None:
        return "Please upload a resume first."

    if uploaded_file.type not in [
        "application/pdf",
        "text/plain"
    ]:
        return "Only PDF and TXT files are supported."

    if uploaded_file.size > MAX_FILE_SIZE:
        return "File size exceeds the 5 MB limit."

    return None
