# counter
import random
from collections import Counter

numbers_list = []

for x in range(10000):
    numbers_list.append(random.randint(0, 1000))

# print(numbers_list)
# print(len(numbers_list))

# using counter
# shows a dictionary and the first element is the number list
# the second is number quantity that repeats
counter = Counter(numbers_list)
print(counter, '<<<<<<< counter')
print(counter[0], '<<<<<<< quantity of zeros')

# get the most frequent number
# shows a list of tuples , most frequent numbers ordered
mc = counter.most_common()
print(mc, '<<<<<<< most commons')

# destructure
element, quantity = mc[0]
print(element, quantity, '<<<<<< element')
