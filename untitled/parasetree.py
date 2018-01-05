import nltk

groucho_grammar = nltk.CFG.fromstring(
"""
s -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP pp
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

sent = ['elephant', 'I', 'in', 'shot', 'an', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)


