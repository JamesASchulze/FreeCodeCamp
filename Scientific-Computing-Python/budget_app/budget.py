class Category:
  def __init__(self, title):
    self.title = title

  # deposit
  def deposit(amount=0,description=""):
    print("amount: {}, description: {}".format(amount,description))

  # withdraw

  # get_balance

  # transfer
  
  # check_funds

  # print out object
  def __repr__(self):
    return "Print: {}".format(self.title)


def create_spend_chart(categories):
  return "Bar chart goes here...."