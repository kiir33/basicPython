try:
    file=open("testfile.txt","a")
    try:
        file.write("\nWritten by program.")
    finally:
        print("Inner Try")
        file.close()
except IOError as e:
    print(str(e))
