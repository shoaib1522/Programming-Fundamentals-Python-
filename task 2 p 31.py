file1 = open ('nums.txt','r')
n=int(file1.readline())

list1 = list(map(int, file1.readline().split()))
list2 = list(map(int, file1.readline().split()))


file = open("compare.txt", "w")
file.write(str(len(list1)))
file.write('\n')
n_list=[0]*len(list1)
for i in range (len(list1)):
    if list1[i]==list2[i]:
        n_list[i] = 1
    else:
        n_list[i]=0
for i in range(len(n_list)):
    file.write(str(n_list[i]) + " ")


file.close()
