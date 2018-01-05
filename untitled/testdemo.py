from PyQt5 import QtCore, QtGui, QtWidgets
import nltk
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem
from nltk.corpus import stopwords


"""sentence=I met Joan. I met your sister.

            All the kids were sleeping.

            The boy in the blue jeans says he'll do it.

            He bought her a beautiful red dress.

            Mom baked tasty chocolate cookies.

            Julia was thinking about her friends back home.

            Will you talk with these rude people?

            You are a true hero.

            My dog is my best friend."""

sentence = "All the kids were sleeping."
print(sentence)

grammar = r"""
  NP: {<DT|JJ.*|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  """

sent_token = nltk.sent_tokenize(sentence)
print(sent_token)
for s in sent_token:
    print(s)
stop = set(stopwords.words('english'))
#print(stop)
result=""
for sent in sent_token:
    word = nltk.word_tokenize(sent)
    print(nltk.pos_tag(word))
    #word_st = [i for i in word if i not in stop]
    #print(word_st)
    word_pos = nltk.pos_tag(word)
    #print(word_pos)
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(word_pos)

    for i in result.subtrees():
        print(i.label())
        print(i.leaves())
        word_st = i.leaves()
        #print([r for r,pos in word_st])
        w = [r for r,pos in word_st if r not in stop ]
        print(w)

print(result)
result.draw()