import calendar

date = input("Enter a date: ")
year = int(date [6:])
month  = int(date [3:5])
day = int(date [0:2])
dayOfWeek = calendar.weekday(year, month, day)
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print (day_names[dayOfWeek])