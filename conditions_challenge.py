#!/usr/bin/env python3
"""Jurassic Park Trivia"""

# Question 1
question1 = input("In Jurassic Park, what kind of dinosaur is the star attraction? ")

# Check if the answer is correct (you need to add the logic!)

# Question 2
question2 = input("What type of DNA was used to fill the gaps in the dinosaur genome? ")

# Check if the answer is correct (you need to add the logic!)

if question1.lower() == "t-rex" and  question2.lower() == "frog":
    print("Respuesta correcta")

elif question1.lower() == "t-rex" and  question2.lower() != "frog":
    print("Dino Ok but ADN not ok")

elif question1.lower() != "t-rex" and  question2.lower() == "frog":
    print("ADN Ok but Dino not ok")

else:
    print("Ninguna respuesta es correcta") 
