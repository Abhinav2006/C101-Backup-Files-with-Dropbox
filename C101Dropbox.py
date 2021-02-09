import dropbox

class TransferData :
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def upload_file(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)

def main():
    accessToken = 'sl.Aq7Z69TFFLr-CmUQvY82HGNo7Ab3g2iylQlXGJxB8Rw5MbxUjSMXAq5h4SnQgcdQGSCUFXzZcjuktUFOtnoorE4tYrAgcHig__NGaC6gx054yVwWS2S9kSph-Opsvm3zriPBDT4'
    transferData = TransferData(accessToken)
    filefrom = input("Enter File Name to upload")
    fileto = input("Enter the full path to upload to Dropbox")
    transferData.upload_file(filefrom, fileto)
    print("File has been moved successfully")

main()