import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r"C:\Users\KYALO\finance\food_inflation.xlsx", sheet_name="food_inflation")


months = df['Month']
sales = df['food_inflation']


plt.plot(months, sales, marker='o', linestyle='-', color='b')


plt.title('month over food_inflation')
plt.xlabel('Month')
plt.ylabel('food_inflation')


plt.show()





import pandas as pd
import matplotlib.pyplot as plt

# Load data from the first Excel file
df1 = pd.read_excel(r"C:\Users\KYALO\finance\food_inflation.xlsx", sheet_name="food_inflation")

# Load data from the second Excel file
df2 = pd.read_excel(r"C:\Users\KYALO\finance\another_inflation.xlsx", sheet_name="another_inflation")

# Combine the data
# Assuming both files have the same structure
combined_df = pd.concat([df1, df2])

# You may want to handle duplicate months or combine values if they overlap
# For simplicity, this code assumes there are no duplicates and just concatenates the data

months = combined_df['Month']
sales = combined_df['food_inflation']

# Plotting the bar chart
plt.bar(months, sales, color='b', alpha=0.7)

plt.title('Month over Food Inflation')
plt.xlabel('Month')
plt.ylabel('Food Inflation')

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit labels

plt.show()


