from datetime import datetime
import random 

class Book:

  on_shelf = []
  on_loan = []

  def __init__(self, title, author, ISBN):
    self.title = title
    self.author = author 
    self.ISBN = ISBN

  @classmethod
  def create(cls, title, author, ISBN):
      new_book = Book(title, author, ISBN)
      cls.on_shelf.append(new_book)

  @classmethod
  def browse(cls): 
      browse = random.choice(cls.on_shelf)
      return browse 

  @classmethod
  def current_due_date(cls): 
    now = datetime.now()
    two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
    future_timestamp = now.timestamp() + two_weeks
    return datetime.fromtimestamp(future_timestamp)
      



  def __str__(self):
      return f'Title: {self.title},\nAuthor: {self.author},\nISBN: {self.ISBN}'


  def borrow(self):
    book = Book()
    if self.on_shelf[book] == True: 
     on_loan.append(book)
    return f'{self.title} by {self.author} is now on loan.'

  def return_to_library(self): 
      book = Book()
      if on_loan[book] == True: 
        on_loan.pop(book)
        on_shelf.append(book)
      return f'{self.title} by {self.author} has been returned.'
    


book = Book('I know why the caged bird sings', 'Maya Angelou', 12345678910)
sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue())) # 0
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0
 


