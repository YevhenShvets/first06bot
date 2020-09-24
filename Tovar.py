class Tovar:
    id: int
    name: str
    category: str
    category_id: str
    price: int
    def __init__(self, id, name, category, category_id, price):
        self.id = id
        self.name = name
        self.category = category
        self.category_id = category_id
        self.price = price

    def get_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'category_id': self.category_id,
            'price': self.price
        }


