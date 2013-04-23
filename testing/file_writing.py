# If the file "testfile.txt" doesn't exist, this will create it and write the contents of the .write statement
# If the file "testfile.txt" does exist, this will add directly on to the end.

newfile = open("testfile.txt","a")
newfile.write("To come to the aid of their party")