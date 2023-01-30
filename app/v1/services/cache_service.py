import json

from fastapi.encoders import jsonable_encoder


class CacheService():
    def __init__(self, cache):
        self.cache = cache

    def set_all(self, list_name, data):
        data = [value.__dict__ for value in data]
        for value in data:
            value.pop('_sa_instance_state', None)
        data = json.dumps(jsonable_encoder(data))
        return self.cache.set(list_name, data)

    def get(self, name):
        value = self.cache.get(name)
        return json.loads(value) if value else None

    def set(self, name, value):
        value = jsonable_encoder(value)
        return self.cache.set(name, json.dumps(value))

    def delete(self, name):
        keys = self.cache.keys(f'{name}*')
        if keys:
            for key in keys:
                self.cache.delete(key)
