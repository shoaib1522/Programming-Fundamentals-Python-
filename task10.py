rows=int(input('Rows: '))
col=int(input('Columns: '))
i=1
x=1
while i<=rows:
    j=1
    while j<=col:
        print(x,end=' ')
        j+=1
        x+=1
    print()
    a=1
    char=96+i
    while a<=(col):
        print(chr(char),end=' ')
        char+=1
        a+=1 
    print()
    i+=1
    x=0+i
    