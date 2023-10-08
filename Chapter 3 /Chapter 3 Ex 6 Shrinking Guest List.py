#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:54:22 2023

@author: rzakir
Chapter 3 Ex 6 shrinking guest list 
"""

guests = ["Ahmed", "Khalid", "Ali", "Zahid"]

print("Apologies, I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Apologies, {removed_guest}, I can't invite you to dinner.")

for remaining_guest in guests:
    print(f"{remaining_guest}, you are still invited to dinner.")

del guests[0]
del guests[0]

print("Guest list is now empty:", guests)
