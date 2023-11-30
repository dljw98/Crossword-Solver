import pandas as pd
import numpy as np
from PyDictionary import PyDictionary

def solve(args):
    input = args
    rows = input.split(",")
    length = len(rows[0])   
    
    for row in rows:
    #print(row)
        if len(row) != length:
            return "Inputted rows are not of the same length!"
        if ' ' in row:
            return "An inputted row contains a blank space!"
    
    dictionary = PyDictionary() # Oxford dictionary package. Used to check words
    all_words = []
    
    # Horizontal
    # abc
    # def
    # ghi
    for i in range(len(rows[0])): # Column-wise
        for j in range(len(rows)): # Row-wise
            word = rows[j][i]
            all_words.append(word)
            
            # Horizontals
            for k in range(i, len(rows[0])): # Column wise
                word += rows[j][k]
                reverse_word = word[::-1]
                all_words.append(word)
                all_words.append(reverse_word)
                        
                        
    
    valid_words = []
    for word in all_words:
        if type(dictionary.meaning(word)) == dict:
            valid_words.append(word)
    for word in valid_words:
        print(word)
    return "Done!"