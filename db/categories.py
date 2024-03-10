from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import BaseModel


class Category(BaseModel):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))

    item_rel: Mapped[List['Item']] = relationship(back_populates='category_rel')
