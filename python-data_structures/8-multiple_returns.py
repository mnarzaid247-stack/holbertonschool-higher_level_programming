#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        length = len(sentence)
        first_ch = sentence[0]
        return length, first_ch
    else:
        length = 0
        first_ch = None
        return length, first_ch
