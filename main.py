import pyrebase

cred = {
    "your_key": "your_key"
  }

firebase = pyrebase.initialize_app(cred)
storage = firebase.storage()
path_local_image = "./teste.txt"
path_storage = "fiap/txts/config.txt"
storage.child(path_storage).put(path_local_image)
