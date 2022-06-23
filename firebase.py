import pyrebase
import json
import os

config = {
  "apiKey": "AIzaSyADcGu8UFY4BrKaFiZzflb469-GF2o4ye8",
  "authDomain": "canbewell-test-75591.firebaseapp.com",
  "projectId": "canbewell-test-75591",
  "storageBucket": "canbewell-test-75591.appspot.com",
  "messagingSenderId": "665570512",
  "appId": "1:665570512:web:a34fd339eee40da49da2d5",
  "measurementId": "G-6E28QME46V",
  "databaseURL": "https://canbewell-test-75591-default-rtdb.firebaseio.com/" 
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

# https://uottawa-my.sharepoint.com/personal/pnikb070_uottawa_ca/Documents/CANBEWELL/App%20Usage%20Data%20and%20Analytics/Firebase%20Backup%20of%20App%20Usage%20Data/Data%20Backup/Data%2013-30%20April%20-2022/13th%20until%2030th%202022-prod.json

current_path = os.getcwd()
with open(current_path + '/test-input.json', 'r') as f:
  data = json.load(f)

for key, val in data.items():
  print(key)
  for k, v in val.items():
      database.child(key).child(k).set(v)
      # database.child(key).remove()

print("DONE!")
