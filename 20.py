
def multiply_adjacent_values(input_array):
    result_array = []
    for i in range(len(input_array) - 1):
        result_array.append(input_array[i] * input_array[i + 1])
    return result_array

n = int(input("Enter the array limit: "))
print("Enter the values of array:")
input_array = [int(input()) for _ in range(n)]
output_array = multiply_adjacent_values(input_array)
print("Output:")
print(" ".join(map(str, output_array)))
