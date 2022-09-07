# max min len
import random

# interval range, quantity of numbers
list = random.sample(range(0, 10000), 1000)
print(list)

# return list quantity
print(len(list))

# return max and min number
print(max(list))
print(min(list))

# random quantity
# generate between 50 and 5000 elements into my list
list2 = random.sample(range(0, 10000), random.randint(50, 5000))
print(len(list2))
print(max(list2))
print(min(list2))
