from svmutil import *

my_file1 = open("tdata.txt", "w")
my_file4 = open("tdata_test.txt", "w")
with open('data.txt', 'r') as f:
     data = f.readlines()
     #print(data)
     #print(" length data ")
     numberOfData = len(data)

#Scale of Training Data
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
    for j in range(0,8):
        data1 = float(words1[j])
        data1 = lower + (upper-lower)/(maxi-mini)*(data1-mini)   
        words1[j] = str(data1)
    arr2.append(words1)
    
#print("scaled \n")
#print(arr1)
#print(arr2)
#print(arr2[3])

#print("printing")


with open('x500.txt', 'r') as g:
     xdata = g.readlines()
     #print(xdata)

for line in xdata:
    arr3.append(line[:-1])
    
#print(arr3)

for i in range(0,last):
    words2 = arr3[i]
#  print("this is starting the writing task")
#  print(words2)
    my_file1.write(words2+ " ")
    k = 1
    for j in arr2[i]:
#        print(' '+str(k)+':'+j),
        my_file1.write(str(k)+":"+str(j)+" ")
        k=k+1
    my_file1.write("\n"); 
 #   print("\n")
my_file1.close()



#Scaling of data to be predicted
with open('randomdata500.txt', 'r') as f:
     data = f.readlines()
     #print(data)
     #print(" length data ")
     numberOfTestData = len(data)

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
    for j in range(0,8):
        data1 = float(words1[j])
        if data1<mini:
            mini = data1
        if data1>maxi:
            maxi = data1

upper = 1
lower = 0

for i in range(0,last):
    words1 = arr1[i].split()
    for j in range(0,8):
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
    k = 1
    for j in arr2[i]:
        #print(' '+j),
        my_file4.write(str(k)+":"+str(j)+" ")
        k=k+1
    my_file4.write("\n");
    #print("\n")
my_file4.close()

y, x = svm_read_problem('tdata.txt')
		    
C = max(y) - min(y);	
T = 2; 					# RBF kernel
gamma =[0.0078125, 0.015625, 0.03125, 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 128];  # range of the gamma parameter
epsilon = [0, 1, 2, 3, 4, 5];				# range of the epsilon parameter
best_mse = 100000000

for j in range(0,15):
    G = gamma[j]
    for k in range(0,6):
        E = epsilon[k]
        mse = svm_train(y[:numberOfData], x[:numberOfData], '-q -v 5 -s 3 -t 2 -b 1 -c ' + str(C) + ' -g ' + str(G) + ' -p ' + str(E))  # build model on Learning data
        #print ("mse")
        #print (mse)
        if mse <= best_mse:
            best_mse = mse
            bestG = G
            bestE = E
print("best parameters mse G E")
print(best_mse, bestG, bestE)

model = svm_train(y[:numberOfData], x[:numberOfData], '-q -s 3 -t 2 -c ' + str(C) + ' -g ' + str(bestG) + ' -p ' + str(bestE))

y, x = svm_read_problem('tdata_test.txt')
#print("input")
#print(y)
#print(x)
p_label, p_acc, p_val = svm_predict(y[0:], x[0:], model)

#print("p_label")
#print(p_label)
#print(p_acc)
#print(p_val)

my_file2 = open("resultsx.txt", "w")
for i in range(0,numberOfTestData):
    my_file2.write(str(p_label[i])+"\n")

my_file2.close()
