file = open('data.txt', 'r')
data = file.read

#x = set(data)

number = input("Enter a #:")

def Validator(number):
    if number in data:
        print("The number" + number + "you have entered has been found")
    else:
        print("Invalid number")
        bad = input("please pick another #:")

Validator(number)
