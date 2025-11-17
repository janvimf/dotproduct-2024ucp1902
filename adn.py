# Simple vector addition in Python

# Define two vectors
v1 = [1, 2, 3]
v2 = [4, 5, 6]

# Add the vectors element-wise
result = [v1[i] + v2[i] for i in range(len(v1))]

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Sum:", result)

