string = input("Enter the string: ")
string_lower = string.lower()
if string_lower == string_lower[::-1]:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")