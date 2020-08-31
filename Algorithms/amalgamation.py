# Selection sort
listNum = [4, 2, 1, 5, -5, 9, 6, 7]

def selectionSort(listNum):
    for j in range(len(listNum)):
        minValue = listNum[j]
        counter = j
        indValue = j

        for i in range(j, len(listNum)):
            if listNum[i] < minValue:
                minValue = listNum[i]
                indValue = counter
            counter+=1

        listNum[j], listNum[indValue] = listNum[indValue], listNum[j]

    return listNum


# Bubble sort
def bubbleSort(listNum):
    for j in range(len(listNum)):
        for i in range(len(listNum)-1-j):
            if listNum[i] > listNum[i+1]:
                listNum[i], listNum[i+1] = listNum[i+1], listNum[i] 
    return listNum

sortedList = bubbleSort(listNum)



# Merge sort 
def mergeSort(listNum):
    if len(listNum) > 1:
        mid = len(listNum) // 2
        left_list = listNum[:mid]
        right_list = listNum[mid:]
        mergeSort(left_list)
        mergeSort(right_list)

        i = 0
        j = 0 
        k = 0

        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                listNum[k] = left_list[i]
                i+=1
                k+=1
            else:
                listNum[k] = right_list[j]
                j+=1
                k+=1

        while i<len(left_list):
            listNum[k] = left_list[i]
            i+=1
            k+=1

        while i<len(right_list):
            listNum[k] = right_list[j]
            j+=1
            k+=1

        

    return listNum      



def tryAgain(mySortList):
    if len(mySortList) > 1:
        mid = len(mySortList) // 2
        left_list = mySortList[:mid]
        right_list = mySortList[mid:]
        tryAgain(left_list)
        tryAgain(right_list)

        i = 0
        j = 0
        k = 0

        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                mySortList[k] = left_list[i]
                i+=1
                k+=1
            else:
                mySortList[k] = right_list[j]
                j+=1
                k+=1

        while i<len(left_list):
            mySortList[k] = left_list[i]
            i+=1
            k+=1

        while i<len(right_list):
            mySortList[k] = right_list[j]
            j+=1
            k+=1

    return mySortList



def pivot_place(list1, first, last):
    pivot = list1[first]
    left_index = first+1
    right_index = last

    while True:
        while left_index <= right_index and list1[left_index]<=pivot:
            left_index+=1
        while left_index <= right_index and list1[right_index]>=pivot:
            right_ind ex-=1

        if right_index < left_index:
            break
        else:
            list1[left_index], list1[right_index] = list1[right_index], list1[left_index]

    list1[first], list1[left_index] = list1[left_index], list1[first]
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

