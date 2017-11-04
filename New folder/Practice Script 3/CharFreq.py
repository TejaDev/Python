def char_freq(a):
    b = {}
    for i in a:
        b[i] = b.get(i, 0) + 1
    print(b)

char_freq("abbabcbdbabdbdbabababcbcbab")
