import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth


# Fetch the service account key JSON file contents
cred = credentials.Certificate('grumble-49981-firebase-adminsdk-1qx5e-b186c2daff.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://grumble-49981-default-rtdb.europe-west1.firebasedatabase.app"
})

#auth.create_user(email="chrisgillespie2001@googlemail.com",password="testererowh")
#etest = auth.get_user_by_email(email="chrisgillespie2002@googlemail.com")
ref = db.reference('Database reference')
print(ref.get())



