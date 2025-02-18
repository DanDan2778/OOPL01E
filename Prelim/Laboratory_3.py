# Class for Book
class Book:

# Initialize
    def __init__(self, title, author, year_published, status, code):
    # Place Holder
        self.title = title
        self.author = author
        self.year_published = year_published
        self.status = status
        self.book_code = code
    # change status to borrowed
    def display_book(self):
        print(f'Book Code: {self.book_code}, Title: {self.title}, Author: {self.author}, Year Published: {self.year_published}, Status: {self.status}')

    def borrow_book(self):
        self.status = 'Borrowed'
        print(f'{self.title} is now {self.status}')

    def return_book(self):
        self.status = 'Available'
        print(f'{self.title} is now {self.status}')

# Initialize Objects for Class Book
book1 = Book('Engineering Economics', 'Chan S. Park', 2007, 'Available', 1001)
book2 = Book('Engineering Mechanics', 'Timoshenko', 2008, 'Available', 1002)
book3 = Book('Engineering Mathematics', 'H.C. Taneia', 2010, 'Available', 1003)

# Displaying Initialized Object

def books():
    print('Available Books: ')

    book1.display_book()
    book2.display_book()
    book3.display_book()
while True:
    # Ask User for Input
    print() # whitespace
    print('1. Borrow Book')
    print('2. Return Book')
    print('3. Display All Books')
    print('4. Exit Program!!')
    choose = int(input('What do you want to do: '))

    if choose == 1:
        print() # whitespace
        books()
        print() # whitespace
        choose = int(input('Enter the Book Code to be Borrowed: '))
        if choose == 1001:
            book1.borrow_book()
        elif choose == 1002:
            book2.borrow_book()
        elif choose == 1003:
            book3.borrow_book()
        else:
            print('Invalid Book Code!!')

    elif choose == 2:
        choose = int(input('Enter the Book Code to be Returned: '))
        if choose == 1001:
            book1.return_book()
        elif choose == 1002:
            book2.return_book()
        elif choose == 1003:
            book3.return_book()
        else:
            print('Invalid Book Code!!')


    elif choose == 3:
        print() # whitespace
        books()
    elif choose == 4:
        break
    else:
        print('Invalid Choice!!')

