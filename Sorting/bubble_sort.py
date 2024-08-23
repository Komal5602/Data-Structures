def bubble_sort(myList):
    for i in range(len(myList)-1,0,-1):
        for j in range(i):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
    return myList
myList = list(map(int,input().split()))
print(bubble_sort(myList))
