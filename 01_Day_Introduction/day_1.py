import math

# Operations
print ('Operations in Print statements.')
num1, num2 = 3, 4
print ('Addition: ', num1 + num2)
print ('Subtraction: ', num1 - num2)
print ('Multiplication: ', num1 * num2)
print ('Modulus1: ', num1 % num2)
print ('Modulus2: ', num2 % num1)
print ('Division: ', num1 / num2)
print ('Exponential: ', num1 ** num2)
print ('Floor Division1: ', num1 // num2)
print ('Floor Division2: ', num2 // num1)

# Strings
print ('\nWrite out Strings')
strSet = ['Christian', 'Moore', 'USA', 'I am enjoying 30 days of Python']
for i in strSet:
    print (i)

# Check Data Types
print ('\nCheck Data Types')
print(type(10))
print(type(9.81))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(strSet[0]))
print(type(strSet[1]))
print(type(strSet[2]))

# Different Examples of types
print (type(-20))
print (type(5.018))
print (type(5-1j))
print (type('Calculus'))
print (type(True))
print (type([2.3, 4.5]))
print (type(('Bacon', 'Maple')))
print (type({2, 3, 4}))
print (type({
    'name':'Christian',
    'Occupation':'Child of God'
    }))

# Euclidean Distance
P1 = {
    'x':2,
    'y':3
}
P2 = {
    'x':10,
    'y':8
}
dist = math.sqrt( (P2['x'] - P1['x']) ** 2 + (P2['y'] - P1['y']) ** 2 )
print ('The distance between ', P1, ' and ', P2, ' is ', dist, '.')
