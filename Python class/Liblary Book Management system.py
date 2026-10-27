class Book:

  def __init__(self, title, author, price, copies):
    self.title = title
    self.author = author
    self.price = price
    self.copies = copies

  def calculate_stock_value(self):
    return self.price * self.copies

  def check_stock(self):
    if self.copies > 0:
      return "In Stock"
    else:
      return "Out of Stock"


# Create two objects using the provided table data
book1 = Book("Python Basics", "John Okelo", 1200, 400)
book2 = Book("Data Structures and Algorithms", "Caroline Mueni", 3200, 20)

# Display Book 1 details
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Stock Value: KSh {book1.calculate_stock_value():,}")
print(f"Status: {book1.check_stock()}\n")

# Display Book 2 details
print(f"Book 2: {book2.title} by {book2.author}")
print(f"Stock Value: KSh {book2.calculate_stock_value():,}")
print(f"Status: {book2.check_stock()}")
