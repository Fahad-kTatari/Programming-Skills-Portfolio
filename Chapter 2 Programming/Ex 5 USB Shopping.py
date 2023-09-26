#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:53:20 2023

@author: rzakir
"""

usb_stick_cost = 6
total_budget = 50

num_usb_sticks = total_budget // usb_stick_cost

remaining_budget = total_budget % usb_stick_cost

print("She can buy", num_usb_sticks, "USB sticks.")
print("She will have £", remaining_budget, "left.")
