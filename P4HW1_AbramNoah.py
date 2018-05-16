# P4HW1
# cti 110
# Noah Abram
# 5/16/2018

vehicleSpeed = float( input( "What is the speed of the vehicle?: " ))
timeTraveled = int( input( "How many hours has it traveled?: " ))

print()
print( "Hour","\tDistance Traveled" )
for currentHour in range( 1, timeTraveled + 1 ):
    distanceTraveled = vehicleSpeed * currentHour
    print( currentHour, "\t", distanceTraveled)
