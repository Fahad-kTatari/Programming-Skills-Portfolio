#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:24:05 2023

@author: rzakir
Chapter 3 Ex 5 Change guest list
"""

invitees = ["Ahmed", "Ali", "Khalid"]

invitation_message = "Dear {},\n,I would appreciate if you would accept my invitation and come to dinner"

guest_cant_make_it = "Ali"

print("Ali can't make it to the dinner.")

invitees.remove(guest_cant_make_it)
new_invitee = "Zahid"
invitees.append(new_invitee)

for person in invitees:
    print(invitation_message.format(person))
