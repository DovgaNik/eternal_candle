import random
import random_string

from typing import List, Optional

categories = [
    "Here & Now – mood, day, current season of life.",
    "Past Moments – memories, turning points, earlier versions of you.",
    "Future & Dreams – hopes, plans, imagined versions of your life.",
    "Everyday Life – routines, habits, small joys and annoyances.",
    "Love & Connection – ways you give, receive, and feel loved.",
    "Tough Stuff – conflict, repair, stress, fears, and resilience.",
    "Play & Adventure – fun, risk, curiosity, and trying new things.",
    "Body & Senses – touch, energy, comfort, and sensory details.",
    "Family & Roots – childhood, family stories, inherited patterns.",
    "Values & Choices – what matters most, lines you won’t cross.",
]

question_types = [
    "Reflection – invite a thoughtful, open answer.",
    "Either-Or – offer a clear choice between two options.",
    "Photo Prompt – ask for a real or imagined photo or scene.",
    "Tiny Challenge – invite them to do something small right now.",
    "Memory Flash – focus on one specific moment from the past.",
    "Future Snapshot – imagine a concrete moment in the future.",
]

tones = [
    "Warm & Gentle – kind, soft, caring.",
    "Light & Playful – curious, a bit silly, easygoing.",
    "Calm & Grounded – simple, steady, reassuring.",
    "Curious & Thoughtful – reflective, honest, open.",
    "Softly Brave – a bit vulnerable, but safe and contained.",
]

mechanics = [
    "Time anchor – mention a clear time (today, this week, ten years from now, etc.).",
    "Sensory lens – highlight a smell, sound, touch, or small visual detail.",
    "Photo mode – imagine or take a photo that answers the question.",
    "List three – ask them to name three small things instead of one big one.",
    "Tiny experiment – invite a tiny action they could actually do today.",
    "Either-or choice – let them pick between two concrete options.",
]


def get_prompt(previous_questions: Optional[List[str]] = None) -> str:
    seed_text = random_string.get_random_paragraph()

    category = random.choice(categories)
    q_form = random.choice(question_types)
    tone = random.choice(tones)
    mechanic = random.choice(mechanics)

    recent_block = ""
    if previous_questions:
        for q in previous_questions[-10:]:
            recent_block += f"- {q}\n"

    prompt = f"""
    You are a creative writer designing ONE question for a couples reflection app (similar in spirit to Candle).

Two partners will answer separately, then see each other's responses. The question must feel warm, clear, and interesting to answer in 1–3 sentences.

### RECENT QUESTIONS (AVOID REPEATING)

Here are some questions you have generated before. Do not reuse their ideas, metaphors, or openings. Aim for a clearly new topic or angle.

<<<PREVIOUS_QUESTIONS_START>>>
{recent_block if recent_block else "(no previous questions in this run)"}
<<<PREVIOUS_QUESTIONS_END>>>

### INPUTS

- Category (WHAT the question is about):
  {category}

- Question form (HOW they answer):
  {q_form}

- Tone (EMOTIONAL COLOR of the question):
  {tone}

- Mechanic / twist (STRUCTURAL constraint):
  {mechanic}

- Romanian literary seed (IDEA SOURCE):
  The text below is a paragraph in Romanian from a story or fairy tale. Read it and extract 1–3 simple ideas (an object, place, feeling, situation):

  <<<ROMANIAN_SEED_START>>>
  {seed_text}
  <<<ROMANIAN_SEED_END>>>

### STYLE & TASK

1. Combine the category, question form, tone, and mechanic into ONE coherent question for a couple.
2. From the Romanian seed, use at least ONE idea, but keep it subtle and natural:
   - For example: a specific object, a small place, a mood, a tiny action.
   - Do **not** copy long phrases or obscure imagery.
3. Write in simple, conversational English:
   - Prefer clear, everyday words over poetic, complex, or archaic phrases.
   - It's okay to include ONE light image or metaphor, but keep it easy to understand.
   - Avoid invented roles or titles like “sentinel”, “secretary of my inner world”, “trumpet call”, etc.
4. Make the question easy and inviting to answer:
   - It should be answerable without overthinking, in 1–3 sentences.
   - It should feel like something you might see in a modern relationship app, not in a literary novel.
5. Ensure DIVERSITY:
   - Avoid classic clichés like “favorite memory”, “first time we met”, or “small rule you broke” unless the seed truly makes it fresh and specific.
   - Vary the opening structure: do **not** always start with “What”, “When”, or “Would you rather”.
   - Make it clearly different in topic, scenario, and phrasing from the recent questions listed above.

### CONSTRAINTS

- Maximum 30 words.
- Exactly ONE question sentence.
- Address the couple, their shared experience, or their individual lives in a way that still makes sense in a couple’s context.
- Natural, emotionally intelligent, modern language — not generic, not overly poetic.
- No meta-text, no bullet points, no explanations.

### OUTPUT

Write ONLY the final question text, nothing else.
    """

    return prompt
