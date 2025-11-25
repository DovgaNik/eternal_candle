import random

# GET A RANDOM STRING
# dataset used before with just random words https://apiacoa.org/publications/teaching/datasets/google-10000-english.txt
# dataset with paragraphs in romanian https://huggingface.co/datasets/readerbench/ro-stories
# This dataset has to be cleared up before being to being just a pragragraph in a single sting per line
dataset_file = open("data/ro_paragraphs_12516.csv").read()
dataset = dataset_file.split('\n')

def get_random_paragraph():
    return random.choice(dataset)