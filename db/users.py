from typing import List

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

    cart_rel: Mapped[List['Cart']] = relationship('user_rel')
