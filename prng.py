#!/usr/bin/python
# -*- coding: UTF-8 -*-
from random import choice, seed, random
from hashlib import sha512
import sys
import argparse

# Getting Pretty Console Parameters
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--file')
    parser.add_argument ('--numbilets')
    parser.add_argument ('--parameter')     
    return parser


# Only when main
if __name__ == '__main__':

    parser = createParser()
    arguments = parser.parse_args(sys.argv[1:])

    try:
        data_file = open(arguments.file,'r', encoding='utf-8')
    except FileNotFoundError:
        print("Error: File not found (check --file argument)")
        sys.exit()
    
    upper_limit = int(arguments.numbilets)
    used_seed = int(arguments.parameter)

    salt = hex(used_seed)

    questions = [i for i in range(1, upper_limit+1)]

    for i in data_file:
        # using sha512 for unspecified meme reasons
        hash_object = sha512(i.strip().encode('utf8')+salt.encode('utf8'))
        hex_dig = hash_object.hexdigest()

        # using seed to get question number
        seed(hex_dig.encode('utf8'))
        print(i.strip() + ": " + str(choice(questions)))

    data_file.close()





     
