import json


class CacheService():
    def __init__(self, cache):
        self.cache = cache

    def get(self, url):
        value = self.cache.get(url)
        return json.loads(value) if value else value

    # def getall(self, url):
    #     values = self.cache.keys(f'{url}*')
    #     print("GETALL", values)
    #     return [json.loads(value) for value in values]

    def set(self, url, value):
        return self.cache.set(url, json.dumps(value))

    def delete(self, url):
        keys = self.cache.keys(f'{url}*')
        if keys:
            for key in keys:
                self.cache.delete(key)
