class Category:
  def __init__(self, title):
    self.title = title
    self.ledger = []
    self.balance = 0
    self.total_debts = 0

  # deposit
  def deposit(self,amount,description=""):
    self.ledger.append({"amount":amount,"description":description})
    self.balance += amount

  # withdraw
  def withdraw(self,amount,description=""):
    is_enough_funds = self.check_funds(amount)
    if is_enough_funds == True:
      self.balance -= amount
      self.total_debts += amount
      negative_amount = amount - amount * 2
      self.ledger.append({"amount":negative_amount,"description":description})
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
      print(entry["amount"])
      amount  = float(str(entry["amount"])[:7])
      desc    = entry["description"][:23]

      res += "{:<23}{:>7.2f}\n".format(desc,amount)
      
    # Total
    res += "Total: {}".format(self.balance)
    # print(res)
      
    return res
    # return "Print: {}".format(self.title)


def create_spend_chart(categories):
  # Copy the categories & total debts from all of the categories.
  data = []
  longest_title_len = 0 
  total_debts = 0

  for category in categories:
    title = category.title
    if len(title) > longest_title_len:
      longest_title_len = len(title)
    data.append(category)
    total_debts += category.total_debts

  # function to find the percentage spent for each category.
  def get_percentage_spent(total_debts,category_debts):
    return (category_debts / total_debts) * 100
     
  # Header
  res = "Percentage spent by category\n"

  # Percentage Spent Chart
  i = 100
  while i >= 0:
    res += "{:>3}|".format(i)

    for category in data:
      category_debts = category.total_debts
      percentage_spent = get_percentage_spent(total_debts,category_debts)
      if percentage_spent >= i:
        res += " o "
      else:
        res += "   "
    
    res += " \n"
    i -= 10
    
  # dashed line
  res += "    "
  for category in categories:
    res += "---"
  res += "-\n"

  # Category names  
  row = 0
  while row < longest_title_len:
    res += "    "
    for category in data: 
      if len(category.title) < longest_title_len:
        category.title += " "
      cat_title = category.title[row]
      res += " {} ".format(cat_title)
    if not row == longest_title_len - 1:
      res += " \n"
    else:  
      res += " "
      
    row += 1
      
  return res