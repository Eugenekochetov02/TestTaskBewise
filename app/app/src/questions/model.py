from sqlalchemy.orm import Mapped, mapped_column

from db import Base


# Create model
class Question(Base):
    __tablename__ = "question"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    text: Mapped[str]
    value: Mapped[int] = mapped_column(nullable=True)
    created_at: Mapped[int] = mapped_column(nullable=False)
    updated_at: Mapped[int] = mapped_column(nullable=False)
