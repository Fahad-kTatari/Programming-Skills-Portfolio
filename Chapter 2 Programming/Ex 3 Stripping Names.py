#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:50:21 2023

@author: rzakir
"""

name_with_whitespace = "\t   Fahad\Tatarin"

print(name_with_whitespace)

print(name_with_whitespace.lstrip())  # Left strip
print(name_with_whitespace.rstrip())  # Right strip
print(name_with_whitespace.strip())   # Strip from both sides
