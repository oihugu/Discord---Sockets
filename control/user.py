class User():

    def __init__(self, name, id, ip) -> None:
        self.name = name
        self.id = id
        self.ip = ip

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"


    