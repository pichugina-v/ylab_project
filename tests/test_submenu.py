from pytest import mark

from tests import submenu_to_dict

router = '/api/v1/menus/1/submenus'
router_id = 'api/v1/menus/1/submenus/{id}'


@mark.asyncio
async def test_list_empty_submenu(client, cache):
    resp = await client.get(router)
    assert resp.status_code == 200
    assert resp.json() == []


@mark.asyncio
async def test_list_submenu(client, submenu_1, cache):
    resp = await client.get(router)
    assert resp.status_code == 200
    assert resp.json() == [submenu_to_dict(submenu_1)]


@mark.asyncio
async def test_get_submenu_not_found(client, cache):
    resp = await client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}


@mark.asyncio
async def test_get_submenu(client, submenu_1, cache):
    resp = await client.get(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == submenu_to_dict(submenu_1)


@mark.asyncio
async def test_create_submenu(client, db, menu_1, cache):
    resp = await client.post(
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


@mark.asyncio
async def test_update_submenu(client, db, submenu_1, cache):
    resp = await client.patch(
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


@mark.asyncio
async def test_update_submenu_not_found(client, db, cache):
    resp = await client.patch(
        router_id.format(id=1),
        json={
            'title': 'My updated submenu',
            'description': 'My updated submenu description',
        },
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}


@mark.asyncio
async def test_delete_submenu(client, db, submenu_1, cache):
    resp = await client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 200
    assert resp.json() == {
        'status': 'true',
        'message': 'The menu has been deleted',
    }


@mark.asyncio
async def test_delete_submenu_not_found(client, cache):
    resp = await client.delete(
        router_id.format(id=1),
    )
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'submenu not found'}
