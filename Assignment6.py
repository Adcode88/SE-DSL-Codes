def partition(array,low, high):
    pivot=array[high]
    i=low-1
    j=low
    while(j<=(high-1)):
        if(array[j]<pivot):
            i=i+1
            cont=array[j]
            array[j]=array[i]
            array[i]=cont
        j=j+1
    cont=array[i+1]
    array[i+1]=array[high]
    array[high]=cont
    return (i+1)

def quicksort(array, low, high):
    if(low<high):
        pi=partition(array, low, high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

array2=[]

n=int(input("Enter number of elements in array:"))
m=0
while(m<n):
    array2.append(int(input("enter element:")))
    m=m+1

print("Entered array is:", array2)

quicksort(array2,0,(len(array2)-1))
print("sorted array is:", array2)