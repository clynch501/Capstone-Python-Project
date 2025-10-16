# Input for days of saving pennies
days = int(input('How many days would you like to save pennies?:'))
#Accumulator
total = 0
#Value of a penny
penny = 0.01

print("Day\tPennies\n---------------")
for day in range(days):
    penniestoday = 2**day
    total = total + penniestoday
    print(day+1, "\t", '$', penniestoday*penny)

print('The total savings for day', days, 'is $', total*penny)
