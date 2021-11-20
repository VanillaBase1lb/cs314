arr = [[1, 3, 4], [3, 5, 5], [6, 6, 6]]

def isPrime(num):
    if num <= 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def modifyArray(arr) :
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                if isPrime(arr[i][j]) == 1:
                    arr[i][j] += 1
                else:
                    arr[i][j] -= 1

modifyArray(arr)

for i in arr:
    for j in i:
        print(j, end=" ")
    print()