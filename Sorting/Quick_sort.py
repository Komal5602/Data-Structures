def swap(myList,index1,index2):
    myList[index1],myList[index2]=myList[index2],myList[index1]
    return myList

def pivot(myList,pivot_index,end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if myList[i] < myList[pivot_index]:
            swap_index += 1
            swap(myList, i, swap_index)
    swap(myList,pivot_index,swap_index)
    return swap_index

def _quick_sort(myList,left,right):
    if left < right:
        pivot_index = pivot(myList,left,right)
        _quick_sort(myList,left,pivot_index-1)
        _quick_sort(myList,pivot_index+1,right)
    return myList

def quick_sort(myList):
    return _quick_sort(myList,0,len(myList)-1)

myList = [4,6,1,7,5,3,2]
print("Unsorted array:",myList)
print("Sorted Array:",quick_sort(myList))