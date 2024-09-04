num_rows = 5  # Number of rows in Pascal's Triangle

triangle = []

for row_num in range(num_rows):
    # Start with a row of 1s
    row = [1] * (row_num + 1)
    
    # Update the row based on the previous row
    for col in range(1, row_num):
        row[col] = triangle[row_num - 1][col - 1] + triangle[row_num - 1][col]
    
    # Append the row to the triangle
    triangle.append(row)

# Print the triangle
for row in triangle:
    print(row)
