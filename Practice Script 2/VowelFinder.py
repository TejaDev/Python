def vowel(x):
    if x.lower() in a:
        return True
    else:
        return False

x = input("enter an alphabet:")
a = ['a','e','i','o','u']

print(format(vowel(x)))