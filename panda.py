import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students_marks.csv")

data['Average'] = data[['Maths', 'Physics', 'Chemistry']].mean(axis = 1)

# plt.bar(data['Name'], data['Average'], color = 'skyblue')
# plt.xlabel("Students")
# plt.ylabel("Average Marks")
# plt.title("Average Marks of Students")
# plt.show()

data.to_csv("students_cleaned.csv", index=False)