import pattern
from pattern import parse
s = 'The mobile web is more important than mobile apps.'
s = parse(s, relations=True, lemmata=True)
print (s)