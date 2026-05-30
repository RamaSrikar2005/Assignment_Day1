bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

tip_amount = (bill * tip_percent) / 100
total_bill = bill + tip_amount
amount_per_person = total_bill / people


remainder = total_bill % people

print("\n===== BILL SUMMARY =====")
print(f"Original Bill      : {bill}")
print(f"Tip Amount         : {round(tip_amount,2)}")
print(f"Total with Tip     : {round(total_bill,2)}")
print(f"Amount Per Person  : {round(amount_per_person,2)}")
print(f"Remainder          : {round(remainder,2)}")
print("========================")