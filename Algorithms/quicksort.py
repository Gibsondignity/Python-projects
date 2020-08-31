
# to get the correct position of the pivot element
def pivot_place(list1, first, last):
    pivot = list1[first]
    left_index = first+1
    right_index = last

    while True:
        while left_index <= right_index and list1[left_index]<=pivot:
            left_index+=1
        while left_index <= right_index and list1[right_index]>=pivot:
            right_index-=1

        if right_index < left_index:
            break
        else:
            list1[left_index], list1[right_index] = list1[right_index], list1[left_index]

    list1[first], list1[right_index] = list1[right_index], list1[first]

    return right_index

def quickSort(list1, first, last):
    if first<last:
        p = pivot_place(list1, first, last)
        quickSort(list1, first, p-1)
        quickSort(list1, p+1, last)


listNum = [56, 26, 93, 17, 31, 44]
n = len(listNum)
quickSort(listNum, 0, n-1)
print(listNum)

