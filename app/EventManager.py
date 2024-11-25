from enum import Enum
from queue import Queue

class Events(Enum):
    COLLISSION = "COLLISION"
    DEATH = "DEATH"
    pass

class EventManager:
    def __init__(self):
        self.events = Queue()

    def add_event(self, event_type, source, **kwargs):
        """Fügt ein neues Event zur Warteschlange hinzu."""
        event = {"type": event_type, "source": source, **kwargs}
        self.events.put(event)

    def get_next_event(self):
        """Holt das nächste Event aus der Warteschlange."""
        if not self.events.empty():
            return self.events.get()
        return None