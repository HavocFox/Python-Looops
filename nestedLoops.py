#Task 1: Meal Planner Simulate a meal planner that picks a random meal from a meal list for breakfast lunch and dinner for each day of the week.
#Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the meals of the day.
#For each time, randomly select a meal from a predefined list and print it. 

import random

meals = ['Breakfast', 'Lunch', 'Dinner']
food = ['Burger', 'Fish', 'Sausage', 'Egg', 'Sandwich', 'Escargot', 'Camembert', 'Tripe', 'Humuhumunukunukuapuaa', 'Brownies']
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for day in range(len(week)):
    for time in range(len(meals)):
        print(week[day], "for", meals[time], "I'm having", random.choice(food))
