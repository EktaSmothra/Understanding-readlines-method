import os         # used for measuring size of file and has lot of other options.
get_file= input("Enter name of the file that you want to print: ")
try:
    with open(get_file,'r',encoding="utf-8") as f:
        print("Name of the file is: ",f.name)       #f.name is used for printing name.
        a = f.readlines()                   #f.readlines will read the contents of whole file                          
        if os.stat(get_file).st_size > 0:   #os.stat .st_size is used for checking the size of file.
            print("Checking into the contents of the file: \n", a)
except:
        print("File contains no content. We are really sorry. Nothing can be displayed.")



