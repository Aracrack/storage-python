import pyrebase

cred = {
    "apiKey": "AIzaSyAojQkQOSahcwovsDn8GXwGBuekoEIe-3U",
    "authDomain": "fir-python-3e64f.firebaseapp.com",
    "databaseURL": "https://fir-python-3e64f.firebaseio.com",
    "projectId": "fir-python-3e64f",
    "storageBucket": "fir-python-3e64f.appspot.com",
    "messagingSenderId": "603326099037",
    "appId": "1:603326099037:web:bd5cb79da47c4db8d367b4",
    "measurementId": "G-WSCKFKH4BL"
  }

firebase = pyrebase.initialize_app(cred)
storage = firebase.storage()
path_local_image = "./teste.txt"
path_storage = "fiap/txts/config.txt"
storage.child(path_storage).put(path_local_image)