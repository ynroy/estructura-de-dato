transactions = []

def deposit(amount):
  transactions.append({'type': 'deposit', 'amount': amount})

def withdraw(amount):
  transactions.append({'type': 'withdrawal', 'amount': amount})

def view_history():
  for transaction in transactions:
    print(f"{transaction['type'].capitalize()}: {transaction['amount']}")

def check_balance():
  balance = 0
  for transaction in transactions:
    if transaction['type'] == 'deposit':
      balance += transaction['amount']
    else:
      balance -= transaction['amount']
  return balance

# Example usage
deposit(3000)
withdraw(150)
deposit(700)

view_history()
print(f"Current balance: {check_balance()}")