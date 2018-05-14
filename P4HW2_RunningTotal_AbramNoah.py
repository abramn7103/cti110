# P4HW3
# cti 110
# Noah Abram
# 3/25/2018

total=0
for i in range(5):
    newNumber = int (input( "Enter a number:"))
    if newNumber == 0:
        total += 1
print ("You entered a total of",total,"zeros")
