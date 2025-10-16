# Dictionary Phonebook

# Menu Options
Display_all = 1
Look_up = 2
Add = 3
Change = 4
Delete = 5
Quit = 6

# Main Function
def main():
    # Empty dictionary
    phone_numbers = {}
    # User's choice
    choice = 0
    while choice != Quit:
        choice = menu_choice()
        if choice == Display_all:
            print(phone_numbers)
        elif choice == Look_up:
            look_up(phone_numbers)
        elif choice == Add:
            add(phone_numbers)
        elif choice == Change:
            change(phone_numbers)
        elif choice == Delete:
            delete(phone_numbers)
# Lookup entries          
def look_up(phone_numbers):
    name = input('Enter a name:')
    print(phone_numbers.get(name, 'Not found.'))

# Adding entries
def add(phone_numbers):
    name = input('Enter a name:')
    number = input('Enter the phonenumber:')
            # Adding name and number to dictionary
    if name not in phone_numbers:
        phone_numbers[name] = number
    else:
        print('There is already someone in the phonebook with that name.')
# Changing entries
def change(phone_numbers):
    name = input('Enter a name:')
    if name in phone_numbers:
        number = input('Enter a new phone number:')
        phone_numbers[name] = number
    else:
        print('That name is not in the phonebook.')   
# Deleting entries
def delete(phone_numbers):
    name = input('Enter a name:')
    if name in phone_numbers:
        del phone_numbers[name]
    else:
        print('That name is not in the phonebook.')

# Function for User's Menu Choice
def menu_choice():
    print('Phonebook')
    print('----------------------')
    print('1. Display all phone numbers in phonebook')
    print('2. Look up a phone number')
    print('3. Add a new phone number')
    print('4. Change a phone number')
    print('5. Delete a phone number')
    print('6. Quit phonebook program')
    print()
    # User's choice
    choice = int(input('Enter your choice for the menu:'))
    # When a number outside of the given menu options is entered
    while choice < 1 or choice > 6:
        try: choice = int(input('Enter a number listed on the menu:'))
        except ValueError:
            choice = int(input('Enter a number listed on the menu:'))

    return choice

# Call the main function
main()
