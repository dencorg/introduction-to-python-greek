num = int(input("X: "))

# έξοδος με μηδέν
while num != 0:
    print(1/num)
    num = int(input("X: "))

# έξοδος με break
while True:
    num = int(input("X: "))

    if num == 0:
        break

    print(1/num)

# Fibonacci sum
def fib(a, b):
    sum = 0;

    while a < 4 * (10 ** 6):
        sum += a
        a, b = b, a + b

    return sum

a, b = 0, 1
print(fib(a, b))

# 0 μέχρι το 9
for i in range(10):
    print(i, end=" ")

# 5 μέχρι 45 (βήμα 10)
for i in range(5,50,10):
    print(i, end=" ")

# Κ-α-λ-η-μ-έ-ρ-α-
for c in "Καλημέρα":
    print(c, end="-")