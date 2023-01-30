from tests import menu_to_dict

router = '/api/v1/menus/'
router_id = 'api/v1/menus/{id}/'


def test_list_empty_menu(client):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == []


def test_list_one_menu(client, menu_1):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [menu_to_dict(menu_1)]


def test_list_two_menus(client, menu_1, menu_2):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [menu_to_dict(menu_1), menu_to_dict(menu_2)]


def test_get_menu_not_found(client):
    resp = client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'menu not found'}


def test_get_menu(client, menu_1):
    resp = client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == menu_to_dict(menu_1)


def test_create_menu(client, db):
    resp = client.post(
        router,
        json={'title': 'My menu', 'description': 'My menu description'},
    )
    assert resp.status_code == 201
    assert resp.json() == {
        'title': 'My menu',
        'description': 'My menu description',
        'id': '1',
        'submenus_count': 0,
        'dishes_count': 0,
    }


def test_update_menu(client, db, menu_1):
    resp = client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated menu',
            'description': 'My updated menu description',
        },
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'title': 'My updated menu',
        'description': 'My updated menu description',
        'id': '1',
        'submenus_count': 0,
        'dishes_count': 0,
    }


def test_update_menu_not_found(client, db):
    resp = client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated menu',
            'description': 'My updated menu description',
        },
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'menu not found'}


def test_delete_menu(client, db, menu_1):
    resp = client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'status': 'true',
        'message': 'The menu has been deleted',
    }


def test_delete_menu_not_found(client):
    resp = client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'menu not found'}
