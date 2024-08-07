def bubsort(array1):gh
    i=0
    while(i<length1):
        j=0
        while(j<length1-1):
            if(int(array1[j])>int(array1[i])):
                container=array1[i]
                array1[i]=array1[j]
                array1[j]=container
            j=j+1
        i=i+1

array1=[]
i=0
length1=int(input("Enter number of students who attended training program:"))
print("")
while(i<length1):
    array1.append(input("Enter roll number of students who attended training program:"))
    i=i+1
bubsort(array1)
print("\nThe roll numbers of training program attendees are:",array1,"\n")
inputt=input("Enter roll number to be searched:")
array2=array1

def linear():
    print("\nLinear:")
    a=0
    count=0
    while(a<length1):
        if(array1[a]==inputt):
          count=count+1
          break
        a=a+1
    if(count>0):
      print("Roll No.", inputt, "attended the training program \n")
    else:
      print("Roll No.", inputt, "did not attend the training program \n")

def sentinel():
    print("Sentinel:")
    store=array1[(length1-1)]
    array1[(length1-1)]=inputt
    a=0
    while(array1[a]!=inputt):
        a=a+1
    array1[(length1-1)]=store
    if((a<(length1-1)) or (array1[a]==inputt)):
        print("Roll No.", inputt, "attended the training program \n")
    else:
        print("Roll No.", inputt, "did not attend the training program \n")


def binaryiterative():
    print("Binary Iterative:")
    array2=array1
    c=0
    while(len(array2)>=1):
        h=int((len(array2)-1)/2)
        if(inputt==array2[h]):
            c=c+1
            break
        elif(inputt<array2[h]):
            j=0
            array3=[]
            while(j<h):
                array3.append(array2[j])
                j=j+1
            array2=array3
        elif(inputt>array2[h]):
            j=h+1
            array3=[]
            while(j<len(array2)):
                array3.append(array2[j])
                j=j+1
            array2=array3
    if(c>0):
        print("Roll No.", inputt, "attended the training program \n")
    else:
        print("Roll No.", inputt, "did not attend the training program \n")


def binaryrec(array):
    i=0
    if(len(array)>=1):
        h=(len(array)-1)//2
        if(inputt==array[h]):
            return h
        elif(inputt<array[h]):
            j=0
            array5=[]
            while(j<h):
                array5.append(array[j])
                j=j+1
            array=array5
            return binaryrec(array)
        elif(inputt>array[h]):
            j=h+1
            array5=[]
            while(j<len(array)):
                array5.append(array[j])
                j=j+1
            array=array5
            return binaryrec(array)
        if(len(array)<3):
            i=i+1
    else:
        return -1

def fibiterative():
    print("Fibonacci Iterative:")
    n=len(array1)
    offset=-1
    pointer1=0
    pointer2=1
    pointer3=pointer1+pointer2
    while(pointer3<n):
        pointer1=pointer2
        pointer2=pointer3
        pointer3=pointer1+pointer2
    while(pointer3>1):
        i=min(offset+pointer1,n-1)
        if(array1[i]==inputt):
            c=1
            break
        elif(inputt<array1[i]):
            pointer3=pointer1
            pointer2=pointer2-pointer1
            pointer1=pointer3-pointer2
            c=0
        else:
            pointer3=pointer2
            pointer2=pointer1
            pointer1=pointer3-pointer2
            offset=i
            c=0
    if(pointer2 and array1[n-1] == inputt):
        c=1

    if (c==1):
        print("Roll No.", inputt, "attended the training program \n")
    else:
        print("Roll No.", inputt, "did not attend the training program \n")



linear()
sentinel()
binaryiterative()
print("Binary Recursive:")
if(binaryrec(array2)!=-1):
    print("Roll No.", inputt, "attended the training program \n")
else:
    print("Roll No.", inputt, "did not attend the training program \n")
fibiterative()


while(1<2):
    print("To search new element press 1 \nTo enter new array press 2 \nTo exit press 3 \n")
    inp=int(input("Enter input:"))
    print("")
    if(inp==1):
        inputt=input("Enter roll number to be searched:")
        linear()
        sentinel()
        binaryiterative()
        print("Binary Recursive:")
        if (binaryrec(array2)!=-1):
            print("Roll No.",inputt,"attended the training program \n")
        else:
            print("Roll No.",inputt,"did not attend the training program \n")
        fibiterative()
    elif(inp==2):
        array1=[]
        i=0
        length1=int(input("Enter number of students who attended training program:"))
        print("")
        while(i<length1):
            array1.append(input("Enter roll number of students who attended training program:"))
            i=i+1
        bubsort(array1)
        print("\nThe roll numbers of training program attendees are:", array1,"\n")
        inputt = input("Enter roll number to be searched:")
        array2 = array1
        linear()
        sentinel()
        binaryiterative()
        print("Binary Recursive:")
        if(binaryrec(array2)!=-1):
            print("Roll No.",inputt,"attended the training program \n")
        else:
            print("Roll No.",inputt,"did not attend the training program \n")
        fibiterative()
    elif(inp==3):
        break
    else:
        print("Invalid Input")