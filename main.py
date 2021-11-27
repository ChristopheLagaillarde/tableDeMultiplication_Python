import sys
sys.tracebacklimit = 0
try:
    a = int(input("Saisir un nombre"))

    for i in range(13):
        print(a, "x", i, "=", a * i)

except ValueError:
    print("saisie non valide")

