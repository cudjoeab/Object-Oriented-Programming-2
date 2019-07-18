from datetime import datetime

class Book:

  on_shelf = []
  on_loan = []

  def __init__(self, title, author, ISBN):
    self.title = title
    self.author = author 
    self.ISBN = ISBN

  @classmethod
  def create(cls):
      new_book = Book()
      cls.on_shelf.append(new_book)

  @classmethod
  def check_out_time(cls):
      now = datetime.now()
      now.timestamp()
      return now 

  @classmethod
  def due_date(cls): 
      one_week = 
      



  def __str__(self):
      return f'Title: {self.title},\nAuthor: {self.author},\nISBN: {self.ISBN}'


  def borrow(self):
    book = Book()
    if on_shelf[book] == True: 
     on_loan.append(book)
    return f'{self.title} by {self.author} is now on loan.'

  def return_to_library(self): 
      book = Book()
      if on_loan[book] == True: 
        on_loan.pop(book)
        on_shelf.append(book)
      return f'{self.title} by {self.author} has been returned.'
    


book = Book('I know why the caged bird sings', 'Maya Angelou', 12345678910)
print(book)
 


