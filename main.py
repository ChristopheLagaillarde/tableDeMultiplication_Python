# Program : main
# Description : execute give_multiplier_table
# Date : 24/05/22
# Author : Christophe LAGAILLARDE
# Version : 1.0

from give_multiplication_table import give_multiplication_table


def main() -> None:
    try:
        print(give_multiplication_table(int(input("number to multiply: ")), int(input("max multiplier: "))))
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()

