#!/usr/bin/python3

def multiple_returns(sentence):
    first_char = None if len(sentence) == 0 else sentence[0]
    length = len(sentence)
    return length, first_char
