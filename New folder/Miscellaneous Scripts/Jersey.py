number = input("Enter a #:")
print(number)

filename = input("Enter the File name you would like to open:")
a = open(filename, 'r')
data = a.readlines()
for i in
print(data)

def function():
    if number in data :
        print(True)
        #b = open('new', 'w' )
    else:
        print(False)

function()