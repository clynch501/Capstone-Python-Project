#Current cost of tuition
tuition = int(input('What is the cost of tuition?:'))
inflation = float(1.02)

print("Year\tProjected Tution\n------------------")
for x in range(5):
    #using the compound interest formula to determine the total cost due to inflation
    inflationcost = tuition*(inflation**x)
    x = x+1
    print( str(x),'\t', '$', format(inflationcost, '.2f'))

    
