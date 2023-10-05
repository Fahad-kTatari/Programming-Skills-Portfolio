#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:20:45 2023

@author: rzakir
Chapter 5 Ex 5 pets
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
