import random
a=[[random.randint(25,100) for i in range(3)]for j in range(4)]
for k in range(len(a)):
    for l in range(3):
        print(a[k][l],end=' ')
print()
for diagonals in range(3):
    for diagonals_a in range(len(a)):
            print(a[diagonals_a][diagonals],end=' ')
    print()
# i=len(a)-1
# while i>=0:
#     for k in range(len(a)):
#         if i==k:
#             print(a[i][k],end=' ')
#     i-=1
