
import nltk


from nltk.corpus import stopwords

sentence = """it is good but not bad"""

grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """

#[('it', 'PRP'), ('is', 'VBZ'), ('good', 'JJ'), ('but', 'CC'), ('not', 'RB'), ('bad', 'JJ')]

sent_token = nltk.sent_tokenize(sentence)
stop = set(stopwords.words('english'))
print(stop)
for sent in sent_token :
    print(sent)
    word = nltk.word_tokenize(sent)
    print(word)
    sort_word = [ i for i in word if i not in stop ]
    word_pos=nltk.pos_tag(sort_word)
    print(word_pos)
    cp = nltk.RegexpParser(grammar,loop=2)
    result = cp.parse(word_pos)
    print(result)
    result.draw()



