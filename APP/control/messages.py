from datetime import datetime

class Messages():
    
    def __init__(self, author, content, time=None) -> None:
        self.author = author
        self.content = content
        self.time = time
        if time is None:
            now = datetime.now()
            self.time = now.strftime("%H:%M:%S")

    def __str__(self) -> str:
        return f"({str(self.author)}, {self.time}) {self.content}"