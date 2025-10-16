# Reading and Displaying the Data from the Utilities Program
def main():
    #Open monthly_bill_details.txt file as read only
    util_file = open('monthly_bill_details.txt', 'r')
    # Read the first line of the file which is the water bill
    water = util_file.readline()
    while water != '':
        # Reads the utilities
        electric = util_file.readline()
        sewer = util_file.readline()
        # Strips newlines from the fields
        water = water.rstrip('\n')
        electric = electric.rstrip('\n')
        sewer = sewer.rstrip('\n')
        #Display monthly expenses
        print('Water:', water)
        print('Electric:', electric)
        print('Sewer:',sewer)
        #Blank line for spacing
        print()
        #Field for the next record
        water = util_file.readline()
    util_file.close()
        
# Call the function
main()



