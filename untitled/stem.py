from nltk import pos_tag
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
import re

ss = SnowballStemmer("english")
ps = PorterStemmer()
ws = WordNetLemmatizer()
example_words = ["jealous","jealousy","facilitator","directors","having","moderator","buys"]
lemwords=[]
print(pos_tag(example_words))
reg ='NN.*'
for word,pos in pos_tag(example_words):
    if(re.match(reg,pos)):
       # print(word)
        lemwords.append(ws.lemmatize(word))
    else:
        print(ps.stem(word))

print(lemwords)
print(" ")
for w in example_words:
    print(ps.stem(w))

print(" ")
for w in example_words:
    print(ss.stem(w))
