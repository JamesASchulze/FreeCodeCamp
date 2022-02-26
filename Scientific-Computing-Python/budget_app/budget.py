class Category:
  def __init__(self, title):
    self.title = title
    self.ledger = []
    self.balance = 0

  # deposit
  def deposit(self,amount,description=""):
    self.ledger.append([amount,description])
    self.balance += amount
    # print("amount: {}, description: {}".format(amount,description))
    # print(self.balance)
    # print(self.ledger)

  # withdraw
  def withdraw(self,amount,description=""):
    is_enough_funds = self.check_funds(amount)
    if is_enough_funds == True:
      self.balance -= amount
      negative_amount = amount - amount * 2
      self.ledger.append([negative_amount,description])
      return True
    else:
      return False
    
  # get_balance
  def get_balance(self):
    return self.balance
    
  # transfer
  def transfer(self,amount,other_category):
    is_enough_funds = self.check_funds(amount)
    if is_enough_funds == True:
      self.withdraw(amount, "Transfer to {}".format(other_category.title))
      other_category.deposit(amount, "Transfer from {}".format(self.title))
      return True
    else:
      return False
  
  # check_funds
  def check_funds(self,amount):
    if amount <= self.balance:
      return True
    else:
      return False
    
  # print out object
  def __repr__(self):
    
    # Header
    res = self.title.center(30,"*") + "\n"

    # Ledger
    for entry in self.ledger:
      amount  = float(str(entry[0])[:7])
      desc    = entry[1][:23]

      res += "{:<23}{:>7.2f}\n".format(desc,amount)

    # Total
    res += "Total: {}".format(self.balance)
    # print(res)
      
    return res
    # return "Print: {}".format(self.title)


def create_spend_chart(categories):
  return "Bar chart goes here...."