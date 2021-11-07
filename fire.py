import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

 # fetching service account key
cred = credentials.Certificate("serviceAccount.json")

    # Initialize the app with service account 
firebase_admin.initialize_app(cred,{
        'databaseURL':'https://dementors-c0305-default-rtdb.firebaseio.com/'})

    