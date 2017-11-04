letters = 'abcdefghijklmnopqrstuvwxyz'
flag = 0

file = open('pangram.txt', 'r')
data =  file.read()

def pangram(x):
    for i in letters[:26]:
        if i in x.lower():
            flag = 1
        else:
            print ('not a pangram')
            flag = 0
            break

    if flag == 1:
        print ('pangram')


pangram(data)