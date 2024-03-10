from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import BaseModel


class Item(BaseModel):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(300))
    photo: Mapped[str] = mapped_column(String(200))
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    category_rel: Mapped['Category'] = relationship(back_populates='item_rel')
    cart_rel: Mapped[List['Cart']] = relationship('item_rel')
