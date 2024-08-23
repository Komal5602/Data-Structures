def insertion_sort(myList):
    for i in range(1, len(myList)):
        temp = myList[i]
        j = i - 1
        while myList[j] > temp and j > -1:
            myList[j+1] = myList[j]
            myList[j] = temp
            j -= 1
    return myList
myList = [3,1,4,2,5]
print(insertion_sort(myList))    

