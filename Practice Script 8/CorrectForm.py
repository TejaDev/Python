import re

verb = input("Enter the Word:")

def correct_form(x):
    es = ('o', 'ch', 's', 'sh', 'x', 'z')
    if x.endswith('y'):
        return re.sub('y$', 'ies', x)
    elif x.endswith(es):
        return x + 'es'
    else:
        return x + 's'

print(correct_form(verb))