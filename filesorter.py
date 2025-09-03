import os

def main():
    folder_name = input("Please enter the folder name: ")
    check(folder_name)

def check(folder_name):
    exception = os.path.isdir(folder_name)

    if exception == False:
        print("Please enter a valid directory")
    else:
        print("Valid Folder! Proceeding... ")
     
###print("Hello")
    

main()






