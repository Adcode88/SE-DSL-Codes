#New Better Version

SE = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
C = ["a","c","e","g","h","l"] #cricket
B = ["c","d","f","g","i","k"] #badminton
F = ["a","b","d","f","h","i","j","k"] #football

def intersection(X,Y):
    C=[]
    for i in range(len(X)):
        for j in range(len(Y)):
            if(X[i]==Y[j]):
                C.append(X[i])
    return C

def union(X,Y):
    C=[]
    for i in range(len(X)):
        C.append(X[i])
    for i in range(len(Y)):
        C.append(Y[i])
    for i in range(len(intersection(X,Y))):
        C.remove((intersection(X,Y))[i])
    return C

def remove(X,Y):
    C=[]
    for i in range(len(X)):
        C.append(X[i])
    for i in range(len(X)):
        for j in range(len(Y)):
            if (X[i] == Y[j]):
                C.remove(X[i])
    return C


print("TO FIND:\n"
      "1)The Students who play both cricket and badminton press 1 \n"
      "2)The Students who play either cricket or badminton but not both press 2 \n"
      "3)The Students who play neither cricket nor badminton press 3 \n"
      "4)The Students who play cricket and football but no badminton press 4 \n"
      "5)To Exit Press 5")

while(1>0):
    inputt = (int(input("\nENTER YOUR CHOICE:")))

    if(inputt==1):
        print(intersection(C,B))
    elif(inputt==2):
        print(remove(union(C,B),intersection(C,B)))
    elif(inputt==3):
        print(remove(remove(SE,C),B))
    elif(inputt==4):
        print(remove(intersection(C,F),B))
    elif(inputt==5):
        print("Exited")
        break
    else:
        print("Invalid Input")


#Older Version
'''
#SE = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
#A = ["a","c","e","g","h","l"] #cricket
#B = ["c","d","f","g","i","k"] #badminton
#C = ["a","b","d","f","h","i","j","k"] #football

SE=[]
A=[]
B=[]
C=[]

def CUB():
    AorB=[]
    AandB=[]
    Universal=[]
    AorC=[]
    i = 0
    while (i < len(A)):
        holder1 = A[i]
        j = 0
        i = i + 1
        while (j < len(B)):
            holder2 = B[j]
            j = j + 1
            if (holder1 == holder2):
                AandB.append(holder1)
    i=0
    while(i<len(A)):
        AorB.append(A[i])
        i=i+1
    i=0
    while(i<len(B)):
        AorB.append(B[i])
        i=i+1
    i=0
    while(i<len(AandB)):
        AorB.remove(AandB[i])
        i=i+1
    i=0
    while(i<len(AandB)):
        AorB.remove(AandB[i])
        i=i+1
    print("Cricket Or Badminton But Not Both =", AorB)

def CIntB():
    AorB=[]
    AandB=[]
    Universal=[]
    AorC=[]
    i=0
    while(i<len(A)):
        holder1 = A[i]
        j=0
        i=i+1
        while(j<len(B)):
            holder2 = B[j]
            j=j+1
            if(holder1==holder2):
                AandB.append(holder1)
    print("Both Cricket and Badminton =", AandB)

def NCNB():
    AorB=[]
    AandB=[]
    Universal=[]
    AorC=[]
    i=0
    while(i<len(SE)):
        Universal.append(SE[i])
        i=i+1
    i=0
    while(i<len(A)):
        AorB.append(A[i])
        i=i+1
    i=0
    while(i<len(B)):
        AorB.append(B[i])
        i=i+1
    i=0
    while(i<len(A)):
        holder1 = A[i]
        j=0
        i=i+1
        while(j<len(B)):
            holder2 = B[j]
            j=j+1
            if(holder1==holder2):
                AorB.remove(holder1)
    i=0
    while(i<len(AorB)):
        Universal.remove(AorB[i])
        i=i+1
    print("No Cricket No Badminton=", Universal)

def CFNB():
    AorB=[]
    AandB=[]
    Universal=[]
    AorC=[]
    i=0
    while(i<len(A)):
        holder1 = A[i]
        j=0
        i=i+1
        while(j<len(C)):
            holder2 = C[j]
            j=j+1
            if(holder1==holder2):
                AorC.append(holder1)
    i=0
    while(i<len(AorC)):
        holder1 = AorC[i]
        j=0
        i=i+1
        while(j<len(B)):
            holder2 = B[j]
            j=j+1
            if(holder1==holder2):
                AorC.remove(holder1)
    print("Cricket and Football But No Badminton=", AorC)


s=int(input("Enter number of second year students:"))
print("Enter all roll numbers of second year students")
i=0
while(i<s):
    SE.append(int(input("roll no:")))
    i=i+1

a=int(input("Enter number of cricket students:"))
print("Enter all roll numbers of cricket students")
i=0
while(i<a):
    A.append(int(input("roll no:")))
    i=i+1

b=int(input("Enter number of badminton students:"))
print("Enter all roll numbers of badminton students")
i=0
while(i<b):
    B.append(int(input("roll no:")))
    i=i+1

c=int(input("Enter number of football students:"))
print("Enter all roll numbers of badminton students")
i=0
while(i<c):
    C.append(int(input("roll no:")))
    i=i+1

print("TO FIND:"
      "1)The Students who play both cricket and badminton press 1 \n"
      "2)The Students who play either cricket or badminton but not both press 2 \n"
      "3)The Students who play neither cricket nor badminton press 3 \n"
      "4)The Students who play cricket and football but no badminton press 4 \n"
      "5)To Exit Press 5")

while(1>0):
    inputt = (int(input("\nENTER YOUR CHOICE:")))

    if(inputt==1):
        CIntB()
    elif(inputt==2):
        CUB()
    elif(inputt==3):
        NCNB()
    elif(inputt==4):
        CFNB()
    elif(inputt==5):
        print("Exited")
        break
    else:
        print("Invalid Input")
    
'''