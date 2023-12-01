import pandas as pd
import numpy as np
import sys
import os
from english_dictionary.scripts.read_pickle import get_dict

def solve():
    num_rows = int(input("Enter the number of rows:"))
    rows = []
    for row in range(1, num_rows+1):
        user_input = input(f"Enter Row #{row}: ")
        rows.append(user_input)
    minimum_length = input("Enter the minimum word length: ")
    try:
        minimum_length = int(minimum_length)
    except:
        print("Please input a valid minimum word length!")
        return
    length = len(rows[0])
    
    if (length < minimum_length) and (len(rows) < minimum_length):
        print("Word search dimensions too small for minimum word length!")
        return
        
    for row in rows:
        if len(row) != length:
            return "Inputted rows are not of the same length!"
        if ' ' in row:
            return "An inputted row contains a blank space!"
    
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
                
    # Diagonals (Left Down to Right Up)
    for i in range(len(rows[0])): # Column-wise
        for j in range(len(rows)): # Row-wise
            word = rows[j][i]
            all_words.append(word)
            curr_column = i+1
            curr_row = j-1
            
            while (curr_row >= 0) and (curr_column < len(rows)):
                word += rows[curr_row][curr_column]
                reverse_word = word[::-1]
                all_words.append(word)
                all_words.append(reverse_word)
                
                curr_column += 1
                curr_row -= 1
                
    valid_words = []
    english_dict = get_dict()
    
    for word in all_words:
        if len(word) < minimum_length:
            continue
        if word in english_dict:
            valid_words.append(word)
        if word == 'kiasu': # Inside joke with my girlfriend :)
            valid_words.append(word)
    for word in valid_words:
        print(word)
    
    return
