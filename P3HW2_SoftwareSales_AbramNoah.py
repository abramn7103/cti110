# P3hw2
# cti 110
# Noah Abram
# 5/12/2018

userNumberOfPackages = int( input( "Enter the number of packages bought: "))+\

packagePrice = 99

if userNumberOfPackages < 10:
    discount = 0;
elif userNumberOfPackages < 20:
    discount = 0.10;
elif userNumberOfPackages < 50:
    discount = 0.20;
elif userNumberOfPackages < 100:
    discount = 0.30;
else:
    discount = 0.40

subTotal = userNumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print( "Amount of discount: " + format(discountAmount, ",.2f" ) + \
       "Total amount: $" + format(total, ",.2f" ))
