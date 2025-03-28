import calendar

print("Enter Year and Month below to view the respective calendar")
year = int(input('Enter year: '))
month = int(input('Enter month: '))

cal = calendar.TextCalendar(calendar.SUNDAY)

cal.prmonth(year, month)