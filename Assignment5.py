array1=[]

def inputt():
    i=0
    length=int(input("Enter number of scores to be sorted:"))
    print("")
    while(i<length):
        array1.append(input("Enter scores:"))
        i=i+1
    print("Entered array is", array1)
    print("")

def bubsort():
    k=0
    global array2
    array2=[]
    while(k<len(array1)):
        array2.append(array1[k])
        k=k+1
    print("Bubble Sort:")
    i=0
    while(i<len(array2)):
        j=0
        while(j<len(array2)-1):
            if(int(array2[j])>int(array2[i])):
                container=array2[i]
                array2[i]=array2[j]
                array2[j]=container
            j=j+1
        i=i+1
    print(array2)
    print("")

def selectsort():
    global array2
    k=0
    array2=[]
    while(k<len(array1)):
        array2.append(array1[k])
        k=k+1
    print("Selection Sort:")
    i=0
    while(i<len(array2)):
        j=i
        container=array2[j]
        a=j
        while(j<len(array2)):
            if(array2[j]<container):
                container=array2[j]
                a=j
            j=j+1
        array2[a]=array2[i]
        array2[i]=container
        i=i+1
    print(array2)
    print("")

def insertsort():
    global array2
    k=0
    array2=[]
    while(k<len(array1)):
        array2.append(array1[k])
        k=k+1
    print("Insertion Sort:")
    i=0
    while(i<len(array2)):
        j=0
        while(j<len(array2)-1):
            while(int(array2[j+1])<int(array2[j]) and j>=0):
                container=array2[j]
                array2[j]=array2[j+1]
                array2[j+1]=container
                j=j-1
            j=j+1
        i=i+1
    print(array2)
    print("")

def shellsort():
    global array2
    k = 0
    array2 = []
    while (k < len(array1)):
        array2.append(array1[k])
        k = k + 1
    print("Shell Sort:")

    n = len(array2)
    interval = (n // 2)
    while (interval > 0):
        for i in range(interval, n):
            cont = array2[i]
            j = i
            while (j >= interval and array2[j - interval] > cont):
                array2[j] = array2[j - interval]
                j = j - interval
            array2[j] = cont
        interval = interval // 2
    print(array2)
    print("")



while(1<2):
    print("To Start press 0 \nTo bubble sort press 1 \nTo selection sort press 2 \nTo insertion sort press 3 \nTo shell sort press 4 \nTo display entered array press 5 \nTo display sorted array press 6 \nTo enter new array press 7 \nTo exit press 8 \n")
    inp=int(input("Enter input:"))
    print("")
    if(inp==0):
        inputt()
    elif(inp==1):
        bubsort()
    elif(inp==2):
        selectsort()
    elif(inp==3):
        insertsort()
    elif(inp==4):
        shellsort()
    elif(inp==5):
        print("Entered array is:", array1)
        print("")
    elif(inp==6):
        print("Sorted array is:", array2)
        print("")
    elif(inp==7):
        array1=[]
        array2=[]
        inputt(array1)
    elif(inp==8):
        print("Exited")
        break
    else:
        print("Invalid Input \n")