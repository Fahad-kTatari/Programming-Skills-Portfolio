#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:00:55 2023

@author: FAHAD TATARI
Chapter 5 Ex 3 Glossary 2
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""

programming_glossary = {
    "variable": "A storage location in a program where you can store and manipulate data.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "A control structure that repeats a block of code until a certain condition is met.",
    "conditional statement": "A statement that allows you to execute different code based on specified conditions.",
    "list": "A data structure that holds an order of items."
}

programming_glossary["dictionary"] = "A data structure that stores key-value pairs."
programming_glossary["module"] = "A file containing Python code that can be reused in other programs."
programming_glossary["class"] = "A blueprint for creating objects with shared attributes and methods."
programming_glossary["exception"] = "An error that occurs during program execution and can be handled using try-except blocks."
programming_glossary["algorithm"] = "A step-by-step procedure for solving a problem or accomplishing a task."

# Print the glossary using a loop
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")
