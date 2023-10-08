#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:50:21 2023

@author: FAHAD TATARI
Chapter 2 Ex 3 Stripping Nmaes
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().


"""

name_with_whitespace = "\t   Fahad\Tatarin"

print(name_with_whitespace)

print(name_with_whitespace.lstrip())  # Left strip
print(name_with_whitespace.rstrip())  # Right strip
print(name_with_whitespace.strip())   # Strip from both sides
