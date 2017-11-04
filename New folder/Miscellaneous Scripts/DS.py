import re

def sentence_splitter(data):
    with open('data.txt', 'r') as file:
        text = file.read()

    text = re.sub("\n", "", text)
    text = re.sub("!\s", "!\n", text)
    text = re.sub(r"\?\s", "?\n", text)
    text = re.sub(r'(?<!Mr)(?<!Ms)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', text)
    print(text)

sentence_splitter('data.txt')