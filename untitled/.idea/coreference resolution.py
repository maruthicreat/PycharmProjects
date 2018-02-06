import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'G:\JavaLibraries\stanford-corenlp-full-2017-06-09', quiet=False)
props = {'annotators': 'coref', 'pipelineLanguage': 'en'}

text = 'Barack Obama was born in Hawaii.  He is the president. Obama was elected in 2008.'
result = json.loads(nlp.annotate(text, properties=props))

num, mentions = result['corefs'].items()[0]
for mention in mentions:
    print(mention)