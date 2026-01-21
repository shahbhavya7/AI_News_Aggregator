import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

YOUTUBE_CHANNELS = [
    # "UCn8ujwUInbJkBhffxqAPBVQ", # Dave Ebbelaar
    "UCawZsQWqfGSbCI5yjkdVkTA", # Matthew Berman
]

