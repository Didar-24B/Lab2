#1
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
#banana

#2
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
#['banana', 'cherry']

#3
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
#['banana', 'cherry']