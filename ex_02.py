a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

A = (a + b) / 2
rp_a = 1 / a
rp_b = 1 / b
H = 2 / (rp_a + rp_b)

print("Arithmetic Mean: ", A)
print("Harmonic Mean: ", H)