from datetime import datetime

class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("\nEnter your journal entry:\n")
        
        if entry == "":
            print("\nError: Journal entry cannot be empty.")
            return

        with open(self.filename, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write("[" + timestamp + "]\n")
            file.write(entry + "\n")
            
        print("\nEntry added successfully!")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                
            if content == "":
                print("\nNo journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print(content)
                
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

    def search_entry(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
            
            if content.strip() == "":
                print("\nError: The journal file is empty. Please add a new entry first.")
                return

            keyword = input("\nEnter a keyword or date to search: ")
            
            if keyword == "":
                print("\nError: Search keyword cannot be empty.")
                return

            print("\nMatching Entries:")
            found = False
            
            with open(self.filename, "r") as file:
                while True:
                    timestamp_line = file.readline()
                    if not timestamp_line:
                        break
                        
                    entry_line = file.readline()
                    if not entry_line:
                        break
                    
                    if keyword in timestamp_line or keyword in entry_line:
                        print(timestamp_line, end="")
                        print(entry_line, end="")
                        found = True

            if not found:
                print("No entries were found for the keyword: " + keyword + ".")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

    def delete_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                
            if content.strip() == "":
                print("\nNo journal entries to delete.")
                return
            
            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")
            
            if confirm == "yes":
                with open(self.filename, "w") as file:
                    pass 
                print("All journal entries have been deleted.")
            else:
                print("Deletion cancelled.")
                
        except FileNotFoundError:
            print("\nNo journal entries to delete.")

journal = JournalManager()

print("Welcome Menu:")
print("Welcome to Personal Journal Manager!")

while True:
    print("\nPlease select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nUser Input:\n")

    match choice:
        case "1":
            journal.add_entry()
        case "2":
            journal.view_entries()
        case "3":
            journal.search_entry()
        case "4":
            journal.delete_entries()
        case "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("\nInvalid option. Please select a valid option from the menu.")
