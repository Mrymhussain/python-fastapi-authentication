from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class TeaModel(BaseModel):
    __tablename__ = "teas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    in_stock = Column(Boolean)
    rating = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("UserModel", back_populates="teas")
    comments = relationship("CommentModel", back_populates="tea")

    def __str__(self):
        return f"{self.id}: {self.name}"