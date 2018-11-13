""" This script helps to identify how itertools are working"""

import itertools


counter = itertools.count(start=5)


print(next(counter))
print(next(counter))

data = [100,200,300,400]



data_count = list(zip(itertools.count(), data))
data_count1 = list(zip(range(1, 10), data)) # prints only the data items count
data_count2 = list(itertools.zip_longest(range(1, 10), data)) # prints all items till range comes
print(data_count)
print(data_count1)
print(data_count2)


counter1 = itertools.cycle([1,8,9])

print(next(counter1))
print(next(counter1))
print(next(counter1))
print(next(counter1))


counter3 = itertools.repeat(3)

thanus = lambda x,y : x * y
squers = map(thanus, ["thanu","vino"], counter3)

print(list(squers))
