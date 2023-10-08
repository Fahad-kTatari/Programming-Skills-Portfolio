#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 18:23:56 2023

@author: FAHAD TATARI
Chapter 7 Ex 3 T- shirts
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.


"""

def make_shirt(size, message):
    print(f"Making a {size}-sized shirt with the message: '{message}'")

make_shirt("Large", "I Love Python")

make_shirt(size="large", message="I Love Codes")
