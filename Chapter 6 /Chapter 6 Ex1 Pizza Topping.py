#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:34:36 2023

@author: rzakir
"""
Chapter 6 Ex 1 Pizza toppings

pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    
    if topping.lower() == 'quit':
        break
    

    pizza_toppings.append(topping)
    print(f"You'll add {topping} to your pizza.")

print("Your pizza will have the following toppings:")
for topping in pizza_toppings:
    print(topping)
