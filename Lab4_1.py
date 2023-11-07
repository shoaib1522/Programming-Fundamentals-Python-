basic_salary = int (input ('Basic Salary = '))
medical_allowance = basic_salary * 0.1
conveyance_allowance = basic_salary * 0.15
house_rent = basic_salary * 0.45
gross_salary = basic_salary + medical_allowance + conveyance_allowance +house_rent
annual_gross_salary  = gross_salary * 12
if annual_gross_salary < 200000:    tax = 0;
elif annual_gross_salary < 400000:  tax = gross_salary * 0.1;
elif annual_gross_salary < 600000:  tax = gross_salary * 0.15;
elif annual_gross_salary < 800000:  tax = gross_salary * 0.2;
else:                               tax = gross_salary * 0.25;
net_salary =  gross_salary - tax
print ('Basic Salary\t\t\t', basic_salary)
print ('Medical Allowance\t\t', int(medical_allowance))
print ('Conveyance Allowance\t', int(conveyance_allowance))
print ('House Rent\t\t\t', int(house_rent))
print ('-----------------------------')
print ('Gross Salary\t\t\t', int(gross_salary))
print ('-----------------------------')
print ('Less Tax\t\t\t\t', int(tax))
print ('-----------------------------')
print ('Net Salary\t\t\t',int(net_salary))
print ('-----------------------------')