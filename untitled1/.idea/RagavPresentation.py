import nltk
from nltk.corpus import stopwords

def detection(paragraph):
    word = nltk.word_tokenize(paragraph)  # tokenizing the words in a paragraph
    print(word)
    stop = set(stopwords.words('english'))
    wordopt = [i for i in word if i not in stop]  # removing stop words
    word_pos = nltk.pos_tag(wordopt)
    noun_words = [r for r, pos in word_pos if pos in ["NN","NNS","NNP","NNPS"]]
    print(noun_words)



paragraph="""Definition: A stack is push an orderex list in which insertion and deletion and done at
            one end , where the end is called as top . The last element iserted is the first one to be deleted. Hence, it
            is called Last in First out (LIFO) or First in Last out (FILO) list."""
detection(paragraph)