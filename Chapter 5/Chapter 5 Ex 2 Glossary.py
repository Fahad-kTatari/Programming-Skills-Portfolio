# -*- coding: utf-8 -*-
"""
Spyder Editor
Author = FAHAD TATARI
"""
Chapter 5 Ex 2 Glossary
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.
"""



programming_glossary = {
    "variable": "A storage location in a program where you can store and manipulate data.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "A control structure that repeats a block of code until a certain condition is met.",
    "conditional statement": "A statement that allows you to execute different code based on specified conditions.",
    "list": "A data structure that holds an ordered."
}

for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")
