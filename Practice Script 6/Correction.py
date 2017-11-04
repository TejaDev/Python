a = input("Enter the String for Correction: ")

def space():
    string = a
    while '  ' in string:
        string = string.replace('  ', ' ')
    return string

alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&,'
def alphabet(string):
    temp = ''
    for x in string:
        if x in alphabets:
            temp += x
        elif x == ' ':
            temp += ' '
        elif x == ".":
            temp += '. '
    return temp

print(alphabet(space()))