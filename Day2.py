print("Welcome to tip calculator.")
bill = float(input("What was the total bill? : "))
tip_perc = int(input("What percentage tip would you like to give? 10, 12, or 15? :"))
people = int(input("How mant people you  will splitt the bill? :"))
total_bill = (bill + (bill * (tip_perc/100)))/ people
splitted_bill = round(total_bill, 2)
splitted_bill = "{:.2f}".format(total_bill)
print(splitted_bill)
print(f"Each person should pay ${splitted_bill}")
