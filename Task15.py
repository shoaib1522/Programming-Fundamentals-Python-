import random
array=[[random.randint(0,9) for j in range(10)]for i in range(10)]
for printing_array in range(len(array)):
    for printing_array2D in range(len(array)):
        print(array[printing_array][printing_array2D],end=' ')
    print()
for printing_diagonals in range(len(array)):
    for printing_diagonals2D in range(len(array)):
        if array[printing_diagonals][printing_diagonals2D]==0:
            print(printing_diagonals,' ',printing_diagonals2D)
