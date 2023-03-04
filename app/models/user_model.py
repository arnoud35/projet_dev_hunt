from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field, EmailStr
from typing import Optional

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    matricule: Indexed(str, unique=True)
    email: Optional[Indexed(EmailStr, unique=True)]
    role: float
    hashed_password: str
    first_name: str
    last_name: str

    def __repr__(self) -> str:
        return f"<User {self.matricule}>"

    def __str__(self) -> str:
        return self.matricule

    def __hash__(self) -> int:
        return hash(self.matricule)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.matricule == other.matricule
        return False

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_matricule(self, matricule: str) -> "User":
        return await self.find_one(self.matricule == matricule)

    class Collection:
        name = "users"                            