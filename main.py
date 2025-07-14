import numpy as np
import matplotlib.pyplot as plt


print('1st try...')

x = np.array([1, -4, 3, 6, 9, -40, 20, 2], dtype=np.int32)

plt.plot(x, marker='o', linestyle='--', color='b')

#plt.hist( x, bins=10, color='blue', alpha=0.7, edgecolor='black')

plt.title('1st try')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()
#print(x)


for elem in sorted(x):
    print(elem)

# Create a 2-dimensional array of signed integers
x2d = np.array([[1, -4, 3], [6, 9, -40]], dtype=np.int32)
print("\n2D array:")
print(x2d, "\n")

for row in x2d:
    for elem in sorted(row):
        print(elem)

print("\nthat's all of 1st try!")
