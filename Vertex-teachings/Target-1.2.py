a = float(input("Enter total bill:"))
b = float(input("Enter total tip:"))
c = float(input("Enter number of people:"))
total = (a*(1+b/100))/c
print("Total cost to be paid by everyone is:"+ str(round(total,2)))