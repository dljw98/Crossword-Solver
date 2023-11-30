# Crossword Solver

## Introduction
Welcome to the Crossword Solver, a Python-based tool designed to assist you in conquering challenging crossword puzzles! This solver is a command-line application that leverages the power of Python to find solutions for crossword clues, making your puzzling experience more enjoyable and efficient. I was inspired to make this crossword puzzle after casually encountering a difficult crossword puzzle online that stumped me.

## Getting started
To start solving crosswords with this tool, follow the installation instructions below and begin enjoying a seamless solving experience.
1. Clone this repository to your local machine using GitBash. Detailed instructions can be found at https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
2. On the same GitBash client, navigate to the project directory using `cd crossword-solver`
3. Install the required dependencies using `pip install -r requirements.txt`

## Using the solver
1. Run the solver using `python main.py`
2. You will be prompted to input the number of rows in your crossword puzzle
3. Next, you will need to input the letters of each row
4. Finally, you will need to indicate the minimum word length that you wish to find for your results
5. Once that has been done, hit `Enter`, which prompts the solver to run  and output the valid words. The validity of a word is determined using the english-dictionary package by Daniel E. Dell'uomo. This package is also commonly used for NLP applications. https://pypi.org/project/english-dictionary/

## Notes
- Your crossword puzzle does not have to be a square, the program accepts any dimensions
- Ensure that all the inputted rows are of the same length, or the program will flag this and print an error message
- Ensure that your crossword puzzle can accomodate the minimum word length. For instance, if your crossword dimensions are 3x3 and the inputted minimum word length is 4, the program will flag this and print an error message

## Sample program output
<img width="600" alt="image" src="https://github.com/dljw98/Crossword-Solver/assets/72072042/4bb7b8af-7306-40a0-9f35-0dba57b356c6">

