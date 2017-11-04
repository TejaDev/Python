def palindrome1(x):
    for i in open(x).read().split('\n'):
        if i == i[::-1]:
            print(i + " is palindrome")


palindrome1('polindrome.txt')


def palindrome2(x):
    for i in open(x).readlines():
        i = i.rstrip()
        if i == i[::-1]:
            print(i + " is palindrome")


palindrome2('polindrome.txt')
