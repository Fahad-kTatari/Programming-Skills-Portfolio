#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:17:09 2023

@author: rzakir
Chapter 3 Ex 7 seing the world
"""

places_to_visit = ["Japan", "Norway", "Newzeland", "California", "Switzerland"]

print("Original order:")
print(places_to_visit)

print("\nAlphabetical order:")
print(sorted(places_to_visit))

print("\nOriginal order (still):")
print(places_to_visit)

print("\nReverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))

print("\nOriginal order (still):")
print(places_to_visit)

places_to_visit.reverse()

print("\nReversed order:")
print(places_to_visit)

places_to_visit.reverse()

print("\nOriginal order (again):")
print(places_to_visit)

places_to_visit.sort()

print("\nAlphabetical order (sorted):")
print(places_to_visit)

places_to_visit.sort(reverse=True)

print("\nReverse alphabetical order (sorted):")
print(places_to_visit)
