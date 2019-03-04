# Understanding-readlines-method
__readlines()__ reads whole file into memory, and builds a list full of strings out of those lines. In short, we can say that this function returns a list of lines of the file. It is an easy way of reading and parsing file in python. The simplest way of using this function is as follows:

    # Open the file in read mode
    f = open('demo.txt', "r", encoding="utf-8") as f:   # use readlines()  function to read all lines in the file and store it in a variable
        lines = f.readlines()
    print(lines)          #This will print all the lines in a list from the file
    # close the file after reading the lines.
    f.close() 

This function is not memory efficient when large text file comes into picture. It consumes more memory as it will read whole file into the memory, so, it is best suited for reading small sized files. The best suited way to read a text file in python is by reading it line by line. This can be achieved by using for loop, while loop etc.

## Reading text file line by line using while loop in python

I am presenting a simple way of reading a file using while loop in python. I would go for more complex programs for more better understanding later. Here is the cod eto start with:

    
    f = open('demo.txt')          # Open the file with read only permit 
    line = f.readline()                   # use readline() to read the for reading the file 
    while line:
        print(line)                       # use realine() to read next line
        line = f.readline()
    f.close()
    
## Reading text file line by line using for loop in python

Here is a beginner code for getting started with readlines function and reading file line by line using for loop.

    x = open('demo.txt','r', encoding='utf-8')
    for line in x:
          print(line)
    x.close()

## Note: We don't need to close file when using "with" for opening files. "with" creates a context manager and automatically closes the file when you are done with it. When simply using open, we should close the file at the end. We should also check whether the handler is closed or not by using "file_object.closed" command.

I will add more better real use case programs for this function soon. So do keep checking the upgradations in this repository.

## References  
https://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/  

