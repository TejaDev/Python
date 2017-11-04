string = input("enter the String:")
print("you entered:", string)

def translator(x):
    consonants = 'bcdfghjklmnpqrstvwxz'
    translated = ""
    for i in string:
        if i in consonants:
            translated += i + 'o' + i
        else:
            translated += i

    return translated

print(translator(string))

