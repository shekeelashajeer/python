def getArray(size):
    
    print(f"Enter the values for the array ({size}x{size}):")
    array = []
    for i in range(size):
        row = list(map(int, input().split()))
        array.append(row)
    return array

def addArray(array1, array2, size):
   
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = array1[i][j] + array2[i][j]
    return result

def displayArray(array):
   
    print("Resultant Array:")
    for row in array:
        print("\t".join(map(str, row)))

def main():
   
    size = int(input("Enter the size of the array: "))
    
    print("Array 1:")
    array1 = getArray(size)
    
    print("Array 2:")
    array2 = getArray(size)
    
    result = addArray(array1, array2, size)
    
    displayArray(result)


if __name__ == "__main__":
    main()
