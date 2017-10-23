# -*- coding: utf-8 -*-

# Collatz conjecture

# είσοδος από το χρήστη
x = int(input("X: "))

# τρέχει όσο μεγαλύτερο του 1
while x > 1:

    if (x % 2 == 0):
        # αν είναι άρτιος
        x = x // 2

    else:
        # αλλιώς
        x = 3 * x + 1

    print(x, end=" ")

print()