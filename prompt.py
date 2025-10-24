import random

import random_string

categories = [
    "Relationship & Love – About connection, affection, communication, or growth between partners.",
    "Personal Growth – Exploring identity, change, goals, or lessons learned.",
    "Friendship & Social Bonds – About friends, community, belonging, or shared memories.",
    "Family & Childhood – Roots, upbringing, parents, nostalgia, or family dynamics.",
    "Fun & Playful – Lighthearted, imaginative, or silly 'what-if' scenarios.",
    "Life & Purpose – Meaning, direction, ambition, or reflection on existence.",
    "Creativity & Expression – Art, inspiration, storytelling, and personal creation.",
    "Mind & Emotions – Feelings, self-awareness, fears, hopes, mental wellbeing.",
    "Daily Life & Habits – Everyday routines, comfort, small pleasures, productivity.",
    "Nature & The World – The environment, travel, awe, simplicity, or grounding.",
    "Time & Memory – Past vs. future, nostalgia, life stages, transformation.",
    "Sensory & Aesthetic – Beauty, colors, sounds, textures, and sensory awareness.",
    "Technology & Future – Digital life, innovation, AI, or how the world is changing.",
    "Philosophy & Wonder – Big ideas, paradoxes, curiosity, or perspective shifts.",
    "Culture & Society – Human diversity, identity, traditions, and shared experiences.",
    "Play & Imagination – Creative fantasies, 'make-believe,' or thought experiments.",
    "Self & Identity – Understanding who we are and how we see ourselves.",
    "Change & Resilience – Adapting, overcoming, and learning from challenges.",
    "Joy & Gratitude – Appreciation, happiness, and noticing small miracles.",
    "Dreams & Aspirations – Vision, hope, and long-term personal or shared dreams."
]

question_types = [
    "Open-Ended – Invites storytelling, reflection, or detailed answers.",
    "Example: 'What is something that has quietly shaped who you are today?'",
    "Yes/No (or Either/Or) – Quick contrast, but still meaningful.",
    "Example: 'Would you rather explore space or the deep ocean — and why?'",
    "Photo / Visual Prompt – Encourages a picture, scene, or creative act.",
    "Example: 'Take a photo of something that calms your mind instantly.'",
    "Choice / Ranking – Small decision or preference that reveals personality.",
    "Example: 'Which feels more like home to you right now — routine or adventure?'",
    "Fill-in-the-Blank – Short, expressive responses, often poetic or emotional.",
    "Example: 'Right now, I feel most alive when ______.'",
    "Memory Recall – Triggering a specific moment or past experience.",
    "Example: 'What’s a small moment from years ago that still makes you smile?'",
    "Action / Challenge – Invite the user to do something reflective or creative.",
    "Example: 'Send a message to someone you’ve been thinking about lately.'"
]

tones = [
    "Deep / Introspective – Serious, thoughtful, exploring meaning or emotion.",
    "'What part of yourself do you keep most private, and why?'",
    "Playful / Curious – Light, fun, full of imagination or gentle humor.",
    "'If our thoughts had colors, what shade would yours be today?'",
    "Flirty / Romantic – Warm, intimate, expressive of affection or attraction.",
    "'What’s something small I do that secretly makes you smile?'",
    "Reflective / Nostalgic – Looking back with emotion or gratitude.",
    "'What’s a moment from the past that you’d love to relive for a day?'",
    "Poetic / Sensory – Using imagery, beauty, or feeling to evoke emotion.",
    "'What sound feels like comfort to you?'",
    "Philosophical / Abstract – Big ideas, paradoxes, or imaginative thought.",
    "'Do you think we become who we are, or do we remember who we’ve always been?'",
    "Whimsical / Surreal – Dreamlike, creative, unexpected.",
    "'If you could open a door to another version of your life, what would you see?'",
    "Grounded / Practical – Simple, real, about daily life and balance.",
    "'What’s one small thing that instantly improves your day?'",
    "Hopeful / Optimistic – Bright, uplifting, focusing on growth or gratitude.",
    "'What’s something you’re looking forward to, no matter how small?'",
    "Vulnerable / Honest – Brave, emotional, encouraging openness.",
    "'What’s a truth about yourself that took time to accept?'"
]

def get_prompt(category = random.choice(categories), question_type = random.choice(question_types), tone = random.choice(tones), seed_length = 100):
    return f"""
    Category: {category}
    Question Type: {question_type}
    Tone: {tone}
    Creative Randomness Seed:
    [CHAOTIC_SEED_START] {random_string.get_random_words(seed_length)} [CHAOTIC_SEED_END]
    Guidelines
    
    Write naturally. The question should sound as if it came from a thoughtful, emotionally intelligent person — never robotic or generic.
    Fit the Category. Shape the question around the chosen topic while keeping it personal, relatable, or thought-provoking.
    Match the Question Type.
    Open-Ended: Encourage storytelling, reflection, or imagination.
    Yes/No: Use clear contrast (e.g., 'Would you rather…' or 'Do you believe…').
    Photo: Invite a visual or creative response (e.g., 'Capture a photo that shows…').
    Tone: follow the tonality set by the random choice.
    Use the Randomness Seed only as subtle inspiration for tone, imagery, or emotional direction.
    Examples provided should not limit your creativity they are provided only to guide and advise you, the final thought on the questions still remains to you
    Output Format:
    Write only the final question — no explanations, headings, or meta text.
    
    [QUESTION]
    """