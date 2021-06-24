class TransferData

uploadFile(){
    for root, dirs, files in os.walk(file_from)
    relative_path = os.path.relpath(local_path, file_from)
    dropbox_path = os.path.join(file_to, relative_path)

    with open(local_path,'rb') as f:
        dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))
}