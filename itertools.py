""" This script helps to identify how itertools are working"""

import itertools


counter = itertools.count(start=5)


print(next(counter))
print(next(counter))

data = [100,200,300,400]



data_count = list(zip(itertools.count(), data))
data_count1 = list(zip(range(1, 10), data)) # prints only the data items count
data_count2 = list(itertools.zip_longest(range(1, 10),[1,2,3,4], data)) # prints all items till range comes
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


##############################################starmap#############################################


squers_one = itertools.starmap(thanus, [(0,1),(1,2),(3,6)])

print(list(squers))
print(list(squers_one))


################################Combinations&permutations##########################################



letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ["thanu", "ganesh"]

#results = itertools.combinations(letters, 2) #combinations only given a single pair (a,b) not (b,a_ b ecaz it is considered both as same

#for item in results:
    #print(item)


#if i need to print all the values then use permutations


results = itertools.permutations(letters, 2)
for item in results:
    print(item)



##########################################chain##############################


#combine all the squences and we need to iterate then chain
cobined = itertools.chain(letters, numbers, names)

for i in cobined:
    print(i)

##################islice#####################################


resp = itertools.islice(range(10), 2, 4, 2)

for ite in resp:
    print (ite)


with open("isslice_example.txt") as f:
    header = itertools.islice(f,3)
    for item in header:
        print(item)



#####################compress######################


selectors =[True, True, False, True]


first_result = itertools.compress(numbers, selectors)

for itr in first_result:
    print(itr)




######################filter Function#####################################





