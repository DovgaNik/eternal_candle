import os

from google import genai
from pydantic import BaseModel, Field

import db
import prompt

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])


class CandleQuestion(BaseModel):
    question_explanation: str = Field(
        description="Short explanation of what the question aims to explore."
    )
    question: str = Field(
        description="A Candle-style reflective question, max 25 words."
    )


for i in range(5):
    for _ in range(5):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt.build_prompt(),
            config={
                "response_mime_type": "application/json",
                "response_json_schema": CandleQuestion.model_json_schema(),
            },
        )

        text = (response.text or "").strip()
        print(text)

        obj = CandleQuestion.model_validate_json(text)
        question = obj.question
        explanation = obj.question_explanation

        db.insert_question(
            question_body=question,
            question_explanation=explanation,
        )
