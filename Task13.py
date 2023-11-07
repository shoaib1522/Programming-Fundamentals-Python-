import random
array=[random.randint(3,7) for i in range(10)]
print(array)
for i in range(8):
    print(array[i],array[i+1],array[i+2])