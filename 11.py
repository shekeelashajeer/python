size = int(input("Enter the size of an array: "))
array = list(map(int, input("Enter the values of the array separated by commas: ").replace("","").split(',')))

even_count = sum(1 for num in array if num % 2 == 0)

print(f"Number of even number is given in the array is {even_count}.")