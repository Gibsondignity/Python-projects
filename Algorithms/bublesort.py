L = [4, 1, 5, -5, 3, 6, -1, 8, -4]

for j in range(len(L)):
    for i in range(len(L)-1-j):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]  

print(L)