import os
import glob
count=0
location = input("Please Enter Location: ")
file_type=input("Please Enter Type of file")
try:
    if(os.path.exists(location)):
        for loc,var,file in os.walk(location):
            right_type = "*" + file_type
            count = count + len(glob.glob1(loc,right_type))
        print("Number of items " ,count)
    else:
        print("The given path doesn't Exist")
except OSError as e:
    print(e)
    

    
