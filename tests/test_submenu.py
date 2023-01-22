import json
from tests import menu_to_dict, submenu_to_dict

from app.v1.crud.submenu import get_submenus

router = '/api/v1/menus/1/submenus/'
router_id = 'api/v1/menus/1/submenus/{id}/'

def test_list_empty_submenu(client):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == []

def test_list_one_submenu(client, submenu_1):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [submenu_to_dict(submenu_1)]

def test_list_two_submenus(client, submenu_1, submenu_2):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [
        submenu_to_dict(submenu_1), submenu_to_dict(submenu_2)
    ]

def test_get_submenu(client, submenu_1):
    resp = client.get(
        router_id.format(id=1)
    )
    assert resp.status_code == 200
    assert resp.json() == submenu_to_dict(submenu_1)

def test_get_submenu_not_found(client):
    resp = client.get(
        router_id.format(id=1)
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}

def test_create_submenu(client, db, menu_1):
    resp = client.post(
        router,
        json={'title': 'My submenu', 'description': 'My submenu description'},
    )
    assert resp.status_code == 201
    assert resp.json() == {
        'title': 'My submenu',
        'description': 'My submenu description',
        'id': '1',
        'dishes_count': 0,
    }
    submenus = get_submenus(db)
    assert len(submenus) == 1

def test_update_submenu(client, db, submenu_1):
    resp = client.patch(
        router_id.format(id=1),
        json={'title': 'My updated submenu', 'description': 'My updated submenu description'},
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'title': 'My updated submenu',
        'description': 'My updated submenu description',
        'id': '1',
        'dishes_count': 0
    }
    submenus = get_submenus(db)
    assert len(submenus) == 1

def test_update_submenu_not_found(client, db):
    resp = client.patch(
        router_id.format(id=1),
        json={'title': 'My updated submenu', 'description': 'My updated submenu description'},
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}
    submenus = get_submenus(db)
    assert len(submenus) == 0

def test_delete_submenu(client, db, submenu_1):
    resp = client.delete(
        router_id.format(id=1)
    )
    assert resp.status_code == 200
    assert resp.json() == {'message': 'The submenu has been deleted'}
    submenus = get_submenus(db)
    assert len(submenus) == 0

def test_delete_submenu_not_found(client):
    resp = client.delete(
        router_id.format(id=1)
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}
