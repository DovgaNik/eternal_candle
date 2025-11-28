import os

from google import genai

import generate_question

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

for _ in range(5):
    question_uuid = generate_question.generate_random_question()
