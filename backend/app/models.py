from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .enum import CityEnum, CategoryEnum
from .database import Base


class VK(Base):
    __tablename__ = 'VKs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    full_name: Mapped[str]
    adress: Mapped[str]
    city: Mapped[CityEnum] = mapped_column(nullable=False)

    batch = relationship('Batch', back_populates='vk')
    telephone = relationship('Telephone', back_populates='vk')

class Telephone(Base):
    __tablename__ = 'telephones'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(nullable=False)
    comment: Mapped[str]

    vk_id: Mapped[int] = mapped_column(ForeignKey('VKs.id'), nullable=False)

    vk = relationship('VK', back_populates='telephone')

class Command(Base):
    __tablename__ = 'commands'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str]

    batch = relationship('Batch', 'command')


class Batch(Base):
    __tablename__ = 'batches'

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[CategoryEnum] = mapped_column(nullable=False)
    osn: Mapped[bool] = mapped_column(nullable=False)
    value_osn: Mapped[int]
    value_perem: Mapped[int]

    vk_id: Mapped[int] = mapped_column(ForeignKey('VKs.id'), nullable=False)
    command_id: Mapped[int] = mapped_column(ForeignKey('commands.id'), nullable=False)

    vk = relationship('VK', back_populates='batch')
    command = relationship('Command', back_populates='batch')