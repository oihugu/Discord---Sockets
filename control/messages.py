from datetime import datetime

class Messages():
    
    def __init__(self, user, text) -> None:
        self.user = user
        self.text = text
        
        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")

    def __str__(self) -> str:
        return f"({self.user.name}, {self.time}) {self.text}"