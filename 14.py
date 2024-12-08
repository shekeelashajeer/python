size = int(input("Enter the size of arrays: "))
print("Enter the value of array 1:")
array1 = []
for i in range(size):
    row = list(map(int, input().split()) )
    array1.append(row)

print("Enter the value of array 2:")
array2 = []
for i in range(size):
    row = list(map(int, input().split()) )
    array2.append(row)

sum_array = []
for i in range(size):
    row_sum = []
    for j in range(size):
        row_sum.append(array1[i][j] + array2[i][j])
    sum_array.append(row_sum)

print("Sum of 2 arrays is:")
for row in sum_array:
    print(" ".join(map(str, row)))
