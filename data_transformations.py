my_file1 = open("data.txt", "r")
my_file2 = open("xdata.txt", "r")
my_file = open("tdata.txt", "w")

with open('data.txt', 'r') as f:
     data = f.readlines()
     print(data)
with open('xdata.txt', 'r') as g:
     xdata = g.readlines()
     print(xdata)

arr1 = []
arr2 = []

for line in data:
    arr1.append(line[:-1])

for line in xdata:
    arr2.append(line[:-1])


last = len(arr1);

for i in range(0,last):
    words1 = arr1[i].split()
    words2 = arr2[i]
    print(words2)
    my_file.write(words2+ " ")
    i = 1
    for j in words1:
        print(' '+j),
        my_file.write(str(i)+":"+str(j)+" ")
        i=i+1
    my_file.write("\n");
    print("\n")
my_file.close()
my_file1.close()
my_file2.close()

