#Part 2: Calories
#Starting by making the function for the total calories.
def total():
    carb_calories = carb()
    fat_calories = fat()
    total = fat_calories + carb_calories
    print(f'The total number of calories is {total}')
    print(f'The calories from fat is {fat_calories}')
    print(f'The calories from carbohydrates is {carb_calories}')

# The total grams of fat and fat calories for the day.
def fat():
    fat_grams = int(input('How many grams of fat did you consume today?'))
    calories_f = fat_grams*9
    return calories_f
# The total grams of carbs and carb calories for the day.
def carb():
    carb_grams = int(input('How many grams of carbohydrates did you consume today?'))
    calories_carb = carb_grams*4
    return calories_carb

total()
