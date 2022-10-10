## In this file, we learn/practice lambda function

## lambda function can be used when we want to create simple functions 

lambda1 = lambda s: s*10
print(lambda1(5))

## the above lambda function is same as the below function 
def lambda1_func(s):
    return s*10
print(lambda1_func(5))

## lambda can take multiple agruments 
mult = lambda x,y:x*y
print(mult(1,2))

## Lambda use case 1
points2D = [(1,2),(2,3),(0,5)]
pointed2D_sorted = sorted(points2D)
print(pointed2D_sorted) ## by default, sorted sorts using the first element of the tuple 

## to sort using the second element of the tuple 
pointed2D_sorted_y = sorted(points2D,key=lambda x: x[1])
print(pointed2D_sorted_y)

## lamnda expression is used in map, filter and reduce 

## map (func,seq)
a = [1,2,3,4]
map1 = map(lambda x:x*2,a)
print(map1) ## will print map 
print(list(map1)) ## will print the list 

## the above can be achieved using a list comprehension 
print([2*x for x in a])

##filter(fnc,seq) ##it will return the subset of elements where the lambds function is true 
filter1 = filter(lambda x:x%2==0,a)
print(filter1)
print(list(filter1))
print([x for x in a if x%2==0])


##reduce function. It applies the function until we get a single value at the end 

from functools import reduce
reduce1 = reduce(lambda x,y:x+y,a) ## the lamnda function always has 2 arguments 
print(reduce1) ## it prints a single number
