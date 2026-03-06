from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, item_id):
        super().__init__(title, item_id)
        self.author = author

    def get_type(self):
        return "Book"

    def get_details(self):
        return super().get_details() + f" Author: {self.author}"