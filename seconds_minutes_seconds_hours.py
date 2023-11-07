number_of_seconds=int(input('What are the total number of seconds:'))
hours = number_of_seconds //3600
seconds = number_of_seconds%3600
minutes = seconds //60
remainder_seconds = number_of_seconds%60
print(hours)
print(minutes)
print(remainder_seconds)
