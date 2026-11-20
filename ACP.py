tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

add1 = 1
add2 = 1

for i in tup1:
    add1 = add1 * i

for i in tup2:
    add2 = add2 * i

print(tup1)
print("Tup 1 with all digits multiplied is: ", add1)

print(tup2)
print("Tup 2 with all digits multiplied is: ", add2)