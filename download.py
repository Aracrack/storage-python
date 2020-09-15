import pyrebase

cred = {
    "your_key": "your_key"
  }

firebase = pyrebase.initialize_app(cred)
storage = firebase.storage()
download_path = 'fiap/txts/config.txt'
outfile = 'txt_downloaded.txt'
storage.child(download_path).download(outfile)
