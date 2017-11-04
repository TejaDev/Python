string = input("enter the String:")
print("you entered:", string)

consonants = 'bcdfghjklmnpqrstvwxz'

translated = ""
for i in string:
    if i in consonants:
        translated += i + 'o' + i
    else:
        translated += i

print(translated)
