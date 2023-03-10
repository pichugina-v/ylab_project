from pytest import mark

from tests import menu_to_dict

router = '/api/v1/menus'
router_id = 'api/v1/menus/{id}'


@mark.asyncio
async def test_list_empty_menu(client, cache):
    resp = await client.get(router)
    assert resp.status_code == 200
    assert resp.json() == []


@mark.asyncio
async def test_list_menu(client, menu_1, cache):
    resp = await client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [menu_to_dict(menu_1)]


@mark.asyncio
async def test_get_menu_not_found(client, cache):
    resp = await client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'menu not found'}


@mark.asyncio
async def test_get_menu(client, menu_1, cache):
    resp = await client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == menu_to_dict(menu_1)


@mark.asyncio
async def test_create_menu(client, db, cache):
    resp = await client.post(
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


@mark.asyncio
async def test_update_menu(client, db, menu_1, cache):
    resp = await client.patch(
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


@mark.asyncio
async def test_update_menu_not_found(client, db, cache):
    resp = await client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated menu',
            'description': 'My updated menu description',
        },
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'menu not found'}


@mark.asyncio
async def test_delete_menu(client, db, menu_1, cache):
    resp = await client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'status': 'true',
        'message': 'The menu has been deleted',
    }


@mark.asyncio
async def test_delete_menu_not_found(client, cache):
    resp = await client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'menu not found'}
