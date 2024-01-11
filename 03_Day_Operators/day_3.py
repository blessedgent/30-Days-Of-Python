import math

# Set up a loop and switch statement to be able to test each case without trigerring all the others and loop back so I don't have to recompile.
keepLooping = True

while keepLooping:

    probNum = int( input ('\nWhat problem number do you wish to test?' ) )

    match probNum:
        
        case 1: # Declare your age as an integer variable
            myAge = int(32) # in years

        case 2: # Declare your height as a float variable
            myHeight = float(5 + (11 / 12)) # in feet

        case 3: # Declare a variable that store a complex number
            complexNumber = 7+2j

        case 4: # Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
            # Can one input be used to gether multipe values at once? Yes!!
            triangleBase = float( input ('Please enter the length of the triangle base: ') )
            triangleHeight = float( input ('Please enter the length of the triangle height: ') )
            # var1, var2 = input('Var1'), input('Var2')
            triangleArea = (triangleBase * triangleHeight) / 2
            print ('The area of the triangle is ', triangleArea, '.')
            print()

        case 5: # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
            sideA, sideB, sideC = float(input('Side a: ')), float(input('Side b: ')), float(input('Side c: '))
            print ('The perimeter of the triangle is ', (sideA + sideB + sideC))
            print()

        case 6: # Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
            rectLength, rectHeight = float(input('Length: ')), float(input('Height: '))
            print ('The perimeter of the rectangle is ', 2 * (rectHeight + rectLength))
            print ('The area of the rectangle is ', (rectHeight * rectLength))

        case 7: # Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
            radius = float(input('Radius: '))
            print ('The circumference of the circle is ', 2 * math.pi * radius)
            print ('The area of the circle is ', (radius ** 2) * math.pi )    

        case 8: # Calculate the slope, x-intercept and y-intercept of y=2x-2. (Take equation as input)
            equation = input ('Enter the linear equation: y=')
            equation = equation.replace(' ', '').replace('+', ' +').replace('-', ' -').lstrip()
            termList = equation.split(' ')
            print (termList)
            for i in termList:
                if 'x' in i:
                    slope = i.replace('x','')
                    if slope == '+' or len(slope) == 0:
                        slope = 1
                    elif slope == '-':
                        slope = -1
                else:
                    yInt = i
            xInt = -1 * float(yInt) / float(slope)
            print ('The slope is ', slope, ', the y-intercept is (0,', yInt, '), and the x-intercept is (', xInt,', 0).')

        case 9: # Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
            slope2 = (10 - 2) / (6 - 2)
            print ('The Euclidean distance between (2, 2) and (6, 10) is ', math.sqrt((10 - 2) ** 2 + (6 - 2) ** 2), '.')
            print ('The slope between (2, 2) and (6, 10) is ', slope2, '.')

        case 10: # Compare the slopes in tasks 8 and 9. Must run cases 8 and 9 before this case.
            slope = float(slope)
            if slope == slope2:
                comparison = 'equal to'
            elif slope > slope2:
                comparison = 'greater than'
            else:
                comparison = 'less than'
            print (slope, ' is ', comparison, slope2, '.')

        case 11: # Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
            x = float( input ("Please enter an x value for y=x^2+6x+9. x=") )
            y = x ** 2 + 6 * x + 9
            print ('The value of y for y=(',x,')^2+6(',x,')+9 is ', y, '.')

        case 12: # Find the length of 'python' and 'dragon' and make a falsy comparison statement.
            print ('The lengths of "python" and "dragon" are the same. ', ( len('python') != len('dragon') ))

        case 13: # Use and operator to check if 'on' is found in both 'python' and 'dragon'
            onBool = ('on' in 'python') and ('on' in 'dragon')
            print ('"python" and "dragon" both have the substring "on" in them. ', onBool)

        case 14: # I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
            jargonBool = 'jargon' in 'I hope this course is not full of jargon.'
            print ('"I hope this course is not full of jargon." contains "jargon". ', jargonBool)

        case 15: # There is no 'on' in both dragon and python
            onBool = ('on' not in 'python') or ('on' not in 'dragon')
            print ('Neither "python" nor "dragon" have the substring "on" in them. ', onBool)

        case 16: # Find the length of the text python and convert the value to float and convert it to string
            strLength = str( float( len('python') ) )
            print ('Length of "python" is ', strLength, ' and is of the type', type(strLength), '.')

        case 17: # Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
            print('Use modulo (% 2) after any numeric value and get 0 to determine when a value is even or get 1 when it is odd.')

        case 18: # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
            print ( (7 // 3) == int(2.7) )

        case 19: # Check if type of '10' is equal to type of 10
            print ( type('10') == type(10) )

        case 20: # Check if int('9.8') is equal to 10
            print( int(9.8) == 10 )

        case 21: # Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
            hours = float( input ('Enter hours: ') )
            rate = float( input ('Enter rate per hour: ') )
            print ('Your weekly earning is ', hours * rate, '.')

        case 22: # Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
            years = float( input('Enter number of years you have lived: ') )
            print ('You have lived for ', years * 365.25 * 24 * 60 * 60, ' seconds.')

        case 23: # Write an exponential table script
            for i in range(1, 6):
                expLine = '%i | ' % i
                for j in range(0, 4):
                    expLine += '%i ' % (i ** j)
                print (expLine)

        case _: # Default. No valid selection made.
            print ('No valid selection was made. Please try again.')
        
    response = input ('Do you wish to test another problem? (Y/N) ').lower()
    if response == 'n':
        keepLooping = False
