n = 5
arr = [None] * n

def populateArray():
    for i in range(0, n):
        arr[i] = []
        arr[i] = [int(j) for j in input().split(sep=" ")]
        
def sortRows():
    for row in arr:
        row[1:] = sorted(row[1:])

if __name__ == "__main__":
    populateArray()
    sortRows()
    print()
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

'''
input to copy paste:
1 89 65 90 45 23 10 43 23 18 12
2 85 60 95 40 21 18 40 27 13 17
3 80 62 91 42 22 12 41 25 10 71
4 81 61 94 49 29 13 46 21 12 88
5 83 66 96 47 27 14 48 28 19 55
'''