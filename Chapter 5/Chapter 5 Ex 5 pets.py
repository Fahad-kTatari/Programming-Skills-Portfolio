#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:20:45 2023

@author: FAHAD TATARI
Chapter 5 Ex 5 pets
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""

pets = [
    {"kind": "Dog", "owner": "Ali"},
    {"kind": "Cat", "owner": "Ahmed"},
    {"kind": "Lion", "owner": "Khalid"},
    {"kind": "Zebra", "owner": "Zahid"}
]

for pet in pets:
    kind = pet["kind"]
    owner = pet["owner"]
    print(f"This is a {kind} owned by {owner}.")
