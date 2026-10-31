from s3_operations import  list_files, upload, delete, download

def main():
    while True:
        print("========== CLOUDVAULT ==========")
        print("1.List\n2.Upload\n3.Download\n4.Delete\n5.Exit")
        check_input = int(input("Enter your choice (1-5): ").lower().strip())

        if check_input == 1:
            list_files()

        elif check_input == 2:
            file = input("Give file on your computer (name, ex: upload_test.txt): ")
            ob_name = input("Give name of the object in S3: ")
            upload(file,ob_name)

        elif check_input == 3:
            ob_name = input("File's name (s3 Key) in the bucket: ")
            file = input("Where to save the downloaded file on your computer ( with path add the file name which is to be saved) : ")
            download(ob_name,file)

        elif check_input == 4 :
            ob_name = input("Enter S3 object name to delete: ")
            delete(ob_name)
        elif check_input == 5:
            break
        else:
            print("Give proper input")
        print("\n" * 2)
if __name__ == "__main__":
    main()

