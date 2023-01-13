from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.sqlalchemy_base import db


class Menu(db):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), unique=True)
    description = Column(String(1000))
    submenus = relationship(
        'Submenu', back_populates='menu',
        cascade='all, delete', passive_deletes=True
    )


class Submenu(db):
    __tablename__ = 'submenus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), unique=True)
    description = Column(String(1000))
    menu_id = Column(ForeignKey('menus.id', ondelete='CASCADE'), nullable=False)
    menu = relationship('Menu', back_populates='submenu')
    dishes = relationship(
        'Dish', back_populates='submenu',
        cascade='all, delete', passive_deletes=True
    )


class Dish(db):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), unique=True)
    description = Column(String(1000))
    submenu_id = Column(ForeignKey('submenus.id', ondelete='CASCADE'), nullable=False)
    submenus = relationship('Submenu', back_populates='dish')
    price = Column(String(50))
