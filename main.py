import numpy as np

print('1st try...')

x = np.array([1, -4, 3, 6, 9, -40, 20, 2], dtype=np.int32)
#print(x)


for elem in sorted(x):
    print(elem)

# Create a 2-dimensional array of signed integers
x2d = np.array([[1, -4, 3], [6, 9, -40]], dtype=np.int32)
print("2D array:")
print(x2d)

for row in x2d:
    for elem in sorted(row):
        print(elem)

print("that's all of 1st try!")
