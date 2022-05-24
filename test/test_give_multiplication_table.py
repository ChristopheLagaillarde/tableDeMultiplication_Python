# Program : test_give_multiplication_table
# Description : test case of give_multiplication_table
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

from give_multiplication_table import give_multiplication_table


def test_give_multiplication_table() -> None:
    assert give_multiplication_table(7, 12) == [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84],\
        "the program does not work"


test_give_multiplication_table()