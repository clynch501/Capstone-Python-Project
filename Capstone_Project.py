# Capstone Project
# Assignments & Parts for Reference
# Assignment 1 - Binary Digits
# Assignment 2 - Egg Prices and Temperature Conversion
# Assignment 3 - Restaurant Selector, Age Classifier, & Roman Numerals
# Assignment 4 - Penny Savings and Price Increase
# Assignment 5 - Property Tax Calculator, Calories per Day, Basketball Ticket Sales
# Assignment Turle Graphics - Shapes using Turtle Graphics
# Assignment 6 - Saving and Reading Employee Records, Saving and Reading Monthly Utilities
# Assignment Algorithm Workbench - Algorithm Workbench
# Assignment 7 - Storing Student Grades, Bar Chart for student graduating, Pie Chart for student expenses
# Assignment 8 - Phonebook

# Global Constants for Menu Options 
A1 = 1
A2a = 2
A2b = 3
A3 = 4
A4a = 5
A4b = 6
A5a = 7
A5b = 8
A5c = 9
AT = 10
A6a = 11
A6b = 12
AAW = 13
A7a = 14
A7b = 15
A7c = 16
A8 = 17
Quit = 18

def main():
    # User's Menu choice
    choice = 0
    while choice != Quit:
        choice = menu_choice()
        if choice == A1:
            import binary_digits
        elif choice == A2a:
            import EggPrices
        elif choice == A2b:
            import Temperatureconversion    
        elif choice == A3:
            import Assignment3    
        elif choice == A4a:
            import penny_savings
        elif choice == A4b:
            import price_increase  
        elif choice == A5a:
            import property_tax
        elif choice == A5b:
            import calories_per_day
        elif choice == A5c:
            import basketball_tickets
        elif choice == AT:
            import shapes_graphics_mod
        elif choice == A6a:
            import save_read_emp_records
        elif choice == A6b:
            import save_monthly_utility
            import read_monthly_utility
        elif choice == AAW:
            import Algorithm_Workbench
        elif choice == A7a:
            import student_grades
        elif choice == A7b:
            import bar_chart    
        elif choice == A7c:
            import pie_chart    
        elif choice == A8:
            import Phonebook
    # Thank you message
    if choice == Quit:
        print('Thank you for using my collection of programs!')
        
def menu_choice():
    print('Welcome to my Python programming portfolio! Here is a menu of the 17 programs I made this semester.')
    print('-------------------------------------------------------------------------------------------------')
    print('1. Binary Digits: Displays my name in binary.')
    print('2. Egg Prices: Determines the cheapest egg prices.')
    print('3. Temperature Conversion: Converts from Celsius to Fahreneheit.')
    print('4. Restaurant Selector: Determines what restaurants to go to given certain dietary restrictions.')
    print('   Age Classifier: Determines what age bracket your are in.')
    print('   Roman Numerals: Displays the roman numeral for any number from 1-10')
    print('5. Penny Savings: Calculates savings of pennies given a certain number of days.')
    print('6. Price Increase: Calculates inflation cost of tuition.')
    print('7. Property Tax Calculator: Calculates the property tax.')
    print('8. Calories Per Day: Calorie tracker for fat and carbs.')
    print('9. Basketball Ticket Sales: Calculates total revenue for a basketlball game.')
    print('10. Turtle Graphics: Displays shapes using Turtle.')
    print('11. Saving and Reading Employee Records: Creates a readable file of employee records.')
    print('12. Saving and Reading Monthly Utilities: Creates a readable file of monthly utlities.')
    print('13. Algorithm Workbench: Creates lists')
    print('14. Storing Student Grades')
    print('15. Bar Chart for Students Graduating Each Year.')
    print('16. Pie Chart for Student Expenses')
    print('17. Phonebook: Creates a phonebook with entries that can be modified and removed. ')
    print('18. Quit program')
    print()
    # Menu choice
    choice = int(input('Which program would you like to run?:'))
    # For when a number outside the menu is entered
    while choice < 1 or choice > 18:
        try: choice = int(input('Please enter a number listed on the menu:'))
        except ValueError:
            choice = int(input('Please enter a number listed on the menu:'))

    return choice

# Call main function
main()
