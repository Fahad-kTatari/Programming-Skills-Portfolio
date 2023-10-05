#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 18:05:19 2023

@author: rzakir
Chapter 6 Ex 5 no pastrami
"""

sandwich_orders = ["tuna", "club", "pastrami", "turkey", "ham", "pastrami", "pastrami"]

finished_sandwiches = []

print("Sorry, we have run out of pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
