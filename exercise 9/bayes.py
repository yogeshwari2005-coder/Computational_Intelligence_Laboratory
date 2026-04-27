print("Bayes Theorem")

A = input("Enter event A: ")
B = input("Enter event B: ")

p_B_given_A = float(input("Enter P(B|A): "))
p_A = float(input("Enter P(A): "))
p_B = float(input("Enter P(B): "))

if p_B == 0:
    print("P(B) cannot be zero")
else:
    result = (p_B_given_A * p_A) / p_B
    print("P(", A, "|", B, ") =", round(result,4))
