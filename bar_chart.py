# Bar Chart for Graduation of number of students for 5 years
import matplotlib.pyplot as plt

#Function
def main():
    # List of left edges of each bar
    left_edges = [5, 10, 15, 20, 25] 
    # List of heights(Number of Students) for each bar
    heights = [25, 20, 35, 40, 50]
    #Chart
    plt.bar(left_edges, heights, color = ('r', 'b', 'r', 'b', 'r'))
    # Title
    plt.title('Graduation of Students Per Year')
    # Labeling Axis
    plt.xlabel('Year')
    plt.ylabel('Number of Students Graduated')
    # Tick Mark Labels
    plt.xticks([5, 10, 15, 20, 25],
              [2020, 2021, 2022, 2023, 2024])
    #Show chart
    plt.show()

# Call function
main()
