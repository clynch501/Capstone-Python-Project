#Part 1. Restuarant Selector
vegetarian = input('Is anyone is your party a vegetarian?')
vegan = input('Is anyone in your party a vegan?')
gluten = input ('Is anyone in your party gluten-free?')
if vegetarian == 'yes':
    if vegan == 'yes':
        if gluten == 'yes':
            print ('Here are your restaurant choices:')
            print ('Corner Cafe')
            print ('The Chef\'s Kitchen')
        else:
            print ('Here are your restaurant choices:')
            print ('Corner Cafe')
            print ('The Chef\'s Kitchen')
    else:
        if gluten == 'yes':
            print ('Here are your restaurant choices:')
            print ('Main Street Pizza Company')
            print ('Corner Cafe')
            print ('The Chef\'s Kitchen')
        else:
            print ('Here are your restaurant choices:')
            print ('Main Street Pizza Company')
            print ('Corner Cafe')
            print ('Mama\'s Fine Italian')
            print ('The Chef\'s Kitchen')
else:
    if vegan == 'yes':
        if gluten == 'yes':
            print ('Here are your restaurant choices')
            print ('Corner Cafe')
            print ('The Chef\'s Kitchen')
        else:
            print ('Here are your restaurant choices')
            print ('Corner Cafe')
            print ('The Chef\'s Kitchen')
    else:
        if gluten == 'yes':
            print ('Here are your restaurant choices')
            print ('Main Street Pizza Company')
            print ('Corner Cafe')
            print ('The Chef\'s Kitchen')
        else: 
            print ('Here are your restaurant choices:')
            print ('Joe\'s Gourmet Burgers')
            print ('Main Street Pizza Company')
            print ('Corner Cafe')
            print ('Mama\'s Fine Italian')
            print ('The Chef\'s Kitchen')

#Part 2. Age Classifier
age = float(input('What is your age?'))
if age <= 1:
    print ('You are an infant')
if age < 13:
    if age > 1:
        print ('You are a child')
if age >= 13:
    if age <20:
        print ('You are a teenager')
if age >= 20:
    print ('You are an adult')

#Part 3. Roman Numerals
number = int(input('Please input any number between 1 and 10:'))
if number == 1:
    print ('I')
if number == 2:
    print ('II')
if number == 3:
    print ('III')
if number == 4:
    print ('IV')
if number == 5:
    print ('V')
if number == 6:
    print ('VI')
if number == 7:
    print ('VII')
if number == 8:
    print ('VIII')
if number == 9:
    print ('IX')
if number == 10:
    print ('X')
if number <1:
    if number >10:
        print ('Error. Number not within range')


    
    
    
