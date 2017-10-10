#!/usr/bin/env python

# This script calculates an average from a list of numbers in the
# range of 0-100.
#
# Remember that an average is the sum of whole list divided
# by the number of entries in the list.
#
# For letter grades:
#    Scores between 90 and 100 = A
#    Scores between 80 and 89  = B
#    Scores between 70 and 79  = C
#    Scores between 60 and 69  = D
#             Scores under 60  = F

def assign_grades(scores):

    grades = {}

    for k,v in scores.items():
        avg = calculate_average(v)
        grades[k] = letter_grade(avg)

    return grades

def letter_grade(average):

    if average >= 90:
        return 'A'
    elif average >= 80 and average < 90:
        return 'B'
    elif average >= 70 and average < 80:
        return 'C'
    elif average >= 60 and average < 70:
        return 'D'
    else:
        return 'F'

def calculate_average(grades):
    entries = len(grades)
    total = 0
    for n in grades:
        total = total + n

    return total/entries
