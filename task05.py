a = float(input('enter the number which you want to check divisible or not'))
if a%2==0 and a%3==0:
    print('number is divisible by 2 and 3')
elif a%2==0 and a%5==0:
    print('number is divisible by 2 and 5')
elif a%2==0 and a%7==0:
    print('number is divisible by 2 and 7')
elif a%3==0 and a%5==0:
    print('number is divisible by 5 and 3')
elif a%3==0 and a%7==0:
    print('number is divisible by 7 and 3')
elif a%7==0 and a%5==0:
    print('number is divisible by 7 and 5')
elif a%2==0:
    print('number is divisible by 2 ')
elif a%3==0:
    print('number is divisible by 3')
elif a%5==0:
    print('number is divisible by 5')
elif a%7==0:
    print('number is divisible by 7')
else:
    print('Your number is not divisible by any 2,3,5,7')
