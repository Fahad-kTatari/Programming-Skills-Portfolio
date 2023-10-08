#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 18:28:01 2023

@author: FAHAD TATARI
chapter 7 Ex4 Large Shirts
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size="large", message="I Love Python"):
    print(f"Making a {size}-sized shirt with the message: '{message}'")

make_shirt()

make_shirt(size="medium")

make_shirt(size="small", message="Python is Awesome!")
