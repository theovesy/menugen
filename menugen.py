#!/usr/bin/python3

import csv
import random
import sys

try:
    mealnumber = int(sys.argv[1])
except:
    mealnumber = 9

with open('meals.csv', 'r') as file:
    reader = csv.reader(file)

    meallist = []
    nb_meal = 0

    for row in reader:
        if len(row) == 2:
            name, count = row
            nb_meal += 1
            for i in range(int(count)):
                meallist.append(name)

chosenmeal = []

for i in range(mealnumber):
    while(True):
        index = random.randint(0, len(meallist)-1)
        meal = meallist[index]
        if meal not in chosenmeal:
            chosenmeal.append(meal)
            print(meal)
            break
        if len(chosenmeal) >= nb_meal:
            break



