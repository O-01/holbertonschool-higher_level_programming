#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        first_character = sentence[0]
    else:
        first_character = None
    return len(sentence), first_character
