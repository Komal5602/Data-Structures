def selection_sort(myList):
    for i in range(len(myList)-1):
        min_index = i
        for j in range(i+1, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j
        myList[i],myList[min_index] = myList[min_index],myList[i]
    return myList
myList = [4,8,2,9,0,1]
print(selection_sort(myList))  