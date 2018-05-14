#CTI-110
#P2HW2 - Distance Traveled
#Noah Abram
#2/18/18


# Get the projected total sales.
total_price = float (input ( 'Enter the price of your food: '))

#Calculate the tip as 18 percent of total price.
tip = total_price * 0.18

#Calculate the tax as 7 percent of total price.
tax = total_price * 0.07

#Display the tip.
print ('The tip you should pay is $', format(tip, ',.1f'))

#Display the tax.
print ('The tax is $', format(tax, ',.07f'))
