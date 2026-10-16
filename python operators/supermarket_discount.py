# Supermarket Discount Program

purchase_amount = float(input("Enter total purchase amount: "))

# Check if customer qualifies for discount
if purchase_amount >= 10000:
    discount = 0.15 * purchase_amount
else:
    discount = 0

# Calculate final amount
final_amount = purchase_amount - discount

# Display results
print("\nPurchase Details")
print("Purchase Amount: KSh", purchase_amount)
print("Discount: KSh", discount)
print("Final Amount: KSh", final_amount)
