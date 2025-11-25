import random
import random_string

from typing import List, Optional

categories = [
    "Romantic Connection – affection, intimacy, how you relate as partners.",
    "Shared Adventures – trips, challenges, things you did together or want to do.",
    "Inner Worlds – thoughts, fears, dreams you rarely say out loud.",
    "Daily Micro-moments – tiny routines, habits, and unnoticed details of the day.",
    "Conflict & Repair – disagreements, apologies, learning to reconnect.",
    "Bodies & Sensations – touch, physical presence, comfort, and embodiment.",
    "Future Visions – plans, hopes, and imagined futures together.",
    "Play & Imagination – games, fantasies, jokes, and creative scenarios.",
    "Values & Ethics – what feels right, important, or non-negotiable to you.",
    "Family & Roots – childhood, parents, origins, and inherited patterns."
]

question_types = [
    "Deep Reflection – invite a thoughtful, detailed answer.",
    "Quick Either-Or – offer a clear choice between two paths.",
    "Photo or Scene Capture – ask them to take or imagine a picture.",
    "Mini-Challenge – propose a small action or experiment.",
    "Memory Snapshot – zoom in on one specific past moment.",
    "Fill-in-the-Blank – short, focused completion of a sentence.",
    "Wild Hypothetical – a ‘what if’ in an unusual scenario.",
    "Ranking or Choice – choose or rank among several options.",
]

tones = [
    "Tender & Warm – gentle, caring, affectionate.",
    "Cheerful & Playful – light, fun, slightly goofy.",
    "Dreamy & Poetic – image-rich, soft, and lyrical.",
    "Grounded & Practical – clear, simple, down-to-earth.",
    "Philosophical & Curious – thoughtful, questioning, zooming out.",
    "Bold & Vulnerable – honest, raw, emotionally brave.",
    "Mischievous & Flirty – teasing, suggestive, charming.",
    "Calm & Soothing – reassuring, slow, peaceful.",
]

mechanics = [
    "Sensory focus – build the question around smell, sound, or texture.",
    "Alternate reality – change one simple rule of the world.",
    "Mini-game – turn the answer into a playful game or rule.",
    "Time travel – anchor the answer to a very specific moment in time.",
    "Object spotlight – revolve around one small, physical object.",
    "Role swap – imagine switching roles, habits, or perspectives.",
    "Map or space – use locations, borders, or imaginary maps.",
    "Secret signal – involve codes, inside jokes, or nonverbal cues.",
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
    You are a creative writer designing one question for a couples reflection app.

    The two partners will answer separately, then see each other's responses. The question must feel fresh, specific, and emotionally meaningful.

    Here are some previous questions that you have generated in the past, do not repeat the ideas or wording of other questions, all the questions must be unique:
    <<<Previous questions begin>>>
    {recent_block}
    <<<Previous questions end>>>

    ### INPUTS

    - Category (WHAT the question is about):
      {category}

    - Question form (HOW they answer):
      {q_form}

    - Tone (EMOTIONAL COLOR of the question):
      {tone}

    - Mechanic / twist (STRUCTURAL constraint):
      {mechanic}

    - Random Romanian literary seed (IDEA SOURCE):
      The following text is a paragraph in Romanian, from a story or fairy tale. Read it and extract 1–3 vivid elements:
      <<<ROMANIAN_SEED_START>>>
      {seed_text}
      <<<ROMANIAN_SEED_END>>>

    ### TASK

    1. Combine the category, form, tone, and mechanic into one coherent question for a couple.
    2. From the Romanian seed, extract specific images, objects, moods, or situations. Use at least ONE idea clearly inspired by the seed (for example: an object, a place, a feeling, a small scene).
    3. Make the question:
       - Written in English.
       - Addressing the couple, their shared experience, or their life or opinion outside the relationship.
       - Aligned with the chosen tone and mechanic (for example, if it’s a mini-game, the question should define the game).
    4. Ensure DIVERSITY:
       - Avoid repeating themes like “favorite memory” or “small rule you broke” unless the seed truly pushes you there in a new way.
       - Vary the opening structure: don’t always start with “What” or “When” or “Would you rather”.
       - Make it feel different in topic, scenario, and phrasing from the recent questions (if any) listed above.

    ### CONSTRAINTS

    - Maximum 30 words.
    - Natural, human, emotionally intelligent language — never generic or robotic.
    - One single question only.
    - No meta-text, no bullet points, no explanations.

    ### OUTPUT

    Write ONLY the final question text, nothing else.
    """

    return prompt
