#!/usr/bin/python3
import random

number = random.randint(-10,10)
if number < 0:
    result = "-98 is negative"
elif number == 0:
    result = "0 is zero"
else:
    result = "98 is positive"
print(f"{result}")
