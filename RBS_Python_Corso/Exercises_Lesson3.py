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
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 10]

plt.hist(data, bins=5, color='purple')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()