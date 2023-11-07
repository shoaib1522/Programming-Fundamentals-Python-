rows=int(input('Rows: '))
col=int(input('Columns: '))
i=1
while i<=rows:
    j=1
    while j<=col:
        print(i,end=' ')
        j+=1
    print()
    a=1
    char=96
    while a<=(col):
        print(chr(char+i),end=' ')
        a+=1 
    print()
    i+=1