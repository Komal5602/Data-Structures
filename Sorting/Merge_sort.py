def merge_sort(myList):
    if len(myList) == 1:
        return myList
    mid = len(myList) // 2
    left = merge_sort(myList[:mid])
    right = merge_sort(myList[mid:])
    return merge(left, right)

def merge(left,right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

myList = [3,1,2,5,4]
print(merge_sort(myList))
    