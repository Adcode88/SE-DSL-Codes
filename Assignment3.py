def matrix(list0,x,y):
    list1=[]
    i=0
    while(i<x):
        j=0
        while(j<y):
            list1.append(input(f"enter element of row {i+1} column {j+1}:"))
            j=j+1
        list0.append(list1)
        list1=[]
        i=i+1
    print(list0)

def sum(list1,list2):
    if(xa==xb & ya==yb):
        list0=[]
        list3=[]
        j=0
        while(j<ya):
            i=0
            while(i<xa):
                list0.append(int(list1[i][j])+int(list2[i][j]))
                i=i+1
            list3.append(list0)
            list0=[]
            j=j+1
        print(list3)
    else:
        print("matrices cannot be added as they have different orders")


def diff(list1,list2):
    if(xa==xb & ya==yb):
        list0=[]
        list3=[]
        j=0
        while(j<ya):
            i=0
            while(i<xa):
                list0.append(int(list1[i][j])-int(list2[i][j]))
                i=i+1
            list3.append(list0)
            list0=[]
            j=j+1
        print(list3)
    else:
        print("matrices cannot be added as they have different orders")


def prod(list1,list2):
    list3=[]
    list0=[]
    list4=[]
    sum=0
    if(ya==xb):
        i=0
        while(i<xa):
            j=0
            list0=[]
            while(j<yb):
                sum=0
                k=0
                while(k<ya):
                    sum=sum+(int(list1[i][k])*int(list2[k][j]))
                    k=k+1
                j=j+1
                list0.append(sum)
                list4.append(list0)
            i=i+1
            if(i==xa):
                a=0
                b=0
                while(a<xa):
                    list3.append(list4[b])
                    b=b+xa
                    a=a+1
        print(list3)

    else:
        print("matrices cannot be multiplied")


def trans(list1,x,y):
    list3=[]
    list0=[]
    j=0
    while(j<y):
        i=0
        while(i<x):
            list0.append(int(list1[i][j]))
            i=i+1
        list3.append(list0)
        list0=[]
        j=j+1
    print(list3)


lista=[]
listb=[]


print("for matrix a")
print("enter order of matrix")
xa=int(input("rows:"))
ya=int(input("columns:"))
print("order of matrix is", xa, "x", ya)
matrix(lista,xa,ya)


print("for matrix b")
print("enter order of matrix")
xb=int(input("rows:"))
yb=int(input("columns:"))
print("order of matrix is", xb, "x", yb)
matrix(listb,xb,yb)


while(1<2):
    print("to find sum press 1 \nto find subtraction press 2 \nto find product press 3 \nto find transpose press 4 \nto re-enter matrices press 5 \nto exit press 6")
    inp=int(input("enter input:"))
    if(inp==1):
        sum(lista,listb)
    elif(inp==2):
        diff(lista,listb)
    elif(inp==3):
        prod(lista,listb)
    elif(inp==4):
        print("to find transpose:\nfirst matrix press 1 \nsecond matrix press 2")
        putin=int(input("enter input:"))
        if(putin==1):
            trans(lista,xa,ya)
        elif(putin==2):
            trans(listb,xb,yb)
        else:
            print("invalid input")
    elif(inp==5):
        lista = []
        listb = []

        print("for matrix a")
        print("enter order of matrix")
        xa = int(input("rows:"))
        ya = int(input("columns:"))
        print("order of matrix is", xa, "x", ya)
        matrix(lista, xa, ya)

        print("for matrix b")
        print("enter order of matrix")
        xb = int(input("rows:"))
        yb = int(input("columns:"))
        print("order of matrix is", xb, "x", yb)
        matrix(listb, xb, yb)
    elif(inp==6):
        break
    else:
        print("invalid input")