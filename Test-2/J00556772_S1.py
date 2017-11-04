import re
import os

filename = input("Enter the File name you would like to open:")

def FileValidation():
    if (os.path.isfile(filename)):
        a = open(filename, 'r')
        paragraph = a.read()
        print(SentenceSplitter(paragraph))
    else:
        print(" File Format Error !!!!!!!!! Check your file format please")

def SentenceSplitter(paragraph):

        sentences = re.sub(r'\n', '', paragraph)
        sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)
        sentences = re.sub(r'!\s', '!\n', sentences)
        sentences = re.sub(r'\?\s', '?\n', sentences)
        return sentences

FileValidation()