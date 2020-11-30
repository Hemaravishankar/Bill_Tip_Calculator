bill = float(input("Enter your Bill amount: "))
tip = int(input("Enter your tip percentange on bill like 10, 12 or 15: "))
person = int(input("How many would u want share: "))

tip_percentage = tip / 100
total_bill_amount = bill * tip_percentage
total_bill = bill + total_bill_amount
each_person_bill = total_bill / person
final_amount = round(each_person_bill, 2)
print(f"Each person should pay {final_amount}")