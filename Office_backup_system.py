import os
import shutil
from pathlib import Path


print("This is an Office Mangment system")

def get_source_information(source):
    print("Folder name   :",os.path.basename(source))
    print("Parent folder :", Path(source).parent)
    print("Absolute Path :",os.path.abspath(source))

    total_file = 0
    total_folder = 0
    
    for current , folders , files in os.walk(source):

        for folder in folders:
            total_folder += 1

        for file in files:
            total_file += 1

    print(f"Total Folders : {total_folder}")
    print(f"Total Files   : {total_file}")
   
    return total_file , total_folder
    

def copy_folder(source , destination):
    try:
        copy_path = shutil.copytree(source , destination)
        print("file copied succesfully")
        print("File copied :",copy_path)
        return "Yes"
    except FileExistsError:
        print("The distination already exists")
        choose = input("Do you want to copy file into existing folder (yes / no) :").lower().split()

        if choose == ["yes"]:
            try:
                copy = shutil.copytree(source ,destination , dirs_exist_ok=True)
                print("File copied succesfully")
                print("File copied :",copy)
                return "Yes"
            except Exception as e:
                print("Error :",e)

        elif choose == ["no"]:
            choice = input("Do you want to delete the existing file (yes / no) :").lower().split()

            if choice == ["yes"]:
                delete = shutil.rmtree(destination)
                print("File deleted succesfully")
                

                copy = shutil.copytree(source, destination)

                print("Folder copied successfully")
                print("Folder copied :", copy)
                return "Yes"
            
            elif choice == ["no"]:
                print("Operationh Canceled")
                return "No"

            else:
                print("Just enter (yes / no) ")
     
        else:
            print("jsut enter (yes / no)")
        

def create_archieve(source , destination):
    print("Creating archieve.......")
    d = Path(destination + ".zip")
    try:
        if d.exists():
            print("The arcieve file Alredy exist")
            choose = input("Do yo want to replace the archeive (yes /no) :").lower().split()
            
            if choose == ["yes"]:
                archieve = shutil.make_archive(destination , "zip" , source)
                print("Archieve replaced suuccesfully")
                print("Archieve :",archieve)
                return "Yes"

            elif choose == ["no"]:
                print("The file did not create")
                print("The old file is given")
                return "No"
            
            else:
                print("Enter just yes or no")

        else:
            try:
                archieve = shutil.make_archive(destination , "zip" , source)
                print("Archieve Created suuccesfullyy")
                print("Archieve :",archieve)
                return "Yes"
            except Exception as e:
                print(e)


    except Exception as e:
        print(e)


def delete_original(source):
    choose = input("Do you want to delete the original folder (yes / no) :").lower().split()
    if choose == ["yes"]:
        try:
            shutil.rmtree(source)
            print("Original file deleted succesfully")
            return "Yes"
        except Exception as e:
            print(e)

    elif choose == ["no"]:
        print("ok we do not delete the file.")
        return "No"
    
    else:
        print("Enter just yes / no")




def final_report(source,
                 destination,
                 total_files,
                 total_folders,
                 copy_status,
                 archive_status,
                 delete_status):

    print("\n" + "=" * 15, "BACKUP REPORT", "=" * 15)

    print(f"Source Folder          : {source}")
    print(f"Backup Location        : {destination}")
    print(f"Files Copied           : {total_files}")
    print(f"Folders Copied         : {total_folders}")
    print(f"Folder Copied          : {copy_status}")
    print(f"ZIP Created            : {archive_status}")
    print(f"Original Folder Deleted: {delete_status}")

    print("\nBackup Completed Successfully")
     

def main():

    source_path = input("Enter Source Folder : ")
    source = Path(source_path)
    if source.exists() and source.is_dir():
        destination_path = input("Enter Backup Folder : ")
        dest = Path(destination_path)

        if dest.parent.exists():
            total_files, total_folders = get_source_information(source_path)

            copy_status = copy_folder(source_path, destination_path)

            archive_status = create_archieve(source_path, destination_path)

            delete_status = delete_original(source_path)

        else:
            print("Destination path is incorrect")
            return

    else:
        print("Source path is incorrect")
        return

        

    final_report(
        source_path,
        destination_path,
        total_files,
        total_folders,
        copy_status,
        archive_status,
        delete_status
    )


main()

# source="E:\\OG"
# destination ="E:\\Backup"

# get_source_information(source)
# copy_folder(source , destination)
# create_archieve(source , destination)
# delete_original(source)

