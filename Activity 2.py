"""Write a program to check whether the 
given tuple - (1,2,3,3,2,1) is a palindrome
 or not. If it's a palindrome, then it is the
   same after being reversed."""

tuple1 = (1,2,3,3,2,1,)
if tuple1 == tuple1[::-1]:
    print("Tuple 1 is a palindrome as: \n", tuple1)
else:
    print("Tuple 1 is not a palindrome: \n", tuple1)