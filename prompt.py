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
    "Yes/No (or Either/Or) – Quick contrast, but still meaningful.",
    "Photo / Visual Prompt – Encourages a picture, scene, or creative act.",
    "Choice / Ranking – Small decision or preference that reveals personality.",
    "Fill-in-the-Blank – Short, expressive responses, often poetic or emotional.",
    "Memory Recall – Triggering a specific moment or past experience.",
    "Action / Challenge – Invite the user to do something reflective or creative.",
]

tones = [
    "Deep / Introspective – Serious, thoughtful, exploring meaning or emotion.",
    "Playful / Curious – Light, fun, full of imagination or gentle humor.",
    "Flirty / Romantic – Warm, intimate, expressive of affection or attraction.",
    "Reflective / Nostalgic – Looking back with emotion or gratitude.",
    "Poetic / Sensory – Using imagery, beauty, or feeling to evoke emotion.",
    "Philosophical / Abstract – Big ideas, paradoxes, or imaginative thought.",
    "Whimsical / Surreal – Dreamlike, creative, unexpected.",
    "Grounded / Practical – Simple, real, about daily life and balance.",
    "Hopeful / Optimistic – Bright, uplifting, focusing on growth or gratitude.",
    "Vulnerable / Honest – Brave, emotional, encouraging openness.",
]

def get_prompt(seed_length = 100):
    prompt = f"""
    Category: {random.choice(categories)}
    Question Type: {random.choice(question_types)}
    Tone: {random.choice(tones)}
    Creative Randomness Seed:
    [CHAOTIC_SEED_START] {random_string.get_random_words(seed_length)} [CHAOTIC_SEED_END]
    Guidelines
    
    Your job is to write questions for an application application for couples. The questions will be presented to two people and they will respond to them individually and then see each other's responses. 
    Write naturally. The question should sound as if it came from a thoughtful, emotionally intelligent person — never robotic or generic.
    Fit the Category. Shape the question around the chosen topic while keeping it personal, relatable, or thought-provoking.
    Match the Question Type.
    Open-Ended: Encourage storytelling, reflection, or imagination.
    Yes/No: Use clear contrast (e.g., 'Would you rather…' or 'Do you believe…').
    Photo: Invite a visual or creative response (e.g., 'Capture a photo that shows…').
    Tone: follow the tonality set by the random choice.
    Use the Randomness Seed in order to be able to extract a topic or an idea, it doesn't neccesarily have to be related to the topic but you can infer and think of an idea from the seed.
    Examples provided should not limit your creativity they are provided only to guide and advise you, the final thought on the questions still remains to you.
    The question should not be longer than 30 words.
    Output Format:
    Write only the final question — no explanations, headings, or meta text.
    
    [QUESTION]
    """
    return prompt