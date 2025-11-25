import random_string
import random

categories = [
    "body awareness",
    "small daily moments",
    "emotional check-in",
    "connection and relationships",
    "self-compassion",
    "energy and pace",
    "transitions and beginnings",
    "comfort and grounding",
    "gentle imagination",
]

question_types = [
    "open-ended",
    "yes/no",
    "choice between two options",
    "imaginative if-prompt",
    "photo prompt",
    "memory recall",
    "future projection",
]

emotional_tones = [
    "calm",
    "warmth",
    "light hope",
    "tired",
    "clarity",
    "soft uncertainty",
    "comfort",
    "reset",
    "neutral",
    "curious"
]

sensory_anchors = [
    "light",
    "warmth",
    "coolness",
    "movement",
    "stillness",
    "sound",
    "quiet",
    "weight",
    "lightness",
    "space",
    "corners",
    "texture",
    "breath",
]

temporal_frames = [
    "right now",
    "today",
    "this week",
    "recently",
    "a past moment",
    "a near future moment",
]

perspectives = [
    "focus on a small detail",
    "keep it gentle",
    "ask about internal experience",
    "ask about physical feeling",
    "ask about something simple",
]


def build_prompt(previous_questions):
    recent_block = ""
    if previous_questions:
        for q in previous_questions[-10:]:
            recent_block += f"- {q}\n"

    prompt = f"""
    You are a question generator inspired by the Candle app.
    
    Follow ALL RULES below:
    
    - Questions must be: short (9–14 words), simple, casual.
    - Use plain English only.
    - No poetic or flowery language.
    - No metaphors beyond basic sensory hints.
    - No heavy, deep, or intense emotions.
    - No long sentences.
    - No repeating or paraphrasing previous questions.
    - Never use the same sentence structure as before.
    - Use the Romanian text ONLY as a randomness seed.
    
    Here is the randomness source (DO NOT reference it directly, however you can use it in order to infer an idea or create a new idea that would be suitable for a question based on the events, actions, words, objects, and ideas etc from the source):
    ROMANIAN_TEXT:
    \"\"\"
    {random_string.get_random_paragraph()}
    \"\"\"
    
    Here are previously generated questions (DO NOT repeat or paraphrase, or use the ideas from the previous questions):
    {recent_block}
    
    Here are your required parameters for the new questions:
    - Category: {random.choice(categories)}
    - Question Type: {random.choice(question_types)}
    - Emotional Tone: {random.choice(emotional_tones)}
    - Sensory Anchor: {random.choice(sensory_anchors)}
    - Temporal Frame: {random.choice(temporal_frames)}
    - Perspective: {random.choice(perspectives)}
    
    - Questions should relate to *real everyday human experiences*, not abstract sensations.
    - Use sensory anchors only as small accents, not as the entire question.
    - Include everyday contexts: mornings, routines, conversations, pauses, choices, time spent alone, small wins, tiny interactions etc.
    - Use parameters as “hints” for mood and direction, NOT literal content.

    Generate 1 NEW Candle-style questions that:
    - follow ALL constraints
    - match the parameters
    - do NOT overlap with previous questions
    - stay natural
    - avoid poetry
    - avoid intensity
    - avoid long or complex phrasing
    
    Output format:
    <question>
    """
    return prompt
