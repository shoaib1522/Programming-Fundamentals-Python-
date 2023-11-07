card_type=input('input the type of card: ')
card_type=card_type.capitalize()
if card_type=='D':
    print('your type is diamond with red color')
elif card_type=='H':
    print('your type is heart with red color')
elif card_type=='S':
    print('Your card type is spade with black color')
elif card_type=='C':
    print('your card type is club with black color')
else:
    print('The card type you entered doesn\'t exist')