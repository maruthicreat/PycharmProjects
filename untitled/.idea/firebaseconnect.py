from firebase import firebase
import nltk
import json
from pprint import pprint
firebase = firebase.FirebaseApplication('https://smartshoppingfinal.firebaseio.com/', None)
result = firebase.get('/Review',None)
for d in result:
    print(result[d]['print'])

#print(result.draw())
#new_user = 'it is soo good'
#result = firebase.post('/Review', {'print': 'silent','url':'hai'})
#print(result)