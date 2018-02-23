m = svm_train(y[:numberOfData], x[:numberOfData], '-c 0.5 -g 0.125 -p 0.001 -s 3 -t 2 -b 1')



with open('randomdata500.txt', 'r') as f:
     data = f.readlines()
     #print(data)
     #print(" length data ")
     numberOfData = len(data)

#Scale The Data
arr1 = []
arr2 = []
arr3 = []
for line in data:
    arr1.append(line[:-1])
    

mini = 1000000
maxi = 0
last = len(arr1);

for i in range(0,last):
    words1 = arr1[i].split()
    for j in range(0,7):
        data1 = float(words1[j])
        if data1<mini:
            mini = data1
        if data1>maxi:
            maxi = data1

upper = 1
lower = 0

for i in range(0,last):
    words1 = arr1[i].split()
    for j in range(0,7):
        data1 = float(words1[j])
        data1 = lower + (upper-lower)/(maxi-mini)*(data1-mini)   
        words1[j] = str(data1)
    arr2.append(words1)
    
#print("scaled \n")
#print(arr1)
#print(arr2)
#print(arr2[3])

with open('randomx500.txt', 'r') as g:
     xdata = g.readlines()
     #print(xdata)

for line in xdata:
    arr3.append(line[:-1])
    
#print(arr3)

for i in range(0,last):
    words2 = arr3[i]
    #print("this is starting the writing task")
    #print(words2)
    my_file4.write(words2+ " ")
    i = 1
    for j in arr2[i]:
        #print(' '+j),
        my_file4.write(str(i)+":"+str(j)+" ")
        i=i+1
    my_file4.write("\n");
    #print("\n")
my_file4.close()



y, x = svm_read_problem('tdata_test.txt')
p_label, p_acc, p_val = svm_predict(y[0:], x[0:], m)
#print(x[:1])
#print(p_label)
#print(p_acc)
#print(p_val)


my_file3 = open("new.txt", "w")
k = str(p_label[0])


for i in p_label:
    my_file3.write(str(i)+"\n")
    #print(i)
    
my_file3.close()
