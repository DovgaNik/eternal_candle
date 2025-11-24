# IMPORTS

import os # for the api key in env
import random
import string

# GCP imports
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig

import prompt

# INIT gemini
client = genai.Client(
    api_key=os.environ['GEMINI_API_KEY']
)

for i in range(10):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt.get_prompt(50),
        config=GenerateContentConfig(
            temperature=1.1,
            #top_p=0.9,
            #top_k=50,
            #thinking_config=types.ThinkingConfig(thinking_budget=0),
            #max_output_tokens=128,
        )
    )

    print(response.text)
