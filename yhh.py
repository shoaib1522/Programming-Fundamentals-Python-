from random import randint
def initialize(x, SIZE):
    for i in range(SIZE):
        x[i] = randint(0, 100) 

def print_array(x, SIZE):
    for i in range(SIZE):
        print(x[i], end=' ')
    print()
    
def main():
    SIZE = randint(5, 15)
    x = [0] * SIZE
    y = [0] * SIZE
    initialize(x, SIZE)
    initialize(y, SIZE)
    print(end="List 1: ")
    print_array(x, SIZE)
    print(end="List 2: ")
    print_array(y, SIZE)
    print('smaller')
    for i in range(SIZE):
        if x[i]<y[i]:
            print(x[i],end=' ')
        else:
            print(y[i],end=' ')
    print()
    print('Larger')
    for j in range(SIZE):
        if x[j]>y[j]:
            print(x[j],end=' ')
        else:
            print(y[j],end=' ')

main()