def make_3sg_form():
    Word = input('Enter a word: ')
    if Word.endswith('y'):
        New_word=Word[:-1]+'ies'

    elif Word.endswith(('o', 'ch', 's', 'sh', 'x' ,'z')):
        New_word=Word+'es'

    else:
        New_word=Word+'s'
    print(New_word)
make_3sg_form()