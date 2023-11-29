#!/usr/bin/python3
import random

number = random.randint(-10,10)
if number < 0:
    result = "negative"
elif number == 0:
    result = "zero"
else:
    result = "positive"
print(f"{number} is {result}\n")
