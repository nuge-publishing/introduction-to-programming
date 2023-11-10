from math import sqrt as sq

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

G = sq(a * b)
Q = sq((a**2 + b**2) / 2)

print("Geometric Mean: ", G)
print("Quadratic Mean: ", Q)