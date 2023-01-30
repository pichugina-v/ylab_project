import json


class CacheService():
    def __init__(self, cache):
        self.cache = cache

    def get(self, url):
        value = self.cache.get(url)
        return json.loads(value) if value else value

    # def getall(self, url):
    #     values = self.cache.keys(f'{url}*')
    #     print('GETALL', [value.decode('utf-8') for value in  values])
    #     return [json.loads(value) if value else value for value in values]

    def set(self, url, value):
        return self.cache.set(url, json.dumps(value))

    def delete(self, url):
        keys = self.cache.keys(f'{url}*')
        if keys:
            for key in keys:
                self.cache.delete(key)

    def delete_menu_cache(self, url):
        url = url.split('/submenus')[0]
        self.cache.delete(url)

    def set_dishes_to_submenu(self, url):
        url = url.split('/dishes')[0]
        try:
            value = json.loads(self.cache.get(url))
            value['dishes_count'] += 1
            self.cache.set(url, json.dumps(value))
        except TypeError:
            pass

    def set_dishes_to_menu(self, url):
        url = url.split('/submenus')[0]
        try:
            value = json.loads(self.cache.get(url))
            value['dishes_count'] += 1
            self.cache.set(url, json.dumps(value))
        except TypeError:
            pass

    def set_submenus_to_menu(self, url):
        url = url.split('/submenus')[0]
        try:
            value = json.loads(self.cache.get(url))
            value['submenus_count'] += 1
            self.cache.set(url, json.dumps(value))
        except TypeError:
            pass
