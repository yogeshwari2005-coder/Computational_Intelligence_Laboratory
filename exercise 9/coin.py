import random

n = int(input("Enter number of coin tosses: "))

heads = 0
tails = 0

for i in range(n):
    toss = random.choice(["H", "T"])
    print("Toss", i+1, ":", toss)

    if toss == "H":
        heads = heads + 1
    else:
        tails = tails + 1

print("\nResults")
print("Heads =", heads)
print("Tails =", tails)

print("\nProbabilities")
print("P(Heads) =", heads / n)
print("P(Tails) =", tails / n)
