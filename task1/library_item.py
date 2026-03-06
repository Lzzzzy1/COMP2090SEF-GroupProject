from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self._item_id = item_id
        self._is_available = True
        self._borrowed_by = None
        self._due_date = None

    @abstractmethod
    def get_type(self):
        pass

    def borrow(self, member):
        if self._is_available and member.can_borrow():
            self._is_available = False
            self._borrowed_by = member
            self._due_date = datetime.now() + timedelta(days=14)
            member.borrowed_items.append(self)
            return True
        return False

    def return_item(self):
        if not self._is_available:
            self._is_available = True
            fine = self.calculate_fine()
            self._borrowed_by.borrowed_items.remove(self)
            self._borrowed_by = None
            self._due_date = None
            return fine
        return 0

    def calculate_fine(self):
        if self._due_date and datetime.now() > self._due_date:
            days_late = (datetime.now() - self._due_date).days
            return days_late * 2
        return 0

    def get_details(self):
        status = "Available" if self._is_available else f"Borrowed (Due: {self._due_date.strftime('%Y-%m-%d')})"
        return f"{self.get_type()}: {self.title} (ID: {self._item_id}) - {status}"