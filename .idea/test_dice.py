import random
import pytest


loosecount=0
wincount=0
for i in range(1,11):
    x=random.randint(1,6)
    if x%2==0:
        wincount=wincount+1
        print(x,"You Won")
    else:
        loosecount=loosecount+1
        print(x,"You Loose")

print("You Lost:",loosecount,"You Won:",wincount)
