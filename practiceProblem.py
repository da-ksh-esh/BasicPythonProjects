'''

year = int(input('Enter year: '))
if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
    print('Its a leap year')
else:
    print('Not a leap year')

'''
'''
mark1 = int(input('Enter your maths marks: '))
mark2 = int(input('Enter your physics marks: '))
mark3 = int(input('Enter your chemistry marks: '))

avg = (mark1 + mark2 + mark3)/3

if avg >= 90:
    print('Grade: A')
elif avg < 90 and avg >= 80:
    print('Grade: B')
elif avg < 80 and avg >= 75:
    print('Grade: C')
else:
    print('Work Hard!')

'''

#check if a number is divisible by 3 and 5
# perform actions based on choicesf