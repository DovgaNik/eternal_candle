import random

# GET A RANDOM STRING
# dataset https://apiacoa.org/publications/teaching/datasets/google-10000-english.txt
dataset_file = open("data/ro_paragraphs_12516.csv").read()
dataset =   dataset_file.split('\n')

def get_random_words(amount):
    return random.choice(dataset)