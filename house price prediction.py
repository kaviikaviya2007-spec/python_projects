print("\t\tHOUSE PRICE PREDICTION\n")

area = int(input("Enter Area (in sq ft): "))
bhk = int(input("Enter Number of BHK: "))
house_type = input("Enter House Type (Rent/Wholesale): ")
age = int(input("Enter House Age (years): "))
location = input("Enter Location (Urban/Rural): ")

# House Price Prediction
if area >= 2000 and bhk >= 3 and age <= 5:
    price = "₹80 Lakhs"
elif area >= 1200 and bhk >= 2 and age <= 10:
    price = "₹50 Lakhs"
else:
    price = "₹30 Lakhs"

print("\n========== HOUSE PRICE PREDICTION ==========\n")

print("Area             :", area, "sq.ft")
print("BHK              :", bhk)
print("House Type       :", house_type)
print("House Age        :", age, "years")
print("Location         :", location)
print("Predicted Price  :", price)