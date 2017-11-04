def convertsentence(mylist):
    for x in mylist:
        if len(x)==3 and x[0].isupper() and x[1].islower() and x[2]=='.':
            print(x,end=" ")
        elif len(x)==4 and x[0].islower() and x[1]=='.' and x[2].islower() and x[3]=='.':
            print(x,end=" ")
        elif x[-1]=='.':
            print(x)
        elif x[-1]=='?':
            print(x)
        else:
            print(x,end=" ")

filename=input("Please enter a file name: ")
if filename == '':
    print("Need to enter a filename.")
    exit()


fr=open(filename,'r')
mylist=fr.readlines()
fr.close()

sentence=mylist[0].rstrip()
list=sentence.split()
convertsentence(list)