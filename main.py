# main.py

import os
from pathlib import Path

from google import genai
from google.genai.types import GenerateContentConfig

import prompt

QUESTIONS_FILE = Path("data/questions.txt")

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])


def load_recent_questions(limit: int = 50) -> list[str]:
    if not QUESTIONS_FILE.exists():
        return []

    with QUESTIONS_FILE.open("r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        return []

    return lines[-limit:]


def append_questions(new_questions: list[str]) -> None:
    if not new_questions:
        return

    QUESTIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with QUESTIONS_FILE.open("a", encoding="utf-8") as f:
        for q in new_questions:
            q = q.strip()
            if q:
                f.write(q + "\n")


def main():
    previous_questions = load_recent_questions(limit=50)

    generated_now: list[str] = []

    for i in range(5):
        prompt_text = prompt.get_prompt(previous_questions)

        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt_text,
            config=GenerateContentConfig(
                temperature=1.25,
                top_p=0.9,
                top_k=40,
            ),
        )

        q = (response.text or "").strip()
        if not q:
            continue

        print(q)
        generated_now.append(q)
        previous_questions.append(q)

    append_questions(generated_now)


if __name__ == "__main__":
    main()
