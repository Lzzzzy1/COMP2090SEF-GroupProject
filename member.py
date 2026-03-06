from abc import ABC, abstractmethod

class Member(ABC):
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_items = []

    @abstractmethod
    def can_borrow(self):
        pass

    def show_borrowed(self):
        if not self.borrowed_items:
            print("   No borrowed items")
            return
        print(f"   {self.name}'s borrowed items ({len(self.borrowed_items)}):")
        for item in self.borrowed_items:
            print(f"     - {item.get_details()}")