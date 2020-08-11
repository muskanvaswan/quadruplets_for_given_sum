A = []
A = [int(item) for item in input("Enter the list items(seperated with commas) : ").split(',')]
result = set()
sum = int(input("Enter the sum: "))

A.sort()
f =0
l = len(A)-1

while l-f>2:
    if A[f]+A[l]>sum:
        A.pop()
        l-=1
    else:
        k = sum -( A[f]+A[l])
        i = f + 1
        j = l - 1
        while True:
            if A[i]+A[j]>k:
                if j-i>1:
                    j-=1
                else:
                    l-=1
                    break
            elif A[i]+A[j]<k:
                if j-i>1:
                    i+=1
                else:
                    f+=1
                    l=len(A)-1
                    break
            else:
                quad = (A[f], A[l], A[i], A[j])
                result.add(quad)
                if j-i>2:
                    j-=1
                    i+=1
                else:
                    l-=1
                    break
print(result)
