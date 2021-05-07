import datetime

# Store the next available id for all new notes. 
last_id: int = 0


class Note:
    """Represent a note in the notebook.
    """
    def __init__(self, memo, tags = ""):
        """Initialize a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
        
    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags."""
        return filter in self.memo or filter in self.tags
    

class Notebook:
    """A collection of notes that can be searched, modified, and tagged.
    """
    
    def __init__(self):
        """Creates our list of notes.
        """
        self.notes:list = []
    
    def _find_note(self, note_id: int):
        """Locate the given id.

        Args:
            note_id (int): The id to search throught the list.

        Returns:
            Note: If the id was found.
            None: If couldn't find the id.
        """
        for note in self.notes:
            return note if str(note.id) == str(note_id) else None

    def new_note(self, memo:str, tags = ""):
        """Add a new note to our list of notes.

        Args:
            memo (str): Te memo to be saved.
            tags (str, optional): An optional tag. Defaults to "".
        """
        self.notes.append(Note(memo, tags))
        
    def modify_memo(self, note_id: str, memo: int):
        """Modify a memo with a given id.

        Args:
            note_id (int): The note's id.
            memo (str): The new memo.
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
            
    def modify_tags(self, note_id: int, tags: str):
        """Will search till meet the given note_id to make de modification.

        Args:
            note_id (int): The id to search.
            tags (str): The new tag to replace.
        """
        self._find_note(note_id).tags = tags
        
    def search(self, filter: str):
        """Return all notes that match with the given filter.

        Args:
            filter (str): The filter to match.

        Returns:
            list: The list with matched notes.
        """
        return [note for note in self.notes if note.match(filter)]