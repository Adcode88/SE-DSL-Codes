#new imrpoved code
strinput=str(input("Enter The String:"))

def longestword(strinput):
    strinput1=strinput+' '
    strword=''
    strtemp=''
    for i in strinput1:
        strtemp+=i
        if(i==" "):
            if(len(strtemp)>len(strword)):
                strword=strtemp
            strtemp=''
    print("Longest word is:",strword)

def frequency(strinput):
    ch=(input("Enter Character To Be Searched:"))
    count=0
    for i in strinput:
        if(i==ch):
            count=count+1
    print("Frequency of entered character is:",count)

def palindrome(strinput):
    strpal=''   
    strpal=strinput[::-1]
    if(strinput==strpal):
        print("Palindrome")
    else:
        print("Not Palindrome")

def index(strinput):
    substring=(input("Enter Substring To Be Searched:"))
    strinput1=strinput+' '
    strtemp=''
    count=0
    check=0
    index=0
    for i in strinput1:
        if(i!=" "):
            strtemp += i
        if(i==" "):
            if(strtemp==substring):
                print("index is:",index)
                check=1
            else:
                index=count+1
                strtemp=''
        count=count+1
    if(check==0):
        print("Substring not found")

def occurence(strinput):
    list1=[]
    strinput1=strinput+' '
    strtemp=''
    for i in strinput1:
        if(i!=" "):
            strtemp+=i
        if(i==" "):
            list1.append(strtemp)
            strtemp=''
    list2 = []
    for n in list1:
        list2.append(n)
    for i in range(len(list1)):
        count=0
        for j in range(len(list2)):
            if(list1[i]==list2[j]):
                count=count+1
                list2[j]=" "
        if(count>0):
            print("the word",list1[i],"occurs",count,"times in the entered string")





longestword(strinput)
frequency(strinput)
palindrome(strinput)
index(strinput)
occurence(strinput)




#old code
'''def leng(list):
    i = 0
    for a in list:
        i=i+1
    return i

class inputt:
    def inputt(self):
        self.strinput = str(input("enter your string:"))
        print("the string you entered is:", self.strinput)
    def longest(self):
        strinput1=""
        i=0
        while(i<leng(self.strinput)):
            strinput1+=self.strinput[i]
            i=i+1
        strinput1+=" "
        longe1=""
        longe2=""
        longe3=""
        longemax=""
        i=0
        while(i<leng(strinput1)):
            longe1+=strinput1[i]
            if(strinput1[i]==" "):
                longe3=longe2
                longe2=longe1
                longe1=""
                if(leng(longe2)>leng(longe3)):
                    if(leng(longe2)>=leng(longemax)):
                        longemax=longe2
                elif(leng(longe3)>leng(longe2)):
                    if(leng(longe3)>=leng(longemax)):
                        longemax=longe3
            i=i+1
        print("longest word is:", longemax)

    def frequency(self):
        charact=input("enter character to be searched:")
        i=0
        j=0
        while(i<leng(self.strinput)):
            if (self.strinput[i]==charact):
                j=j+1
            i=i+1
        print('''"''',charact,'''"''', "occurs", j, "times in the entered string")

    def palindrome(self):
        revlist=""
        i=leng(self.strinput)-1
        while(i>=0):
            revlist+=self.strinput[i]
            i=i-1
        if(revlist==self.strinput):
            print("entered string is a palindrome")
        else:
            print("entered string is not a palindrome")


    def index(self):
        str1=""
        substrin=str(input("enter substring to be searched:"))
        if(substrin in self.strinput):
            i=0
            breakingcounter=0
            while (i<leng(self.strinput)):
                j=0
                i1=i
                while(j<leng(substrin)):
                    if (substrin[j]==self.strinput[i1]):
                        str1+=substrin[j]
                        a=i
                        j=j+1
                        i1=i1+1
                        if(str1==substrin):
                            breakingcounter=1
                            break
                    else:
                        str1=""
                        j=j+1
                    if(breakingcounter==1):
                        break
                i=i+1
                if(breakingcounter==1):
                    break
            print("the starting index of the entered substring is", a)
        else:
            print("entered string does not exist")

    def words(self):
        strinput1=""
        i=0
        while(i<leng(self.strinput)):
            strinput1+=self.strinput[i]
            i=i+1
        strinput1+=" "
        longe1=""
        listwords=[]
        i=0
        while(i<leng(strinput1)):
            longe1+=strinput1[i]
            if(strinput1[i]==" "):
                listwords.append(longe1)
                longe1=""
            i=i+1
        print("words are:", listwords)
        i=0
        while(i<leng(listwords)):
            character=listwords[i]
            x=leng(listwords)
            c=0
            j=0
            while(c<x):
                if(listwords[c]==character):
                    if(listwords[c]==" "):
                        l=1
                    else:
                        listwords[c]=" "
                        j=j+1
                c=c+1
            i=i+1
            if(character!=" "):
                print('''"''', character,'''"''', "occurs", j, "times in the entered string")

obj1=inputt()
obj1.inputt()
obj1.longest()
obj1.frequency()
obj1.palindrome()
obj1.index()
obj1.words()
'''