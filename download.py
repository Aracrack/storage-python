import pyrebase

cred = {
    "apiKey": "AIzaSyAojQkQOSahcwovsDn8GXwGBuekoEIe-3U",
    "authDomain": "fir-python-3e64f.firebaseapp.com",
    "databaseURL": "https://fir-python-3e64f.firebaseio.com",
    "projectId": "fir-python-3e64f",
    "storageBucket": "fir-python-3e64f.appspot.com",
    "messagingSenderId": "603326099037",
    "appId": "1:603326099037:web:5eee5fdf747547f5d367b4",
    "measurementId": "G-ZGTGJPN6CY"
  }

firebase = pyrebase.initialize_app(cred)
storage = firebase.storage()
download_path = 'fiap/txts/config.txt'
outfile = 'txt_downloaded.txt'
storage.child(download_path).download(outfile)