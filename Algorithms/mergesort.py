# Input 
# Devide 
# Merge
L = [2, 3, 9, 1, -3, 0, 4, -1]
'''
def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i+=1
                k+=1
            else: 
                list1[k] = right_list[j]
                j+=1
                k+=1
                
        while i<len(left_list):
            list1[k] = left_list[i]
            i+=1
            k+=1
            
        while j<len(right_list):
            list1[k] = right_list[j]
            j+=1
            k+=1
'''
#num = int(input("How many numbers do you want to type? "))

#list1 = [int(input("Enter number: ")) for x in range(num)]
'''
def sortlist(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left_list = mylist[:mid]
        right_list = mylist[mid:]
        sortlist(left_list)
        sortlist(right_list)

        i = 0
        j = 0
        k = 0

        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                mylist[k] = left_list[i]
                i+=1
                k+=1
            else:
                mylist[k] = right_list[j]
                j+=1
                k+=1
        while i<len(left_list):
            mylist[k] = left_list[i]
            i+=1
            k+=1
        while j<len(right_list):
            mylist[k] = right_list[j]
            j+=1
            k+=1
'''

'''
def myMergeSortList(list2):
    if len(list2) > 1:
        mid = len(list2) // 2
        leftList = list2[:mid]
        rightList = list2[mid:]
        myMergeSortList(leftList)
        myMergeSortList(rightList)

        i = 0
        j = 0
        k = 0

        while i<len(leftList) and j<len(rightList):
            if leftList[i] < rightList[j]:
                list2[k] = leftList[i]
                i+=1
                k+=1
            else:
                list2[k] = rightList[j]
                j+=1
                k+=1

        while i<len(leftList):
            list2[k] = leftList[i]
            i+=1
            k+=1

        while j<len(rightList):
            list2[k] = rightList[j]
            j+=1
            k+=1
'''



def mergeSortAlgorithm(list2):
    if len(list2) > 1:
        mid = len(list2) // 2 
        left_list = list2[:mid]
        right_list = list2[mid:]
        mergeSortAlgorithm(left_list)
        mergeSortAlgorithm(right_list)

        i = 0
        j = 0
        k = 0

        while i<len(left_list) and j<len(right_list):
            if left_list[i]< right_list[j]:
                list2[k] = left_list[i]
                i+=1
                k+=1
            else:
                list2[k] = right_list[j]
                j+=1
                k+=1

        while i<len(left_list):
                list2[k] = left_list[i]
                i+=1
                k+=1

        while j<len(right_list):
                list2[k] = right_list[j]
                j+=1
                k+=1

L = [4, 1, 5, -5, 3, 6, -1, 8, -4]
mergeSortAlgorithm(L)
print(L)








