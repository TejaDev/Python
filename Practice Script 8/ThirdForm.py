word = input('Please enter a word: ')

def correct_form(word):
    if word[len(word)-1] == 'o' or word[len(word)-1] == 's' or word[len(word)-1] == 'x' or word[len(word)-1] == 'z':
        word = word + 'es'
        print (word)
    elif word[len(word)-2] == 'c' and word[len(word)-1] == 'h':
        word = word + 'es'
        print(word)
    elif word[len(word)-2] == 's' and word[len(word)-1] == 'h':
        word = word + 'es'
        print(word)
    elif word[len(word)-1] == 'y':
        word = word[:-1]
        word = word + 'ies'
        print(word)
    else:
        word = word + 's'
        print(word)

correct_form(word)