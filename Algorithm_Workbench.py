# Algorithm Workbench
# 1. Names List
scientists = [ 'Einstein', 'Newton', 'Copernicus', 'Kepler']

# 2. Using for loop to display the list
for n in scientists:
    print(n)

# 3. Making 100 elements for the numbers list
numbers1 = []
i = 0
while i<100:
    numbers1.append(i)
    i += 1
# Copying numbers1 to numbers2 list
numbers2 = [item for item in numbers1]

# 5. Totaling values in a list
total = sum(numbers2)
print('Total of values in numbers2 list:' ,total)

# 6. Names list, determining if Ruby is in the list
names = ['John', 'Jeff', 'Jane', 'Janice']
if 'Ruby' in names:
    print('Hello Ruby')
else:
    print('No Ruby')

# 7.
list1 = [40,50,60]
list2 = [10,20,30]
list3 = list1 + list2
print(list3)

# 8. Making a list of squared values from list1
list4 = [item**2 for item in list1]
print(list4)

# 9. Making a list from list1 with values greater than 100
list5 = []
for n in list1:
    if n >100:
        list5.append(n)
# There are no numbers greater than 100 in list1 so list5 should remain empty
print(list5)

# 10. Making a list with even numbers from list1

list6 = [item for item in list1 if item % 2 == 0]
print(list6)

# 11. 2 Dimensional list with 5 rows and 3 columns
columns = 3
rows = 5
list2D = [[0 for x in range(columns)] for y in range(rows)]
for x in range(3):
    for y in range(5):
        list2D[y][x] = input('What integer would you like this row {} and column {} to be?'.format(y+1, x+1))
print(list2D)



