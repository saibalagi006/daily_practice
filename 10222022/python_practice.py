### This file has all the useful syntax for python 
### This is going to be used as a cheat sheet 

### Data Structures

############## List ########################################
## Lists are ordered, changeable, can be looped and allow duplicate values 
list1 = [1,2,3,4,5]

# Access items of a list 
print("Accessing the index 1 element of the list", list1[1])
print("Accessing the index 1 to 3 element of the list", list1[1:4])

# Change/update items of a list 
print("value of list1 at index 1 before change", list1[1])
list1[1] = -2
print("value of list1 at index 1 after change", list1[1])

# Insert new items to the list 

list1.append(9) ## adds the new element to the end of the list 
list1.insert(1,"hello") ## adds the new element to the 2nd position in the list 

# Delete items in a list 

list1.pop(1)  ## removes the element on the 1st index and returns it
list1.pop() ## removes the last element of the list and returns it
del list1[2] ##deletes the element on the 2nd index and does not return anything

# List comprehension 

list2 = [x+2 for x in list1[3:] if type(x)==int]


############### String #######################
str1 = "hello sai"
## Access a string 

print("accessing the string from index 3 onwards", str1[3:]) 

## format a string 

print(" the string is {} formatted".format((1)))

## add something to the string 
str1 = str1+"addition"

##############Tuples##############
## Tuples are ordered, unchangeable, can be looped and allow duplicate values 

tuple1 = ([x for x in range(1,5)])

## accessing the tuple elements 

print("I am accessing the element at index 3", tuple1[3])

## updating tuples 
    ## tuples cannot be changed once created. So, we convert it into a list, modify it and change it back 
u = list(tuple1)
u.append(3)
tuple1 = tuple(u)

################## set #########################
## set items are unordered, unchangeable, can be looped and do not allow duplicate values

set1 = {1,2,3}

## length of a set 

print("length of the set is ", len(set1))

############# Dictionary #################3 
## Dictionary items are ordered, changeable, can be looped and do not allow duplicate values

dict1 = {"key1": 3,"key2":4}

print(list(dict1.keys()))   ### print the keys as a list 
print(list(dict1.values())) ### print the values as a list 

### add new keys 

dict1['key3'] = 45

##update existing keys 

dict1['key2'] = 12

### delete keys-value pairs 

del dict1['key1'] ## removes the item with the specified key name 
dict1.pop('key2') ## removes the item and return the value of the specified key
dict1.popitem()  ## removes the last key-value pair and returns it as a tuple 

### looping a dictionary 

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key, value in dict1.items():
    print(key,value)
    

