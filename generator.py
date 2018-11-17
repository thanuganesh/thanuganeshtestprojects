
"""This function helps to find genertor """



def squre_nums(numbers):
    results = []
    for i in numbers:
        results.append(i*i)
    return results


my_nums = squre_nums([1,3,3,4])

print(my_nums)


########How to change that func as generator is simple to remove list and return and put yield

###yield denotes that func as generator


def s_n(n):
    for i in n:
        yield i*i



p = s_n([1,2,3,4])

# it return generator object hold entire result in memory it holds only one result in memory it ask for next method give next result

print(next(p))
print(next(p))
print(next(p))
print(next(p))
#print(next(p))


#generator is best for memory


my_nums = [ i*i for i in range(1, 6)]

print(my_nums)


my_nums = (i*i for i in range(1, 6))

print(my_nums)




