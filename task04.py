char = ord(input('Input the character'))
bit =int(input('enter the bit position you want to check is on'))
position=2**(bit-1)
if (char&position==position):
    print(f'The bit number {(bit)} is on in {chr(char)}')
else:
    print(f'The bit number {(bit)} is off in {chr(char)}')
