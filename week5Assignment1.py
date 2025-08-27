# Assignment 1: Designing my Own Class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages  

    def read(self):
        return f"Reading '{self.title}' by {self.author}"

    def get_pages(self):       
        return f"This book has {self.__pages} pages."


class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def read(self):   
        return f"Reading '{self.title}' on a Kindle (size {self.file_size}MB)."


paper_book = Book("Pride and Prejudice", "Jane Austen", 500)
ebook = EBook("Harry Potter", "J.K", 4100, 5)

print(paper_book.read())     
print(paper_book.get_pages()) 
print(ebook.read())      
