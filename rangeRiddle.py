#Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for num in range(len(week)):
    if (num % 2 == 0):
        print(week[num])
