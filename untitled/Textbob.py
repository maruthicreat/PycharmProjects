import nltk
from textblob import TextBlob


sen = TextBlob('its is  very good.')

print(sen.tags)
print(sen.sentiment.polarity)