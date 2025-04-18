# user input for Rectangle A
lengthA =float(input('Enter length of rectangle A: '))
widthA = float(input('Enter width of rectangle A: '))

# user input for rectangle B
lengthB = float(input('Enter length of rectangle B: '))
widthB = float(input('Enter width of rectangle B: '))

# math to get area of user rectangle A
areaA = lengthA * widthA

# math to get area of user rectangle B
areaB = lengthB * widthB

# output of area of rectangles
print(f'The Area of A is {areaA:.1f}')
print(f'The Area of B is {areaB:.1f}')

# if statements comparing the rectangle areas

if areaA > areaB:
    print('Area A is greater than Area B.')  # For A > B
else:  # The 'else' connects directly to the first 'if'
    if areaB > areaA:  # Nested 'if' to check B > A
        print('Area B is greater than Area A.')  # For B > A
    elif areaB == areaA:  # Now the 'elif' is part of the nested structure
        print('Area A is equal to Area B.')