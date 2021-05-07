from notebook import Notebook
import sys

class Menu:
    """Display a menu and respond to user's choices."""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            """
Notebook Menu

1) Show all Notes
2) Search Notes
3) Add Note
4) Modify Note
5) Quit
        """
        )

    def run(self):
        """Display the menu and responde to choices."""
        while 1:
            self.display_menu()
            choice = input("Type your choice: ")
            accion = self.choices.get(choice)
            if accion:
                accion()
            else:
                raise ValueError(f"\a'{choice}' isn't a valid option!")

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.memo}\n{note.tags}")

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added!")

    def modify_note(self):
        id = input("Enter a id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Bye")
        sys.exit(0)
        
def main():
    app = Menu()
    app.run()

if __name__ == '__main__':
    main()
    