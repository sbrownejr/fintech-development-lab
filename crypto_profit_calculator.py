print("Crypto Profit Calculator")
crypto_name = input("Enter the cryptocurrency name: ")
purchase_price = float(input("Enter the purchase price: "))
current_price = float(input("Enter the current price: "))
coins_owned = float(input("Enter the number of coins owned: "))
initial_investment = purchase_price * coins_owned
current_value = current_price * coins_owned
profit_loss = current_value - initial_investment
return_percent = (profit_loss / initial_investment) * 100
print()
print(f"Results for {crypto_name}:")
print(f"Initial investment: ${initial_investment:,.2f}")
print(f"Current value: ${current_value:,.2f}")
print(f"Profit or loss: ${profit_loss:,.2f}")
print(f"Return: {return_percent:.2f}%")