# Import package
import os

# Check for file existence and removal
if os.path.exists("yourfile.txt"):
  print("The file exist!")
  print("Do you want to delete the file?")
  print()
  file_status = input("Enter 'Y for yes. Else enter 'n' for no. ")
  if file_status.upper() == 'Y':
    os.remove("yourfile.txt")
  else:
     exit()
else:
    print("The file does not exist")
    print()