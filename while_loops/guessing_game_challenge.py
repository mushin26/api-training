#!/usr/bin/env python3
"""Jurassic Park Trivia | Solution"""

cq1=0
cq2=0

while cq1 < 3:
    # Question 1
    question1 = input("In Jurassic Park, what kind of dinosaur is the star attraction? ")

    # Check if the answer is correct (case-insensitive)
    if question1.lower() in ["t-rex", "trex", "tyrannosaurus rex"]:
        print("Correct! The T-Rex is the star attraction!")
        break
    else:
        cq1+=1
        if cq1 == 3:
            print("Sorry, that's not correct. The correct answer is T-Rex.")
        else:
            print("Sorry, that's not correct.")
            continue

while cq2 < 3:
    # Question 2
    question2 = input("What type of DNA was used to fill the gaps in the dinosaur genome? ")

    # Check if the answer is correct (case-insensitive)
    if question2.lower() == "frog":
        print("Correct! Frog DNA was used to fill the gaps in the genome!")
        break
    else:
        cq2+=1
        if cq2 == 3:
            print("Sorry, that's not correct. The correct answer is Frog.")
        else:
            print("Sorry, that's not correct")
            continue
