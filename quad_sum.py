
array = []
array = [int(item) for item in input("Enter the list items(seperated with commas) : ").split(',')]
result = set()
sum = int(input("Enter the sum: "))
new1 = array.copy()
for a in array:
    new1.remove(a)
    new2 = new1.copy()
    for b in new1:
        new2.remove(b)
        new3 = new2.copy()
        for c in new2:
            n = sum - (a+b+c)
            new3.remove(c)
            if n in new3:
                quad = (a, b, c, n)
                result.add(quad)

print(f"The set of all Quadruples whose sum is {sum} is {result}")
