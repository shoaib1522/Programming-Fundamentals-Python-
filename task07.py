rows=int(input('Rows: '))
i=1
while i<=rows:
    j=1
    while j<=(rows-i):
        print(' ',end='')
        j+=1
    print(i)
    i+=1 