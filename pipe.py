import pyrebase

# Configuration key for realtime database with all permission (read + write) to true
config = {
    "apiKey": "AIzaSyDUNr8QUe_7DJq_kkQojAO1cMz_BQHP6dM",
    "authDomain": "integra-e5643.firebaseapp.com",
    "databaseURL": "https://integra-e5643.firebaseio.com",
    "storageBucket": "integra-e5643.appspot.com",
}

# Initialize the "pyrebase" and retrieve the realtime database
firebase = pyrebase.initialize_app(config)
firebase_db = firebase.database()

# This will be set to some random user account
username = "ricozhuthegreat"

response = "Hello World!"

def stream_handler(message):

    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    firebase_db.child("users").child(username).child("read").push(
        {
            "message": response
        }
    )  

# Get the datastream from the realtime database
data_stream = firebase_db.child("users").child(username).child("post").stream(stream_handler)