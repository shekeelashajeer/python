size = int(input("Enter the size of an array: "))
array = list(map(int, input("Enter the value of an array separated by commas: ").split(',')))
 
array.sort(reverse=True)
print("Sorted array:")
print(", ".join(map(str, array)))