def BOB():
    for i in range(99, -1, -1):
        if i == 1:
            print(i, "bottles of beer on the wall,", i, "bottle of beer.")
            print("Take one down, pass it around,", i-1, "bottles of beer on the wall.")

        elif i == 0:
            print("No more bottles of beer on the wall.")

        else:
            print(i, "bottles of beer on the wall,", i, "bottle of beer.")
            print("Take one down, pass it around,", i - 1, "bottles of beer on the wall.")

BOB()