from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, issue, item_id):
        super().__init__(title, item_id)
        self.issue = issue

    def get_type(self):
        return "Magazine"

    def get_details(self):
        return super().get_details() + f" Issue: {self.issue}"