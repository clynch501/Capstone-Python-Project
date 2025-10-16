
def main():
    # Total monthly utilities and estimation for desired number of months
    months = int(input('How many months of utilities do you want to calculate?'))

    # Writing to a file
    with open('monthly_bill_details.txt','w') as util_file:
        #Total expenses for specified months
        for count in range(1, months+1):
            # Water, Electric, Sewer
            print(f'Enter amount for each bill in month #{count}')
            water = float(input('How much is the water bill?'))
            electric = float(input('How much is the electric bill?'))
            sewer = float(input('How much is the sewer bill?'))
            #Writing the data to the file
            util_file.write(f'{water}\n')
            util_file.write(f'{electric}\n')
            util_file.write(f'{sewer}\n')
            # Blank line for spacing
            print()
    print('Monthly utility expenses written to monthly_bill_details.txt.')


# Call main function
main()



    
            

