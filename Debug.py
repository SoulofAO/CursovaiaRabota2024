import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]

plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Line Plot of Data')
plt.show()