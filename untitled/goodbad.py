from collections import Counter

def readwords( filename ):
    f = open(filename)
    words = [line.rstrip().split() for line in f.readlines()]
    print(words)
    return words

positive = readwords('positive.txt')
negative = readwords('negative.txt')

paragraph = 'its good but not bad'

count = Counter(paragraph.split())
print(count)
pos = 0
neg = 0
for key,val in count.most_common():
    key = key.rstrip('.,?!\n')# removing possible punctuation signs
    posiv = [posiv for sub in positive for posiv in sub]
    negiv = [negiv for sub in negative for negiv in sub]
    print (posiv)
    if key in posiv:
        pos += val
    if key in negiv:
        neg += val

print (pos, neg)