#User Input
CarSpeed = int(input('Enter the speed the car is traveling:'))

#Math for Distance Traveled
DistanceTraveled1 = CarSpeed * 5 # Math for 5 hours
DistanceTraveled2 = CarSpeed * 10 # Math for 10 hours
DistanceTraveled3 = CarSpeed * 15 # Math for 15 hours

#Print Statements for math
print('The car will travel the following distances:')
print(DistanceTraveled1, 'miles in 5 hours.')
print(DistanceTraveled2, 'miles in 10 hours.')
print(f'{DistanceTraveled3:,} miles in 15 hours.')