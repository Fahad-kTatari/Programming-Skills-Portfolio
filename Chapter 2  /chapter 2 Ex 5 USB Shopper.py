#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:53:20 2023

@author: FAHAD TATARI
Chapter 2 Ex 5 USB shopper
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.

"""

usb_stick_cost = 6
total_budget = 50

num_usb_sticks = total_budget // usb_stick_cost

remaining_budget = total_budget % usb_stick_cost

print("She can buy", num_usb_sticks, "USB sticks.")
print("She will have £", remaining_budget, "left.")
