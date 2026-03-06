from book import Book
from magazine import Magazine
from member import Member
from library_item import LibraryItem
from datetime import datetime

library_items = []
members = {}
transaction_log = []

def register_member():
    name = input("Name: ")
    mtype = input("Type (1=Student 2=Teacher): ")
    mid = f"M{len(members)+1:03d}"
    if mtype == "1":
        class Student(Member):
            def can_borrow(self): return len(self.borrowed_items) < 5
        member = Student(name, mid)
    else:
        class Teacher(Member):
            def can_borrow(self): return len(self.borrowed_items) < 10
        member = Teacher(name, mid)
    members[mid] = member
    print(f"Registration successful! Member ID: {mid}")

def add_item():
    itype = input("Type (1=Book 2=Magazine): ")
    title = input("Title: ")
    iid = f"B{len(library_items)+1:04d}"
    if itype == "1":
        author = input("Author: ")
        item = Book(title, author, iid)
    else:
        issue = input("Issue: ")
        item = Magazine(title, issue, iid)
    library_items.append(item)
    print("Item added successfully!")

def borrow_item():
    mid = input("Your Member ID: ")
    if mid not in members:
        print("Member not found!")
        return
    member = members[mid]
    print("\nAvailable items:")
    available = [item for item in library_items if item._is_available]
    for i, item in enumerate(available, 1):
        print(f"{i}. {item.get_details()}")
    if not available:
        print("No items available")
        return
    choice = int(input("\nEnter number to borrow: ")) - 1
    if 0 <= choice < len(available):
        if available[choice].borrow(member):
            transaction_log.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} {member.name} borrowed {available[choice].title}")
            print("Borrow successful!")
        else:
            print("Cannot borrow (limit reached)")

def return_item():
    mid = input("Your Member ID: ")
    if mid not in members:
        print("Member not found!")
        return
    member = members[mid]
    member.show_borrowed()
    if not member.borrowed_items:
        return
    choice = int(input("\nEnter number to return: ")) - 1
    if 0 <= choice < len(member.borrowed_items):
        fine = member.borrowed_items[choice].return_item()
        transaction_log.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} {member.name} returned item (Fine: HK${fine})")
        print(f"Return successful! Fine: HK${fine}")

def search():
    keyword = input("Search title or author: ").lower()
    print("\nSearch results:")
    found = False
    for item in library_items:
        if keyword in item.title.lower() or (hasattr(item, 'author') and keyword in getattr(item, 'author', '').lower()):
            print(item.get_details())
            found = True
    if not found:
        print("No results")

def show_stats():
    print(f"\nSystem Statistics")
    print(f"Total items: {len(library_items)}")
    print(f"Total members: {len(members)}")
    borrowed = sum(1 for item in library_items if not item._is_available)
    print(f"Currently borrowed: {borrowed}")
    print(f"Today transactions: {len(transaction_log)}")
    for log in transaction_log[-5:]:
        print(f"   {log}")

def main():
    print("Welcome to HKMU MetroLib Library System!\n")
    while True:
        print("\n=== Main Menu ===")
        print("1. Register new member")
        print("2. Add new item (book/magazine)")
        print("3. Borrow item")
        print("4. Return item")
        print("5. Search item")
        print("6. Show my borrowed items")
        print("7. Show system statistics")
        print("8. Exit")
        choice = input("\nEnter option (1-8): ").strip()
        if choice == "1": register_member()
        elif choice == "2": add_item()
        elif choice == "3": borrow_item()
        elif choice == "4": return_item()
        elif choice == "5": search()
        elif choice == "6":
            mid = input("Your Member ID: ")
            if mid in members:
                members[mid].show_borrowed()
            else:
                print("Member not found")
        elif choice == "7": show_stats()
        elif choice == "8":
            print("Thank you for using HKMU MetroLib! Goodbye.")
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
