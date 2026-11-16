"""Write a program to perform the following operations: 
1. Create a tuple with different datatypes 2. Create another
 tuple of integers 3. Create a new tuple by adding 9 to the 
 previous tuple 4. Count the occurrences of an element in the 
 tuple 5. Perform slicing on the tuple"""

tuple1 = ('a', 'b', 1, 2,)
#1
print(tuple1)

tuplen = (1, 3, 5, 7,)
#2
print(tuplen)

tuplex = tuplen + (9,)
#3
print(tuplex)

print(len(tuplex))
#4

print(tuplex[1:4])
#5