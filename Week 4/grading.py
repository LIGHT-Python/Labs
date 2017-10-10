#!/usr/bin/env python

def assign_grades(scores):
    """Given a dict of names and a list of test scores, assign each student a
    letter grade and return it as a dict."""

    grades = {}

    for k,v in scores.items():
        avg = calculate_average(v)
        grades[k] = letter_grade(avg)

    return grades

def letter_grade(average):
    """Scores between 90 and 100 = A
       Scores between 80 and 89  = B
       Scores between 70 and 79  = C
       Scores between 60 and 69  = D
                Scores under 60  = F
    """

    pass

def calculate_average(grades):
    """This function calculates an average from a list of numbers in the range
    of 0-100.  Remember that an average is the sum of whole list divided by the
    number of entries in the list."""

    pass
