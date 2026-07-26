import io
import pypdf


def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extract text from a PDF file.
    """

    pdf_reader = pypdf.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_text_from_file(uploaded_file) -> str:
    """
    Extract text from an uploaded PDF or TXT file.
    """

    if uploaded_file.type == "application/pdf":

        return extract_text_from_pdf(
            io.BytesIO(uploaded_file.read())
        )

    return uploaded_file.read().decode("utf-8").strip()


def get_resume_statistics(text: str) -> dict:
    """
    Calculate basic statistics for the resume text.
    """

    words = text.split()

    word_count = len(words)

    character_count = len(text)

    reading_time = max(1, round(word_count / 200))

    line_count = len(text.splitlines())

    return {
        "word_count": word_count,
        "character_count": character_count,
        "line_count": line_count,
        "reading_time": reading_time
    }