class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return (self.title, self.author, self.pages)
    def len(self):
        return self.pages

if __name__ == "__main__":
    book = Book("파이썬", "코딩하는형", 874)
    print(book.__str__())
    print(book.len())