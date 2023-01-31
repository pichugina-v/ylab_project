from tests import submenu_to_dict

router = '/api/v1/menus/1/submenus/'
router_id = 'api/v1/menus/1/submenus/{id}/'


def test_list_empty_submenu(client, cache):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == []


def test_list_submenu(client, submenu_1, cache):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [submenu_to_dict(submenu_1)]


def test_get_submenu_not_found(client, cache):
    resp = client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}


def test_get_submenu(client, submenu_1, cache):
    resp = client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == submenu_to_dict(submenu_1)


def test_create_submenu(client, db, menu_1, cache):
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


def test_update_submenu(client, db, submenu_1, cache):
    resp = client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated submenu',
            'description': 'My updated submenu description',
        },
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'title': 'My updated submenu',
        'description': 'My updated submenu description',
        'id': '1',
        'dishes_count': 0,
    }


def test_update_submenu_not_found(client, db, cache):
    resp = client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated submenu',
            'description': 'My updated submenu description',
        },
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}


def test_delete_submenu(client, db, submenu_1, cache):
    resp = client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'status': 'true',
        'message': 'The menu has been deleted',
    }


def test_delete_submenu_not_found(client, cache):
    resp = client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}
