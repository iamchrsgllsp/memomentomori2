import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
import requests
import json


# Fetch the service account key JSON file contents
cred = credentials.Certificate('grumble-49981-firebase-adminsdk-1qx5e-b186c2daff.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://grumble-49981-default-rtdb.europe-west1.firebasedatabase.app"
})

#auth.create_user(email="chrisgillespie2001@googlemail.com",password="testererowh")
#etest = auth.get_user_by_email(email="chrisgillespie2002@googlemail.com")
#ref = db.reference('Database reference')
#print(ref.get())

def check_user(email):
    try:
        user = auth.get_user_by_email(email)
        return False
    except:
        return True
    
def add_user(email,password,display):
    auth.create_user(email=email,password=password,display_name=display)
    return True

def sign_user_in(email, password):
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDSAH8IvxM5e9S0tYAiTpMHW1As6UE8bxQ'
    headers = {'Content-Type': 'application/json'}
    data = {"email": email, "password": password}
    resp = requests.post(url, json=data, headers=headers)
    data = json.loads(resp.text)
    if 'registered' in resp.text:
        return {"data":data['displayName']}
    else:
        return False


