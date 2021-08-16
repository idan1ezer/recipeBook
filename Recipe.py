import requests as req

class Recipe:
    def __init__(self, name, plates, ingredients, method, photo_url):
        self.name = name
        self.plates = plates
        self.ingredients = ingredients
        self.method = method
        self.photo_url = photo_url