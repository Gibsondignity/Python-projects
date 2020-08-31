L = [4, 1, 5, -5, 3, 6, -1, 8, -4]

for j in range(len(L)):
    minValue = L[j]
    minIndex = j
    counter = j

    for i in range(j, len(L)):
        if L[i] < minValue:
            # set the minimum value to minValue whenever the L[i] is less than the minValue
            minValue = L[i]
            # set the current index to the minIndex whenever the the condtion is true
            minIndex = counter
        # Keep track of the index 
        counter+=1

    # swap the minimum index with the very first value
    temp = L[j]
    L[j] = minValue
    L[minIndex] = temp
    # or
    #L[j], L[minIndex] = L[minIndex], L[j]

#print(L)
#print(f"The minimum value is: { minValue } and the index of the minimum value is: { minIndex }")


# Using functions
L = [4, 1, 5, -5, 3, 6, -1, 8, -4]

# Function to find the minimum index
def findMinimum(list1, theRange):
    minValue = list1[theRange]
    minIndex = theRange
    counter = theRange
    for i in range(theRange, len(list1)):
        if list1[i] < minValue:
            minValue = list1[i]
            minIndex = counter
        counter+=1

    return minIndex

# Function to minimum value with the first value
def swapValue(L, min_Index, iter_value):
    L[min_Index], L[iter_value] = L[iter_value], L[min_Index]
    return L


def checkList(List3):
    for x in List3:
        if not(isinstance(x, (int,float))):
            return False
    return True



def sortTheList(L):
    if not(checkList(L)):
        print("Invalid list: List does not contain numeric values")
        return False
    else:
        for j in range(len(L)):
            min_index = findMinimum(L, j)
            swapValue(L, min_index, j)
        return L

final_sorted_list = sortTheList(L)

#minIndex = findMinimum(L)
#theList = swapValue(L, minIndex, 0)

print(final_sorted_list)


