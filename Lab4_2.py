amount = int (input ('Amount Deposited = '))
if amount < 500000: tax_rate = 1.07;
else:               tax_rate = 1.1;
print ('Amount after one year = ', int(amount * tax_rate))
print ('Amount after second year = ', int(amount * tax_rate * tax_rate))
print ('Amount after third year = ', int(amount * tax_rate * tax_rate * tax_rate))