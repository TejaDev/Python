import re

filename = input("Enter the File name you would like to open:")
a=open(filename,'r')
paragraph = a.read()

def sentence_splitter(paragraph):

        sentences = re.sub(r'\n', '', paragraph)
        sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)
        sentences = re.sub(r'!\s', '!\n', sentences)
        sentences = re.sub(r'\?\s', '?\n', sentences)
        print (sentences)

sentence_splitter(paragraph)
