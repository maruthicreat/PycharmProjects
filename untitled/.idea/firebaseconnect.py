from firebase import firebase
firebase = firebase.FirebaseApplication('https://smartshoppingfinal.firebaseio.com/', None)
result = firebase.get('/CustomerSignup','2oboeR8MUNe1eJsTkogZZAj9c0D3')
print(result)
