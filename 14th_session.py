#########  practice session - assignment_3


#21. Write a Python to compare 2 directories ( Eg: C:\python36 and c:\python27 ) and display the below information

from filecmp import dircmp

# Construct a new directory comparision object
# to compare the directories left and right

dcmp = dircmp(r"C:\Python35",r"C:\Python35")

# This directory from left side of dircmp method
print("\nleft:",dcmp.left)



#Files and subdirectories in a directory from left side of dircmp method
print("\nleft list:", dcmp.left_list)

#The directory from right side of dircmp method
print("\nright:",dcmp.right)

 
#Files and subdirectories in a directory from right side of dircmp method
print("\right list:", dcmp.right_list)

#Files and subdirectories in both left and right
print("\nCommon:",dcmp.common)

#Files in both left and right
print("\nCommon files:", dcmp.common_files)

#files which are identical in both left and right, using the class's
# file comparision operator
print("\nsame_files", dcmp.same_files)



#22. Write a Python program to generate 4 digit random number.

import random
print(random.randrange(1000,9999))


##### 23,24,25 still working on it


#26. Write a Python program to delete all the files from the current directory that are older than 10 days.

def cleanup(number_of_days, path):
print("Inside cleanup")
time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    if os.path.isdir(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            shutil.rmtree(path)
    elif os.path.isfile(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            remove(path)
directory = os.getcwd()
path_with_days = { directory :10 }
for path,days in path_with_days.items():
    cleanup(days, path)


#27. Write a Python program to delete all the files from the current directory that are not modified in last 10 days.

def cleanup(number_of_days, path):
    print("Inside cleanup")
    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    if os.path.isdir(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            shutil.rmtree(path)
    elif os.path.isfile(path):
        stat = os.stat(path)
        if stat.st_mtime <= time_in_secs:
            remove(path)
directory = os.getcwd()
path_with_days = { directory :10 }
for path,days in path_with_days.items():
    cleanup(days, path)
    

## no 28    
#29. Write a Python program to validate the email-address

import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = "giridhar276@gmail.com"
if re.search(regex,email):
    print("valid email")
else:
    print("Invalid email")

## 2nd example
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = "giridhar276@gmail.com"
if re.search(regex,email):
    print("valid email")
else:
    print("Invalid email")
    
    
#30. Write a Python program to validate the IP Address

# without regex
ip = input("Enter any ip address:")
out = ip.split(".")
ip = input("Enter any ip address:")
out = ip.split(".")
if len(out) != 4 :
    print("Invalid ip")   
if int(out[0])  in range(1,256) and int(out[1])   in range(0,256) and  int(out[2])   in range(0,256) and  int(out[3])   in range(0,256):
    print("Valid ip")
else:
    print("Invalid ip") 
    
    

### no 31,32
