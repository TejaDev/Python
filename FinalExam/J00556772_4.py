#prompt for entering file name
filename=input("Please enter a file name: ")

#prevents user from entering null file name
if filename == '':
    print("Need to enter a filename.")
    exit()

fr=open(filename,'r')
data=fr.read()
#fr.close()

print(data)

for i in int(data):
    if (int(i) > 19999) or (int(i)<29000):
        output_file = open('results.txt', 'w')
        print("i")
print(data)