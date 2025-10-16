# Making a list of student grades
import statistics
from statistics import mean
# Function for analyzing the data inputted
def main():
    grades = scores()
    # Converting the list of strings to a list of intergers
    list0 = list(map(int,grades))
    stat_mean = statistics.mean(list0)
    length = len(grades)
    total = total_grades(grades)
    average = total/length
    highest = max(grades)
    lowest = min(grades)
    print('The length of the list of grades is:', length)
    print('The average of all the grades is:', round(average))
    print('The total combined score of the grades is:', total)
    print('The highest of all of the grades is:', highest)
    print('The lowest of all of the grades is:', lowest)
    print('The mean of the grades using the statistics module is:', round(stat_mean))

# Function for inputting grades
def scores():
    # Empty List
    scores = []
    another = 'y'
    while  another == 'y':
        grade = input('Enter the grade for a student:')
        # Adding the inputted grade to the list
        scores.append(grade)
        # Inputting another grade
        print('Would you like to add another student\'s grade?')
        another = input('y = yes, or n = no:')
        print()
    return scores

# Function for the totaling of the list of grades
def total_grades(list1):
    # Accumulator variable
    total = 0
    for number in list1:
        # Adding the number/grade to the accumulator
        total += int(number)
    return total

main()

