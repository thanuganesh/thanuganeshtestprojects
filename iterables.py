"""This function helps to learn about iterables"""


#List is iterable but not iterator
#iterable somthing can be looped over becaz we can loop over list


#how we can say some thing is iterable????

#__iter__() method in iterable then its called iterable


#iterator is object with the state it rembers where its during iteration  and iterable called iter as object and it is return iterator


#something is iterable then it contains __iter__ method with in it.
#iteratot know how to get next value __next__() method


#Bascially for llop in the backgroung it is calling iter object and return iterator so it is called iterable

nums = [1, 2, 3, 4]

print(dir(nums))

for num in nums:
    print(num)

i_nums = nums.__iter__() #this is something for loop getin the background
i_nums = iter(i_nums)

print(i_nums) #print itself 
print(dir(i_nums)) # Shows what are attributes and methods available


print(next(i_nums))
print(next(i_nums))# if this next print next value becaz itetor knows where it is left off


#what for loops to avoid stopIteration error


while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

#iteratoy go forward using __next__ no backward


#own class to behave like iterable####################################



class Myrange:
    
    def __init__(self, start, end):
        self.value = start
        self.end = end


    def __iter__(self): # rember if we need iteratable the we need iter method avilable

        return self #need to return next if return self here


    def __next__(self): #rember iter hace state it knows wer it is left off
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current


nums_1 = Myrange(1, 10)

print(next(nums_1))



def my_range(start, end):
    curent = start
    while curent < end:
       yield curent
       curent+=1



nums_2 = my_range(1, 5)

print(next(nums_2)) # it is same thing what Myrange calss do but genetor contans iter and next method in-bulit


#iter will run tills the next method avialble

#memory efficent program iterator is best, itarble no







