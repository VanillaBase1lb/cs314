marks = [[0] * 10] * 7
marks[0] = [float(num) for num in range(1, 11)]

def populateMarksArray():
    for i in range(1, 6):
        marks[i] = [float(num) for num in input().split(sep=" ")]
    marks[6] = [0] * 10
    
def computeTotal():
    for i in range(0, 10):
        marks[6][i] = sum([marks[j][i] for j in range(1, 6)])

def computeClassAverage():
    return sum(marks[6]) / len(marks[6])
    
def computeMaxTotal():
    return int(max(marks[0], key= lambda x: marks[6][int(x - 1)]))
    
if __name__ == "__main__":
    populateMarksArray()
    computeTotal()
    print()
    print(f"class average = {computeClassAverage()}")
    print(f"student id that scored max total marks = {computeMaxTotal()}")
    for i in marks:
        for j in i:
            print(j, end=" ")
        print()
        

'''
input to copy paste:
32.5 23 34 41 22 33 39 38 49.5 29
43 23.5 13.5 21 42 44 47 27 28.5 54
23 45.5 32.5 31 45 21 28 36 46 33.5
12 25 21.5 14 12 11 17 19 20.5 22.5
44 19 26 12 14 29 48 39 50 10
'''