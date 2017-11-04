# split up a paragraph into sentences
# using regular expressions


def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list '''
    import re
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList


if __name__ == '__main__':
    p = """This is a sentence.  This is an excited sentence! And do you think this is a question?"""

    sentences = splitParagraphIntoSentences(p)
    for s in sentences:
        print (s.strip())

#output:
#   This is a sentence
#   This is an excited sentence

#   And do you think this is a question