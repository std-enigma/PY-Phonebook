class Contact:
    def __init__(self, name: str, phone_number: str, email: str) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
        }

    def __str__(self) -> str:
        return f"{self.name} - {self.email}: {self.phone_number}"

    @classmethod
    def from_dict(cls, data) -> Contact:
        return cls(**data)
