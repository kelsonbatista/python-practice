names1 = ["Albert", "John", "Mark", "Andrew"]
names2 = ["Peter", "Josh", "Carl", ""]
numbers1 = [1, 2, 3, 4]
numbers2 = [0, 5, 6, 7]

n1 = all(names1)
n2 = all(names2)
num1 = all(numbers1)
num2 = all(numbers2)
print(n1, n2, num1, num2)

# enumerate provides index with element
# enumerate objects is iterable
enumerate(names1)

for n in enumerate(names1):
    print(n)

for index, n in enumerate(names1):
    print(index, n)
