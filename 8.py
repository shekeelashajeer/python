limit = int(input("Enter a limit: "))
sum_of_odds = sum(num for num in range(1, limit +1) if num % 2 != 0)
print(f"Sum of odd number = {sum_of_odds}")