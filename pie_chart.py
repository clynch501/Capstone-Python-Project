# Pie Chart of Semester Fees
import matplotlib.pyplot as plt

# Function
def main():
   # List of fees
   fees = [1100, 200, 50, 120]
   # Slice labels
   slice_labels = ['Tuition', 'Course Access Codes', 'Lab Fees', 'Textbooks']
   # Pie Chart
   plt.pie(fees, labels = slice_labels, colors=('g', 'b', 'r', 'm'), autopct = '%1.1f%%')
   # Title
   plt.title('Semester Fees Breakdown')
   # Show chart
   plt.show()

# Call Function
main()
