variables = []
n = int(input("Enter number of variables: "))

for i in range(n):
    name = input("Enter variable name: ")
    variables.append(name)

rows = []
total = 0

print("\nEnter values for all combinations:")

for a in [True, False]:
    for b in [True, False]:
        for c in [True, False]:
            row = {}
            row[variables[0]] = a
            row[variables[1]] = b
            row[variables[2]] = c

            print(variables[0], "=", a, ",",
                  variables[1], "=", b, ",",
                  variables[2], "=", c)

            value = float(input("Enter value: "))
            row["prob"] = value
            total = total + value
            rows.append(row)

for row in rows:
    row["prob"] = row["prob"] / total

query = input("\nEnter query variable (example: a): ")

sum_prob = 0

for row in rows:
    if row[query] == True:
        sum_prob = sum_prob + row["prob"]

print("P(", query, ") =", round(sum_prob,4))
