file = open('words.txt', 'r')  # Open the file for reading.

data =  file.read()  # Read the contents of the file in to memory

def Convert_ICAO(x):
    output = ''
    #List = []
    d = {   "a": "alpha",
            "b": "bravo",
            "c": "charlie",
            "d": "delta",
            "e": "echo",
            "f": "foxtrot",
            "g": "golf",
            "h":"hotel",
            "i":"india",
            "j":"juliett",
            "k":"kilo",
            "l":"lima",
            "m":"mike",
            "n":"november",
            "o":"oscar",
            "p":"papa",
            "q":"quebe",
            "r":"romeo",
            "s":"sierra",
            "t":"tango",
            "u":"uniform",
            "v":"victor",
            "w":"whiskey",
            "x":"x-ray",
            "y":"yankee",
            "z":"zulu"  }
    for word in data:
        for i in word:
            if i in d:
                output = output + d[i] + "-"
    print(output)

print(Convert_ICAO(file))