day_number = int(input("Enter the number (1 -7): "))
days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}
day = days.get(day_number, "Invalid Entry")
print(day)