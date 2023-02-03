import json

from fastapi.encoders import jsonable_encoder


class CacheService():
    def __init__(self, cache):
        self.cache = cache

    async def set_all(self, list_name, data):
        data = [value.__dict__ for value in data]
        for value in data:
            value.pop('_sa_instance_state', None)
        data = json.dumps(jsonable_encoder(data))
        return await self.cache.set(list_name, data)

    async def get(self, name):
        value = await self.cache.get(name)
        return json.loads(value) if value else None

    async def set(self, name, value):
        value = jsonable_encoder(value)
        return await self.cache.set(name, json.dumps(value))

    async def delete(self, name):
        return await self.cache.delete(name)
