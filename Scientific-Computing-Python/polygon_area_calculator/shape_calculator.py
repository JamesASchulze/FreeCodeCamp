class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width >= 50 or self.height >= 50:
      return "Too big for picture."
      
    picture = ""
    row = 0
    print("height: {}".format(self.height))
    print("width: {}".format(self.width))
    while row < self.height:
      col = 0
      while col < self.width:
        picture += "*"
        col += 1

      picture += "\n"
      row += 1

    return picture

  def get_amount_inside(self,sq):
    res = 0

    if sq.height > self.height or sq.width > self.width:
      return 0

    row = 0  
    while row <= self.height:

      res += self.width // sq.width
      row += sq.height
    
    return res
    
  # print out object
  def __repr__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)
    
class Square(Rectangle):
  def __init__(self,side):
    self.width = side
    self.height = side
    
  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height

  # print out object
  def __repr__(self):
    return "Square(side={})".format(self.width)
    