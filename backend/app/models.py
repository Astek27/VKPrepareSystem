from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .enum import CityEnum, CategoryEnum
from .database import Base


class VK(Base):
    __tablename__ = 'VKs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    full_name: Mapped[str]
    adress: Mapped[str]
    city: Mapped[CityEnum] = mapped_column(nullable=False)


class Telephone(Base):
    __tablename__ = 'telephones'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(nullable=False)
    comment: Mapped[str]
    vk_id: Mapped[int] = mapped_column(ForeignKey('VKs.id'), nullable=False)


class Command(Base):
    __tablename__ = 'commands'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str]


class Batch(Base):
    __tablename__ = 'batches'

    id: Mapped[int] = mapped_column(primary_key=True)
    vk_id: Mapped[int] = mapped_column(ForeignKey('VKs.id'), nullable=False)
    category: Mapped[CategoryEnum] = mapped_column(nullable=False)
    oya: Mapped[bool] = mapped_column(nullable=False)
    value: Mapped[int] = mapped_column(nullable=True)
