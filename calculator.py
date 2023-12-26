#calculator
total = float(input("what was the total bill ?\n"))
persons = int(input("how many people to split the bill ? \n"))
percentage = int(input("how percentage tip would you like to give ? 10, 12, or 15 ? \n"))
tip_to_pay = (total * percentage ) / 100
bill_per_person = (tip_to_pay + total) / persons
share = round(bill_per_person ,2)
print(f"Each person should pay share {share}")