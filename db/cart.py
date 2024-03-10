from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import BaseModel


class Cart(BaseModel):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    item: Mapped[int] = mapped_column(ForeignKey('items.id'))

    user_rel: Mapped['User'] = relationship(back_populates='cart_rel')
    item_rel: Mapped['Item'] = relationship(back_populates='cart_rel')
