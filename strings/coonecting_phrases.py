#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'generate_phrases' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY phrases as parameter.
#

def generate_phrases(phrases):
    start_map = dict()
    # end_map = dict()
    for i in range(len(phrases)):
        phrase = phrases[i]
        phrase_list = phrase.split()
        if phrase_list[0] in start_map:
            start_map[phrase_list[0]].append(i)
        else:
            start_map[phrase_list[0]] = []
            start_map[phrase_list[0]].append(i)
        # if phrase_list[-1] in end_map:
        #     end_map[phrase_list[-1]].append(i)
        # else:
        #     end_map[phrase_list[-1]] = []
        #     end_map[phrase_list[-1]].append(i)
    output = []
    for i in range(len(phrases)):
        phrase = phrases[i]
        phrase_list = phrase.split()
        if phrase_list[-1] in start_map:
            for j in start_map[phrase_list[-1]]:
                second_phrase = phrases[j]
                second_phrase_list = second_phrase.split()[1:]
                second_phrase_new = " ".join(second_phrase_list)
                output.append(phrase + " " + second_phrase_new)
    return output


if __name__ == '__main__':
    input = [
        'mission statement',
        'a quick bite to eat',
        'a chip off the old block',
        'chocolate bar',
        'mission impossible',
        'a man on a mission',
        'block party',
        'eat my words',
        'bar of soap'
    ]

    print(generate_phrases(input))