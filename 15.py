def getArray(arr, size):
    print("Enter the value of array:")
    for i in range (size):
        arr[i] = int(input(f"Element {i+1}: "))
def displayArray(arr, size):
    print("The array values are:")
    for i in range (size):
        print(arr[i], end=" ")
    print()

def main():
    size = int(input("Enter the size of array: "))
    arr = [0] * size

    getArray(arr, size)
    displayArray(arr, size)

if __name__ ==" __main__":
    main()

