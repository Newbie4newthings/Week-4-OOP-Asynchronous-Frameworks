# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BLXUItRUrrJVlql1G9V1jaG_pStfeOKT
"""

# Define the Person class
class Person:
    def __init__(i, name, age, gender):
        # Initialize attributes
        i.name = name
        i.age = age
        i.gender = gender

    # Method to introduce the person
    def introduce(i):
        print(f"Hello, my name is {i.name}. I am {i.age} years old and my gender is {i.gender}.")

# Create an instance of the Person class
person_one = Person("Martin", 28, "Male")

# Call the introduce method to display the person's information
person_one.introduce()