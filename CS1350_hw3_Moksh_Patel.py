import numpy as np

# prob 1
# part A

zeros_arr = np.zeros(8)
print("\n1. zeros_arr (1D array of 8 zeros):")
print(zeros_arr)

ones_matrix = np.ones((3, 4))
print("\n2. ones_matrix (3×4 matrix of ones):")
print(ones_matrix)

range_arr = np.arange(10, 51, 5)
print("\n3. range_arr (10 to 50 with step 5):")
print(range_arr)

linear_arr = np.linspace(0, 2, 9)
print("\n4. linear_arr (9 evenly spaced numbers from 0 to 2):")
print(linear_arr)

#part B

a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3, 4, 5])

print("\nGiven arrays:")
print(f"a = {a}")
print(f"b = {b}")

result_add = a + b
print("\n1. a + b:")
print(result_add)

result_mult = a * b
print("\n2. a * b (element-wise multiplication):")
print(result_mult)

result_square = a ** 2
print("\n3. a ** 2 (each element squared):")
print(result_square)

result_div = a / b
print("\n4. a / b (element-wise division):")
print(result_div)

sum_a = np.sum(a)
print("\n5. Sum of all elements in a:")
print(sum_a)

mean_b = np.mean(b)
print("\n6. Mean of all elements in b:")
print(mean_b)



# prob 2
# part A

matrix = np.arange(1, 21).reshape(4, 5)

print("\n1. The array itself:")
print(matrix)

print("\n2. Shape:")
print(matrix.shape)

print("\n3. Number of dimensions:")
print(matrix.ndim)

print("\n4. Total number of elements:")
print(matrix.size)

print("\n5. Data type:")
print(matrix.dtype)

print("\n6. Total bytes used:")
print(matrix.nbytes)

# part B

print("\n1. Overall mean:")
print(np.mean(matrix))

print("\n2. Overall standard deviation:")
print(np.std(matrix))

print("\n3. Minimum and maximum values:")
print(f"Minimum: {np.min(matrix)}")
print(f"Maximum: {np.max(matrix)}")

print("\n4. Sum of each row:")
print(np.sum(matrix, axis=1))

print("\n5. Mean of each column:")
print(np.mean(matrix, axis=0))

print("\n6. Index of the maximum value in the flattened array:")
print(np.argmax(matrix))




# prob 3
# part A

scores = np.array([
    [85, 90, 78, 92],
    [70, 65, 72, 68],
    [95, 98, 94, 97],
    [60, 55, 58, 62],
    [88, 85, 90, 87],
    [75, 80, 77, 82]
])
students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']
exams = ['Exam1', 'Exam2', 'Exam3', 'Exam4']


print("\n1. Carol's Exam2 score:")
print(scores[2, 1])

print("\n2. All of Alice's scores:")
print(scores[0])

print("\n3. All Exam3 scores:")
print(scores[:, 2])

print("\n4. Bob and Carol's scores on Exam1 and Exam2:")
print(scores[1:3, 0:2])

# part B 
print("\n1. Boolean mask for all scores >= 90:")
mask = scores >= 90
print(mask)

print("\n2. All scores that are >= 90:")
print(scores[mask])

print("\n3. Count how many scores are >= 90:")
print(np.sum(mask))

print("\n4. Students with average score >= 85:")
avg_scores = np.mean(scores, axis=1)
high_performers = np.array(students)[avg_scores >= 85]
print(high_performers)

print("\n5. Replace all failing scores (< 60) with 60:")
scores_modified = scores.copy()
scores_modified[scores_modified < 60] = 60
print(scores_modified)






# prob 4
# part A

print("\n1. Create a 1D array with values 1-24:")
arr_1d = np.arange(1, 25)
print(arr_1d)

print("\n2. Reshape to 4×6 matrix:")
arr_4x6 = arr_1d.reshape(4, 6)
print(arr_4x6)

print("\n3. Reshape to 2×3×4 3D array:")
arr_3d = arr_1d.reshape(2, 3, 4)
print(arr_3d)

print("\n4. Flatten the 3D array back to 1D:")
arr_flat = arr_3d.flatten()
print(arr_flat)

# part B

prices = np.array([
    [1.20, 1.50, 1.30, 1.40],
    [0.50, 0.60, 0.55, 0.45],
    [0.80, 0.90, 0.85, 0.75]
])

print("\nOriginal prices:")
print(prices)

print("\n1. Apply 10% discount to ALL prices:")
discounted = prices * 0.9
print(discounted)

print("\n2. Add $0.10 delivery fee to each store:")
delivery_fee = np.array([0.10, 0.10, 0.10, 0.10])
with_delivery = prices + delivery_fee
print(with_delivery)

print("\n3. Calculate final price with tax:")
tax_rates = np.array([0.08, 0.06, 0.07, 0.05])
final_prices = prices * (1 + tax_rates)
print(final_prices)

print("\n4. Normalize prices by subtracting each product's mean price:")
mean_prices = np.mean(prices, axis=1, keepdims=True)
normalized = prices - mean_prices
print(normalized)
