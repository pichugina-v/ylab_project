from sqlalchemy import Column, ForeignKey, Integer, String, select, func
from sqlalchemy.orm import relationship, column_property

from db.sqlalchemy_base import Base


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), unique=True)
    description = Column(String(1000))
    submenu_id = Column(ForeignKey('submenus.id', ondelete='CASCADE'), nullable=False)
    submenus = relationship('Submenu', back_populates='dishes')
    price = Column(String(50))


class Submenu(Base):
    __tablename__ = 'submenus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), unique=True)
    description = Column(String(1000))
    menu_id = Column(ForeignKey('menus.id', ondelete='CASCADE'), nullable=False)
    menu = relationship('Menu', back_populates='submenus')
    dishes = relationship(
        'Dish', back_populates='submenus',
        cascade='all, delete', passive_deletes=True
    )


class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), unique=True)
    description = Column(String(1000))
    submenus = relationship(
        'Submenu', back_populates='menu',
        cascade='all, delete', passive_deletes=True
    )
    # count = select(func.count(Submenu.id)).where(Submenu.menu_id == id).correlate_except(Submenu).scalar_subquery()
    submenus_count = column_property(
        select(func.count(Submenu.id))
        .where(Submenu.menu_id == id)
        .correlate_except(Submenu)
        .scalar_subquery()
    )

# inspect(Menu).add_property(
#     column_property(
#         select(func.count(Address.id))
#         .where(Address.user_id == User.id)
#         .scalar_subquery()
#     )
# )