message = input("please enter your log message:")
if message == '':
    print("Need to enter a message.")
    exit()

file = open('log.txt','r')

data = file.read()

temp = ''
def CLS(data):
    if message != '':
        data[0] = data[0].append(message)
        print(data)

CLS(data)