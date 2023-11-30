import pandas as pd
import numpy as np
from PyDictionary import PyDictionary

def solve():
    user_input = input("Enter the crossword: ")
    minimum_length = input("Enter the minimum word length: ")
    try:
        minimum_length = int(minimum_length)
    except:
        print("Please input a valid minimum word length!")
        return
    rows = user_input.split(",")
    length = len(rows[0])
    
    if (length < minimum_length) and (len(rows) < minimum_length):
        print("Crossword dimensions too small for minimum word length!")
        return
        
    for row in rows:
    #print(row)
        if len(row) != length:
            return "Inputted rows are not of the same length!"
        if ' ' in row:
            return "An inputted row contains a blank space!"
    
    dictionary = PyDictionary() # Oxford dictionary package. Used to check words
    all_words = []
    
    # Horizontal
    for i in range(len(rows[0])): # Column-wise
        for j in range(len(rows)): # Row-wise
            word = rows[j][i]
            all_words.append(word)
            
            # Going across horizontally
            for k in range(i+1, len(rows[0])): # Column-wise
                word += rows[j][k]
                reverse_word = word[::-1]
                all_words.append(word)
                all_words.append(reverse_word)
            
    # Verticals
    for i in range(len(rows[0])): # Column-wise
        for j in range(len(rows)): # Row-wise
            word = rows[j][i]
            all_words.append(word)
            
            # Going down vertically
            for k in range(j+1, len(rows)): # Row-wise
                word += rows[k][i]
                reverse_word = word[::-1]
                all_words.append(word)
                all_words.append(reverse_word)
    
    # Diagonals (Left Up to Right Down)
    for i in range(len(rows[0])): # Column-wise
        for j in range(len(rows)): # Row-wise
            word = rows[j][i]
            print(word)
            all_words.append(word)
            curr_column = i+1
            curr_row = j+1
            
            while (curr_row < len(rows[0])) and (curr_column < len(rows)):
                word += rows[curr_row][curr_column]
                reverse_word = word[::-1]
                all_words.append(word)
                all_words.append(reverse_word)
                
                curr_column += 1
                curr_row += 1
                print(word)
                print(reverse_word)
                print('------')
                
                        
    ''''
    valid_words = []
    for word in all_words:
        if type(dictionary.meaning(word)) == dict:
            valid_words.append(word)
    for word in valid_words:
        print(word)
    return "Done!"'''
    #for word in all_words:
    #    print(word)
solve()