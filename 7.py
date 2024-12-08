number = int(input("Enter the number: "))
print(f"Multiplication table for {number}: ")
for i in range(1, 11):
    print(f"{i}*{number} = {i*number}")