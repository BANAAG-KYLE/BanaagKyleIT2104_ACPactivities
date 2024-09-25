def calculate_discount(purchase_amount):

  if purchase_amount > 5000:
    discount_percentage = 0.1
  else:
    discount_percentage = 0.05

  discount = purchase_amount * discount_percentage
  final_price = purchase_amount - discount

  return final_price

while True:
  purchase_amount = float(input("Enter the total purchase amount: "))
  discount_percentage = 0.1 if purchase_amount > 5000 else 0.05
  final_price = purchase_amount * (1 - discount_percentage)

  print(f"Initial Purchase Amount: {purchase_amount:.2f}")
  print(f"Discount: {(purchase_amount * discount_percentage):.2f}")
  print(f"Final Price: {final_price:.2f}")

  try_again = input("Do you want to try again? (yes/no): ")
  if try_again.lower() != "yes":
    print("Thank you!")
    break