class User():

    def __init__(self, name, id, ip, type) -> None:
        self.name = name
        self.id = id
        self.ip = ip
        self.type = type
        
    def __str__(self) -> str:
        return f"{self.name} ({self.id})"


    