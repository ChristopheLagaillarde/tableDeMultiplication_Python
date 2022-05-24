# Program : give_multiplication_table
# Description : Give the multiplication table of a number
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

def give_multiplication_table(number: int, max_multiplier: int) -> list:
    max_multiplier += 1
    result = [0] * max_multiplier
    for i in range(max_multiplier):
        result[i] = number * i
    return result

