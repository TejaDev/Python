a = input("Please enter your first name:")

def greet(name):
    if(name == ''):
        print("Need to enter your name!!")
        exit()
    else:
        print("Hello. Nice to meet you {}".format(name))

greet(a)