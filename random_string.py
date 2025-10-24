import random

# GET A RANDOM STRING
# dataset https://apiacoa.org/publications/teaching/datasets/google-10000-english.txt
dataset_file = open("google-10000-english.txt").read()
dataset =   dataset_file.split('\n')
def get_random_words(amount):
    to_return = ''
    for i in range(amount):
        to_return += random.choice(dataset) + ' '
    return to_return