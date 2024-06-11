class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transaction = []

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)
    self.previous_transaction.append([item, price, quantity])
      
  def apply_discount(self):
    if self.discount: 
      self.total = int(self.total * ((100-self.discount)/100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.previous_transaction:
      return "There are no transactions to void"
    last_transaction = self.previous_transaction.pop()
    self.total -= last_transaction[1] * last_transaction[2]
    for _ in range(last_transaction[2]):
      self.items.pop()