
import nltk



sentence = """A customer can make a cash withdrawal from his account.  
A customer can make a deposit to any account.
The customer will enter the amount of the deposit into the ATM.
ragav is going to kill the lion. 
im am good boy."""

grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """

sent_token = nltk.sent_tokenize(sentence)

for sent in sent_token :
    #print(sent)
    #word=nltk.word_tokenize(sentence)

    word_pos=nltk.pos_tag(nltk.word_tokenize( sent))
    #print(word_pos)
    cp = nltk.RegexpParser(grammar,loop=2)
    result = cp.parse(word_pos)
    print(result)
    #print(result.label())

    #print(result.productions())
   # prores = result.productions()
    #for i in prores:
     #   print(i)
    #result.draw()

    for i in result.subtrees():
        print(i.label())
     #   print(i.lable())
        #print(tuple(f for f in i))

   #print(i for i in result)
    #result.draw()


#grammar = "NP: {<DT>?<JJ>*<NN>}"


