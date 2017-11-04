import re

filename = input("Enter the File name you would like to open:")

def FileValidation(filename):
    if filename.endswith('.txt'):
        a = open(filename, 'r')
        paragraph = a.read()
        SentenceSplitter(paragraph)
    else:
        print("Invalid Input")

def SentenceSplitter(paragraph):

	paragraph = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', paragraph)
	paragraph = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])',paragraph)
   	for i in paragraph:
            print(i)

FileValidation(filename)