try:
    file=open("testfile.txt","w")
    file.write("Written by program.")
except IOError:
    print("IO error found!")
else:
    print("successfully written")
    file.close()