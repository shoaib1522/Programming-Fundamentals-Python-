rows=int(input('Rows: '))
i=1
while i<=rows:
    j=1
    while j<=(i-1):
        print(' ',end='')
        j+=1
    print(i)
    i+=1 