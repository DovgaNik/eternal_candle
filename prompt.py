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
The questions must not be repetitive, you are provided with a list of previously generated questions. You must analyse the questions provided and see what is common between some of them and avoid that. For example, similar ideas, similar topics, similar question types, similar first word of the question and opening(for example if multiple questions start with when you must avoid using that type of question).:
{get_str_recent(15)}

As well as that, you are introduced with a source of randomness, a paragraph from a romanian story. It will allow you to infer some context or a distant idea that mustn't be present in the question itself but you can develop it into something that can be used in a Candle-style question. THE QUESTIONS MUST BE IN THE STYLE OF THE ONES PRESENT IN CANDLE APPLICATION!!!!!!!!!!!!
{random_string.get_random_paragraph()}
    """
    return prompt
