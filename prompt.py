import db
import random_string


def build_prompt():
    prompt = f"""
Your job is to generate questions simmilar in style and purpose as the candle mobile application and its competitors.
The questions should not be repetitive or similar to the ones that have been generated earlier, to avoid that you are provided with some previously generated questions avoid repeating the same topics, wording, ideas, concepts etc.:
{db.get_recent_questions(10)}

As well as that, knowing that you are an ai model that tends to generate repetitive content, you are introduced with a source of randomness, a paragraph from a romanian story. It will allow you to infer some context or a distant idea that shouldn't be present in the question itself but you can develop it into something that can be used in a Candle-style question:
{random_string.get_random_paragraph()}

The length of the question should be limited to 25 words.
Output format:
{{
    "question_explanation": "<explanation of the topic that the question wants to address, limited to 50 words>",
    "question": "<question, limited to 25 words>"
}}
    """
    return prompt
