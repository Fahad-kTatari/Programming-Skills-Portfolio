#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:08:06 2023

@author: rzakir
Chapter 5 Ex 4 Rivers
"""

rivers = {
    "Amazon": "Brazil",
    "Yangtze": "China",
    "Nile": "Egypt"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers:")
for river in rivers.keys():
    print(river)

print("\nCountries:")
for country in rivers.values():
    print(country)
