'''  
Let say you are a teacher and you have different student
records containing id of a student and the marks list in each subject
where different students have taken different number of subjects. All 
these records are in hard copy. You want to enter all the data in computer
want to compute the average marks and display
'''
import pandas as pd
def studentRecords():
    D = {}
    while True:
        
        studentID = input("\nEnter student id: ")
        marks = input("\nEnter student\'s marks in comma seperated value: ")
        

        if studentID in D:
            print(studentID, "Student id has already taken. Choose different one ")
        else:
            D[studentID] = marks.split(",")

        isMore = input("\nDo you want add more students? Yes or No: ")
        if isMore.upper() == "NO":
            return D

def displayMarks(D):
    averageMarks = {}
    for x in D:
        L = D[x]
        sm = 0

        for marks in L:
            sm += int(marks)
            
        averageMarks[x] = sm/len(L) 

    return averageMarks


Diction = studentRecords()
#records = displayMarks(Diction)


file1 = pd.DataFrame(Diction)
print(file1)

#print(records)

#for i in records:
#    print("The key is: ", i, "and the value is: ", records[i])

'''
loopsaa = True
D = {}
while loopsaa:
    
    name = input("Enter heading: ")
    contentV = input("Enter the values: ")
    D[name] = contentV.split(",")
    loopsaa+=1

    while loopsaa == 5:
        loopsaa = False
print(D)
'''
