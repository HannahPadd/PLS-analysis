class Book:
    def __init__(self, author, title, book_id):
        self.author = author
        self.title = title
        self.book_id = book_id
        self.available = True

    def __str__(self):
        return 'Book({}, {}, {})'.format(self.author, self.title, self.book_id)

    def return_book(self):
        self.available = True
        return "je hebt het boek ingelevert"

    def loan_book(self):
        self.available = False
        return "je bent het boek nu aan het lenen"
    
    
