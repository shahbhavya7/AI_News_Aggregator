import os
import logging
from typing import Optional
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv
from app.config import GEMINI_API_KEY, GEMINI_MODEL

load_dotenv()
logger = logging.getLogger(__name__)


class DigestOutput(BaseModel):
    title: str
    summary: str

PROMPT = """You are an expert AI news analyst specializing in summarizing technical articles, research papers, and video content about artificial intelligence.

Your role is to create concise, informative digests that help readers quickly understand the key points and significance of AI-related content.

Guidelines:
- Create a compelling title (5-10 words) that captures the essence of the content
- Write a 2-3 sentence summary that highlights the main points and why they matter
- Focus on actionable insights and implications
- Use clear, accessible language while maintaining technical accuracy
- Avoid marketing fluff - focus on substance"""


class DigestAgent:
    def __init__(self):
        if not GEMINI_API_KEY:
            logger.error("GEMINI_API_KEY not set")
            raise ValueError("GEMINI_API_KEY not found")
            
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL
        self.system_prompt = PROMPT

    def generate_digest(self, title: str, content: str, article_type: str) -> Optional[DigestOutput]:
        try:
            user_prompt = f"""TASK: Create a digest for this {article_type}.

Title: {title}
Content: {content[:10000]}
"""

            response = self.client.models.generate_content(
                model=self.model,
                contents=user_prompt,
                config={
                    'system_instruction': self.system_prompt,
                    'response_mime_type': 'application/json',
                    'response_schema': DigestOutput,
                }
            )
            
            return response.parsed
        except Exception as e:
            logger.error(f"Error generating digest: {e}")
            return None

