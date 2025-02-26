import os
import shutil
def file_organize(directory):

    file_types = {
        'Archives': ['.zip', '.rar', '.tar'],
        'Spreadsheets': ['.csv', '.xlsx', '.xls'],
        'Documents': ['.pdf', '.txt', '.docx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Audios': ['.mp3', '.wav', '.flac'],
        'Videos': ['.mp4', '.avi', '.mov'],
        
    }

    for folder in file_types:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path): 
            file_ext = os.path.splitext(filename)[1].lower() 
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(directory, folder)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f" Sucessfully moved {filename} to {folder} folder.")
                    break  

def main():
    directory = input("Enter the directory you want to organize: ")

    if not os.path.exists(directory):
        print("The specified directory doesn't exist.")
        return
    file_organize(directory)
    print("File organization completed!")

if __name__ == "__main__":
    main()
