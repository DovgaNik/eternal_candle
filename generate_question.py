import os

from google import genai
from pydantic import BaseModel, Field

import db
import prompt

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

class CandleQuestion(BaseModel):
    idea_inferred: str = Field(
        description="Idea that can be inferred from the random seed, it doesn't have to be the idea of the text itself but it may cause you to think of something that may help generate an interesting question, max 50 words"
    )
    question_explanation: str = Field(
        description="Short explanation of what the question aims to explore, max 50 words"
    )
    question: str = Field(
        description="A Candle-style reflective question, max 25 words."
    )

def generate_random_question():
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt.build_prompt(),
        config={
            "response_mime_type": "application/json",
            "response_json_schema": CandleQuestion.model_json_schema(),
            "temperature": 0.5,
            "top_p": 0.6,
            "top_k": 30,
            "candidate_count": 1,
        },
    )

    text = (response.text or "").strip()
    print(text)

    obj = CandleQuestion.model_validate_json(text)
    question = obj.question
    explanation = obj.question_explanation

    return db.insert_question(
        question_body=question,
        question_explanation=explanation,
    )
