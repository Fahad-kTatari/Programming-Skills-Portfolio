#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:40:16 2023

@author: FAHAD TATARI
Chapter3 Ex 2 Greetings
Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be

personalized with the person’s name.
"""

names = ["Sumaima", "Ahmed", "Ali", "Khalid", "Amir"]

message = "Hello {},you are an amazing person!"

for name in names:
    print(message.format(name))
