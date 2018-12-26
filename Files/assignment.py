result = []
f1 = open('file1', 'r')
f2 = open('file2', 'a')
f3 = open('file3', 'a')
for line in f1.readlines():
    a= line.split(",")
    result.append(a)
    f2.write(a[0])
    f2.write("\n")
    a[1]=a[1].lstrip()
    f3.write(a[1])
f1.close()
f2.close()
f3.close()