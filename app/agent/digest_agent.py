import os
import json
from typing import Optional
import google.generativeai as genai
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


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
        # Configure the Gemini API
        # Make sure you have GOOGLE_API_KEY in your .env file
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # Using gemini-1.5-flash as it is the current standard Flash model. 
        # (gemini-2.5-flash does not exist yet)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.system_prompt = PROMPT

    def generate_digest(self, title: str, content: str, article_type: str) -> Optional[DigestOutput]:
        try:
            # Combine system prompt with user input as Gemini 1.5 usually takes them together comfortably
            # or we can set system_instruction in initialization if preferred, but this works well.
            full_prompt = f"""{self.system_prompt}

TASK: Create a digest for this {article_type}.

Title: {title}
Content: {content[:10000]}
"""

            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                    response_schema=DigestOutput
                )
            )
            
            return DigestOutput.model_validate_json(response.text)
        except Exception as e:
            print(f"Error generating digest: {e}")
            return None

