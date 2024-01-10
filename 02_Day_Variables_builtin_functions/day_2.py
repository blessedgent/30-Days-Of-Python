import math

radius = 30
circum_of_circle = (radius * 2) * math.pi
area_of_circle = (radius ** 2) * math.pi

print ('The circumference of a circle with radius ', radius, 'm is ', circum_of_circle, 'm.')
print ('The area of a circle with radius ', radius, 'm is ', area_of_circle, 'm^2.\n')

radius = float(input ('Please enter the radius of the circle: '))
circum_of_circle = (radius * 2) * math.pi
area_of_circle = (radius ** 2) * math.pi
print ('The circumference of a circle with radius ', radius, 'm is ', circum_of_circle, 'm.')
print ('The area of a circle with radius ', radius, 'm is ', area_of_circle, 'm^2.\n')
