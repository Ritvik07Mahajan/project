# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:23:59 2020

@author: CODER_RITVIK
"""


import json                             #importing the required packages
from difflib import get_close_matches

data = json.load(open("data.json"))     #loadind the required JSON file 

def translate(w):
    w = w.lower()                   #returns the lowercase of the string 
    if w in data:
        return data[w]

    elif w.title() in data:         #it looks for the words like Delhi
        return data[w.title()]

    elif w.upper() in data:         #in case user enters words like USA
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:         #if the required is not present in the dictionary
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N":
            return "The word doesn't exist. Please double check it."

        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")         #inputting the required word
output = translate(word)


if type(output) == list:           #if the output is  a list 
    for item in output:
        print(item)

else:
    print(output)                  #if the output is a string 