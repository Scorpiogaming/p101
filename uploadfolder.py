import os

import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                localpath=os.path.join(root,filename)
                relativepath=os.path.relpath(localpath,file_from)
                dropboxpath=os.path.join(file_to,relativepath)              
        with open(localpath, 'rb') as f:
            dbx.files_upload(f.read(), dropboxpath,mode=WriteMode("overwrite"))

def main():
    access_token ="sl.Ay0970tJaqVKMt-ewGqkhUzKVxjU1aUR7buY_O-4iwymtwB-HU9LIuvIq24rw23nir3pQtCJctZNKHpNOutrbNEgxH_zDc0QhzWXxHowiGx9Oz8ng2m_vZGWQrM6a5cR3lVd_Zw"
    transferData = TransferData(access_token)

    file_from = input("enter the folder path to transfer")
    file_to = input("enter the full path to transfer")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

if __name__ == '__main__':
    main()