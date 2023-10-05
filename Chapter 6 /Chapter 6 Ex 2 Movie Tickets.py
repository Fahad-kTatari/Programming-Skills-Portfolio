#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:50:56 2023

@author: rzakir

Chapter 6 Ex 2 Movie Tickets 
"""

while True:
    age = input("Please enter your age (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break  
    
    try:
        age = int(age)  
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue  
    
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
