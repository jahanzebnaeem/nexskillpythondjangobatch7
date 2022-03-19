# import random
#
# randomNumber = random.randint(1, 100)
#
# if randomNumber > 85:
#     print('You are made for each other.')
# elif randomNumber <= 85 and randomNumber >= 50:
#     print('You are competable')
# else:
#     print('Don\'t bother')

# myList = [1, 2, 3, 4, 5, 6, 7]
# mymat = [(1,2,5), (3,4,3), (5,6,7), (7,8,8), (9,10,9)]
#
# for val1,val2,val3 in mymat:
#     print(val1)

# myDict = {'name': 'jahanzeb', 'age': 24, 'city': 'lahore'}
#
# for val in myDict:
#     print(type(val))
#     print(type(myDict[val]))

# for n in range(2, 10):
#     print('n equals: ' + str(n))
#     for x in range(2, n):
#         print('x equals: ' + str(x))
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)

def sum(num1, num2):
    print(num1 + num2)

sum(2, 5)
sum(3, 6)
sum(4, 14)
