import os
import pathlib
from pathlib import Path

#Main function
def main():

    folder_name = input("Please enter the full path of the folder you want to be sorted: ").strip()
    check(folder_name)

    #finds path of said folder name
    p = Path(folder_name).expanduser().resolve()
    sort(p)

#Check to see if folder is valid
def check(folder_name):
    exception = os.path.isdir(folder_name)

    if exception == False:
        print("Please enter a valid directory")
        return False
    else:
        print("Valid Folder! Proceeding... ")
        return True

#sorts files by files type and puts them in a folder of said file type.
def sort(p):
    for f in p.iterdir():
        #checks if the file is a file if yes continue
        if not f.is_file():
            continue

        match f.suffix.lower:
            case ".mp3":
                t_dir = p / "Music"
            case ".mp4":
                t_dir = p / "Videos"
            case ".txt":
                t_dir = p / "Documents"
            case ".docx":
                t_dir = p / "Documents"
            case ".doc":
                t_dir = p / "Documents"
            case ".pdf":
                t_dir = p / "Documents"

        t_dir.mkdir(exist_ok=True)
        
main()






