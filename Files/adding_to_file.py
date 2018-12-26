result = []
appendlist = ['\tage', 15, 12, 29, 20, 40, 33, 22]
f1 = open('file1', 'r')
i=0
for line in f1.readlines():
    a= line.split(",")
    result.append(a)
    result[i][1] = result[i][1].replace("\n","")
    result[i][1] = result[i][1] .lstrip()
    result[i].append(appendlist[i])
    i+=1
print(result)
f1.close()
f2 = open('file4','a')
i=0
for x in result:
    for j in range(3):
        f2.write(str(result[i][j]))
        if j != 2:
            f2.write(",\t")
        else:
            f2.write("\n")
    i+=1