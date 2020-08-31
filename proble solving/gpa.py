import pandas as pd 
from collections import defaultdict

def StudentRecords():
    D = defaultdict(list)
    inc = 1
    while True:
        course_code = input("\nEnter course code: ")
        course = input("Enter course "+ str(int(inc)) +": ")
        marks = input("Enter marks: ")
        credit_hours = input("Enter credit hours: ")
        inc+=1

        if course_code in D:
            print(course_code + " is already taken!")
        else:
            D["Code"].append(course_code)
            D["Course_Title"].append(course)
            D["Mark"].append(marks)
            D["Credit"].append(credit_hours)

        more = input("Do you want to add more? ") 
        if more.upper() == "NO":
            return D

# Diction = StudentRecords()
# print(Diction)

# myRecords = pd.DataFrame(Diction)
# print(myRecords)


D = {"Marks": ['1', '3', '6', '8', '89'], "course_code": ['IT 171', 'IT 324', 'IT212']}
'''
for x in D:
    L = D[x]
    sum_of_num = 0
    for i in L:
        num = int(i)
        sum_of_num+=num
'''

for x in D:
    new_d = 
    print(D[x])




