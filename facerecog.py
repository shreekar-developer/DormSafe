# -*- coding: utf-8 -*-
"""faceRecog

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jwhsEiBYVztvF1IARjsaV4a_W933CN2j
"""

!pip install pyrebase
import pyrebase
!pip install deepface
import deepface
from deepface import DeepFace
import pandas as pd

config = {
    "apiKey": "AIzaSyBLh9JPlfznWqYXRASgtzpCKzbajycJmr0",
    "authDomain": "pihacks-b60b7.firebaseapp.com",
    "databaseURL": "https://pihacks-b60b7-default-rtdb.firebaseio.com",
    "projectId": "pihacks-b60b7",
    "storageBucket": "pihacks-b60b7.appspot.com",
    "messagingSenderId": "858171101294",
    "appId": "1:858171101294:web:608a110d7673ca5332167f",
    "serviceAccount": "/content/pihacks-b60b7-firebase-adminsdk-gmn9q-b16e15c366 (1).json"
  }
 
 #
firebase = pyrebase.initialize_app(config)
database=firebase.database()
#

#
id=database.child("picid").get()
intId=id.val()
#

#
storage=firebase.storage()
storage.child(intId).download("downloaded.png")
#

allFiles = storage.list_files()
for file in allFiles:
  file.download_to_filename("/content/refphotos/" + file.name)

df = DeepFace.find(img_path = "downloaded.png", db_path = "/content/refphotos")
df.head()

print((df.identity[0])[19:])