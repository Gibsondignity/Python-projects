# Selection sort
# Bubble sort
# Merge sort

'''def searchMinForList(L, n):
    counter = 1
    minValue = L[0]

    while (counter < n):

        v = L[counter]

        if v < minValue:
            minValue = v 
        else:
            pass

        counter += 1

    print(minValue)'''


'''def sortList(L, n):
    L2 = []
    counter = 0
    while (counter <= n):
        m, idx = searchMinForList(L, n)
        L2.append(m)

        del L[idx]
        n = n-1
    return L2


L = [10, -5, 3, -20, 15, 0, -5]
n = len(L)-1

searchMinForList(L, n)

#L = [10, -2, 11, 1,2,3,-5, 8, -1, -6, 31]
L = [1, 2, 4, -5, 7, 9, 3, 2]
print("The first list list is: ", L)

for j in range(len(L)):

    maxValue = L[j]
    counter = j
    idx = j
    for i in range(j, len(L)):
        if L[i] > maxValue:
            maxValue = L[i]
            idx = counter

        counter += 1

    temp = L[j]
    L[j] = maxValue
    L[idx] = temp
print("And")
print("The sorted list is: ", L)
'''

L = [4, 2, 5, 6, 10, 3, -2, -1, 9, 8]
l1 = [4, -4, 2, 5, 6, 10, 3, -2, -1, 9, 8]

for j in range(len(L)):
    lowest_value = L[j]
    idx  = j
    counter = j

    for i in  range(j, len(L)):
        if L[i] < lowest_value:
            lowest_value = L[i]
            idx = counter
        counter+=1


    temp = L[j]
    L[j] = lowest_value
    L[idx] = temp


#print(L)
for i in range(len(l1)):
    min_val = min(l1[i:])
    min_ind = l1.index(min_val)
    l1[i], l1[min_ind] = l1[min_ind], l1[i]

'''
""" Selection sort algorithm using the built-in function"""

list1 = int(input("How many numbers do you want to type ? "))
L = [int(input("Enter number: ")) for x in range(list1)]

print("Unsorted list: ", L)
for i in range(len(L)):
    min_value = min(L[i:len(L)])
    minIndex = L.index(min_value)
    L[i], L[minIndex] = L[minIndex], L[i]

print("Sorted list", L)
'''

'''

"""Selection sort algorithm """
sum = int(input("How many numbers do you want type? "))
L = [int(input("Enter number: ")) for x in range(sum)]

print("Unsorted list: ", L)
for j in range(len(L)):
    mini_value = L[j]
    index_value = j
    counter = j

    for i in range(j, len(L)):
        if L[i] < mini_value:
            mini_value =  L[i]
            index_value = counter

        counter+=1
    L[j], L[index_value] = L[index_value], L[j]
    # temp = L[j]
    # L[j] = mini_value
    # L[index_value] = temp

print("Sorted list: ", L)

'''


'''
# Multiple Argument:

def myAddUniversal(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum
sum1 = myAddUniversal(20, 30, 19, -45, 9.4, -17)
print(sum1)

'''

'''
# Dictionary argument: 

def printAllVariableNamesAndValues(**args):
    for x in args:
        print("Key name is: ", x, "And value name: ",args[x])

printAllVariableNamesAndValues(a = 3, b = 4.5, c = "eight", d = "aabb")

'''


'''
num = int(input("How namy numbers do want to sort: "))
#list1 = [10, 15, 4, 23, 0]
list1 = [int(input("Enter numbers: ")) for x in range(num)]

print("Unsorted list: ", list1)

for j in range(len(list1)-1):
    for i in range(len(list1) - 1-j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            

print("Sorted list: ",list1)





# Second approach
# Bubble sort algorithm:

list1 = [3, 10, 1, 9, 4]
for j in range(len(list1)):
    for i in range(len(list1)-1-j):
        if list1[i] > list1[i+1]:
            #list1[i], list1[i+1] = list1[i+1], list1[i]
            temp = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = temp
# assign the first index value to temp (list[i])
# swap it with whatever the index of the second value plus one is (list[i+1])
# assign the temp back to whatever the index of the first plus one is (list[i+1])
print(list1)

# Bubble sort
# Check if the first value is greater than the second value then swap it
# Otherwise, do nothing
# Repeat step two.

'''


'''
SELECTION SORT USING FUNCTION TO SOLVE A PROBLEM: 


# Find the minimum value
  # Store the first index value in a variable
  # Compare if the first index value is less than any index value in the list
  # If yes: Store that index number in the variable, else: do nothing
# Swap the minimum value
# Sort the list
# Repeat step 1 till the you finish the whole list

def checkIfNotNumeric(L):
    for x in L:
        if not(isinstance(x, (int, float))):
            return False
    return True


def findMinimumValue(L, startInd):
    m = L[startInd]
    counter = startInd
    indexNum = startInd
    for i in range(startInd, len(L)):
        if L[i] < m:
            m = L[i]
            indexNum = counter
        counter+=1

    return indexNum

def swapIndexValues(L, iterValue, indexValue):
    L[indexValue], L[iterValue] = L[iterValue], L[indexValue]

    return L


def sortTheList(L):
    if not(checkIfNotNumeric(lis)):
        print("Error: list values are not numeric! ")
        return False
    else:
        for j in range(len(L)):
            indexNum = findMinimumValue(L, j)
            swapIndexValues(L, j, indexNum)

    return L

lis = [3, 1, 5, 9, 0, -3]
L = sortTheList(lis)
print(L)


#L = sortList(lis)
#print(L)



num = int(input("Enter how many numbers you want to sort: "))

list1 = [int(input("Enter numbers: ")) for x in range(num)]
a = findMin(list1)

print("You entered: ", list1)
print("The minimum value and it's index: ",a)
'''


def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)

        i = 0
        j = 0
        k = 0

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


L = [2, 5, 1, 8, -1, 0, 4]

mergesort(L)
print(L)




















