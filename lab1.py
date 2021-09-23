# Programmers: Veljko Ilic, Milos Ilic, Alonso Faure
# Course: CS151, Prof. Mehri
# Date: September 23th 2021
# Lab Number: 1
#This program will give the number of tablespoons and teaspoons equivalent to a value in mm input by the user

mL = input("Enter value in mL:")
mL = float(mL)
teaspoon = mL//5
tablespoon = teaspoon//3
teaspoon = teaspoon - 3 * tablespoon
print(mL, "mL =", teaspoon, "teaspoons")
print(mL, "mL =", tablespoon, "tablespoons")