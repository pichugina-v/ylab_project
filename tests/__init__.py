from app.v1.models.models import Dish, Menu, Submenu

def menu_to_dict(menu: Menu):
    return {
        'id': str(menu.id),
        'title': str(menu.title),
        'description': str(menu.description),
        'submenus_count': menu.submenus_count,
        'dishes_count': menu.dishes_count
    }

def submenu_to_dict(submenu: Submenu):
    return {
        'id': str(submenu.id),
        'title': str(submenu.title),
        'description': str(submenu.description),
        'dishes_count': submenu.dishes_count
    }

def dish_to_dict(dish: Dish):
    return {
        'id': str(dish.id),
        'title': str(dish.title),
        'description': str(dish.description),
        'price': str(dish.price)
    }
