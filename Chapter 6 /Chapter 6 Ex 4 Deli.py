#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 18:01:02 2023

@author: rzakir
Chapter 6 Ex 4 Deli
"""

sandwich_orders = ["tuna","club","turkey","ham"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
