from tests import dish_to_dict

router = '/api/v1/menus/1/submenus/1/dishes'
router_id = 'api/v1/menus/1/submenus/1/dishes/{id}/'


def test_list_empty_dish(client, cache):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == []


def test_list_dish(client, dish_1, cache):
    resp = client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [dish_to_dict(dish_1)]


def test_get_dish_not_found(client, cache):
    resp = client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'dish not found'}


def test_get_dish(client, dish_1, cache):
    resp = client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == dish_to_dict(dish_1)


def test_create_dish(client, db, submenu_1, cache):
    resp = client.post(
        router,
        json={
            'title': 'My dish',
            'description': 'My dish description',
            'price': '12.50',
        },
    )
    assert resp.status_code == 201
    assert resp.json() == {
        'title': 'My dish',
        'description': 'My dish description',
        'id': '1',
        'price': '12.50',
    }


def test_update_dish(client, db, dish_1, cache):
    resp = client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated dish',
            'description': 'My updated dish description',
            'price': '14.50',
        },
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'title': 'My updated dish',
        'description': 'My updated dish description',
        'id': '1',
        'price': '14.50',
    }


def test_update_dish_not_found(client, db, cache):
    resp = client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated dish',
            'description': 'My updated dish description',
            'price': '12.50',
        },
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'dish not found'}


def test_delete_dish(client, db, dish_1, cache):
    resp = client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'status': 'true',
        'message': 'The menu has been deleted',
    }


def test_delete_dish_not_found(client, cache):
    resp = client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'dish not found'}
