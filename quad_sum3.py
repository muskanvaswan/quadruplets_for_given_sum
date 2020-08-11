from itertools import combinations

A = [int(item) for item in input("Enter the list items(seperated with commas) : ").split(',')]
s = int(input("Enter the sum: "))
result = []
possibilities = list(combinations(A, 4))
for p in possibilities:
    if sum(p) == s:
        result.append(p)
print(result)
