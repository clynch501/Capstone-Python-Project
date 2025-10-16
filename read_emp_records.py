def main():
    #Open employee.txt file
    with open('employee.txt', 'r') as emp_file:
        name = emp_file.readline()
        while name != '':
            id_num = emp_file.readline()
            dept = emp_file.readline()
            # Strips newlines from the fields
            name = name.rstrip('\n')
            id_num = id_num.rstrip('\n')
            dept = dept.rstrip('\n')
            #Display record
            print(f'Name:{name}')
            print(f'ID:{id_num}')
            print(f'Dept:{dept}')
            print()
            # Read the name field of the next record
            name = emp_file.readline()
main()
