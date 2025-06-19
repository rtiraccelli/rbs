import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data for bar plot
#x = [1, 2, 3, 4, 5]
#y = [2, 4, 1, 3, 5]
#plt.scatter(x, y, color='red')
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.title('Scatter Plot')
#plt.show()

# Data for histogram
#data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 10]
#plt.hist(data, bins=5, color='purple')
#plt.xlabel('Data')
#plt.ylabel('Frequency')
#plt.title('Histogram')
#plt.show()

# Data for pie chart
#labels = ['A', 'B', 'C', 'D']
#sizes = [5, 6, 79, 10]
#plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
#plt.title('Pie Chart')
#plt.show()

# Data for histogram
#data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 10]
#plt.hist(data, bins=5, color='purple')
#plt.xlabel('Data')
#plt.ylabel('Frequency')
#plt.title('Histogram')
#plt.show()


# Creating 3D Plots
#from mpl_toolkits.mplot3d import Axes3D
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
# Data for 3D plot
#x = [1, 2, 3, 4, 5]
#y = [2, 3, 5, 7, 11]
#z = [1, 4, 9, 16, 25]

#n = [2, 4, 7, 8, 9]
#o = [2, 3, 5, 7, 11]
#p = [3, 9, 16, 25, 36]

#ax.plot(x, y, z, color='blue', label='Line 1')
#ax.plot(n, o, p, color='green', label='Line 2')
#ax.set_xlabel('X-axis')
#ax.set_ylabel('Y-axis')
#ax.set_zlabel('Z-axis')
#ax.set_title('3D Plot')
#plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')
print(tips.head())

# Box plot with Seaborn
#sns.boxplot(x='day', y='total_bill', data=tips)
#plt.title('Box Plot of Total Bill by Day')
#plt.show()


# Pair plot with Seaborn
#sns.pairplot(tips)
#plt.title('Pair Plot of Tips Dataset')
#plt.show()
# Select only numeric columns for correlation matrix
#numeric_tips = tips.select_dtypes(include=['float64', 'int64'])
# Correlation matrix
#corr = numeric_tips.corr()
# Heatmap with Seaborn
#sns.heatmap(corr, annot=False, cmap='inferno', center=0)
#plt.title('Heatmap of Correlation Matrix')
#plt.show()

import plotly.express as px
import plotly.graph_objects as go

# Scatter plot with Plotly
fig = px.histogram(tips, x='total_bill', y='tip', title='Scatter Plot of Total Bill vs Tip')
fig.show()
