import os
from dotenv import load_dotenv

# -------------------------------------------------------
# Load Environment Variables
# -------------------------------------------------------

load_dotenv()

# -------------------------------------------------------
# OpenAI Configuration
# -------------------------------------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHAT_MODEL = "gpt-4o-mini"

TEMPERATURE = 0.2

MAX_TOKENS = 1000

# -------------------------------------------------------
# File Upload Configuration
# -------------------------------------------------------

SUPPORTED_FILE_TYPES = [
    "pdf",
    "txt"
]

MAX_FILE_SIZE = 5 * 1024 * 1024      # 5 MB

# -------------------------------------------------------
# Resume Score Thresholds
# -------------------------------------------------------

EXCELLENT_SCORE = 80

GOOD_SCORE = 60

# -------------------------------------------------------
# Application Information
# -------------------------------------------------------

APP_NAME = "AI Resume Analyzer"

APP_VERSION = "1.0.0"

APP_ICON = "📃"

# -------------------------------------------------------
# Developer Mode
# -------------------------------------------------------

DEVELOPER_MODE = False