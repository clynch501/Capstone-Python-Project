def main():
    # Input for desired number of employee records
    num_emps = int(input('How many employee records' + ' do you want to create?'))
    # Writing to a file
    with open('employee.txt','w') as emp_file:
        #Data for each employee
        for count in range(1, num_emps +1):
            # Get data for employee
            print(f'Enter data for employee #{count}')
            name = input('Name:')
            id_num = input('ID number: ')
            dept = input('Department:')
            #Writing the data to the file
            emp_file.write(f'{name}\n')
            emp_file.write(f'{id_num}\n')
            emp_file.write(f'{dept}\n')
            #Blank line
            print()
    print('Employee records written to employees.txt.')

# Call main function
main()



