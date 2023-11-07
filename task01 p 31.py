file1 = open ('nums.txt','r')
n=int(file1.readline())

list1 = list(map(int, file1.readline().split()))
list2 = list(map(int, file1.readline().split()))


file = open("sum.txt", "w")
file.write(str(len(list1)))
file.write('\n')
sum_list=[0]*len(list1)
for i in range (len(list1)):
    sum_list[i] = list1[i] + list2[i] 
for i in range(len(sum_list)):
    file.write(str(sum_list[i]) + " ")


file.close()

