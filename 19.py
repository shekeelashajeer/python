
def calculate_income_tax(annual_income):
    tax = 0.0

    if annual_income > 10000000:
        tax += (annual_income - 10000000) * 0.30
        annual_income = 10000000
    if annual_income > 5000000:
        tax += (annual_income - 5000000) * 0.20
        annual_income = 5000000
    if annual_income > 250000:
        tax += (annual_income - 250000) * 0.05

    return tax

annual_income = float(input("Enter the annual income: "))

tax_amount = calculate_income_tax(annual_income)

print(f"Income tax amount = {tax_amount:.2f}")
