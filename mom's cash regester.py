subtotal = float(input("Enter Subtotal "))
whatyouwanttopay = int(input("Enter What You Want To Pay With "))
sales_tax = 1.06
total = round(subtotal * sales_tax, 2)
change = round(whatyouwanttopay - total, 2)
if change < 0:
    print("Im sorry, you dont have enough money to pay for your items")
    exit()
print(f"Your Total For Today Is ${total}")
print(f"Your Change For Today Is ${change}")
print("Thank You For Shopping With Us")

