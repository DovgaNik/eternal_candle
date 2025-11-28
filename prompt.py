import db
import random_string

def get_str_recent(n):
    to_return = ""
    for question in db.get_recent_questions(n):
        to_return += f' - {question}\n'
    return to_return

def build_prompt():
    prompt = f"""
Your job is to generate questions simmilar in style and purpose as the candle mobile application and its competitors.
The questions should not be repetitive or similar to the ones that have been generated earlier, to avoid that you are provided with some previously generated questions avoid repeating the same topics, wording, ideas, concepts, question type, question opening, etc. Analyse the questions that are given to you and find what is common between them and avoid whatever that is. Additionally to the common features, the new question should not repeat any individual questions aspects neither the same way as it should not repeat the general aspects of questions in general:
{get_str_recent(15)}

As well as that, you are introduced with a source of randomness, a paragraph from a romanian story. It will allow you to infer some context or a distant idea that shouldn't be present in the question itself but you can develop it into something that can be used in a Candle-style question:
{random_string.get_random_paragraph()}
    """
    return prompt
