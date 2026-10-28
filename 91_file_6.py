import os 
old_file_name = input("Enter file name to rename")
new_file_name = input("Enter new file name")
os.rename(old_file_name,new_file_name)
print("File renamed successfully")