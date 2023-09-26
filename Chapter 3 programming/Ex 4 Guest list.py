#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:53:11 2023

@author: rzakir
"""
invitees = ["Ahmed", "Ali", "Khalid"]

invitation_message = "Dear {},\n i would appreciate if you would accept my invitation and come to dinner

for person in invitees:
    print(invitation_message.format(person))
