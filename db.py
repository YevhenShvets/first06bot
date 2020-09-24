from Tovar import Tovar
data = []

data.append(Tovar(id=1, name='Яблука', category='Фрукти', category_id=1, price=8).get_dict())
data.append(Tovar(id=2, name='Дуб', category='Дерева', category_id=2, price=200).get_dict())
data.append(Tovar(id=3, name='Груші', category='Фрукти', category_id=1, price=12).get_dict())
data.append(Tovar(id=4, name='Помідори', category='Овочі', category_id=3, price=22).get_dict())
data.append(Tovar(id=5, name='Баклажани', category='Овочі', category_id=3, price=50).get_dict())
data.append(Tovar(id=6, name='Черешні', category='Фрукти', category_id=1, price=25).get_dict())
data.append(Tovar(id=7, name='Огірки', category='Овочі', category_id=3, price=24).get_dict())
data.append(Tovar(id=8, name='Айстри', category='Квіти', category_id=4, price=80).get_dict())
data.append(Tovar(id=9, name='Нарциси', category='Квіти', category_id=4, price=85).get_dict())
data.append(Tovar(id=10, name='Лимони', category='Фрукти', category_id=1, price=40).get_dict())
data.append(Tovar(id=11, name='Картопля', category='Овочі', category_id=3, price=8).get_dict())
data.append(Tovar(id=12, name='Рози', category='Квіти', category_id=4, price=200).get_dict())
data.append(Tovar(id=13, name='Яблуня', category='Дерева', category_id=2, price=500).get_dict())
data.append(Tovar(id=14, name='Черешня', category='Дерева', category_id=2, price=550).get_dict())


def output(t):
    return str(f"Назва товару: *{t['name']}*;\nКатегорія: _{t['category']}_;\nЦіна товару: *{t['price']}* грн;")

def get_categories():
    rez = []
    for i in tuple(data):
        if (i['category_id'], i['category']) not in rez:
            rez.append((
                i['category_id'],
                i['category']
            ))
            yield rez[-1]


def get_tovar(id):
    for i in tuple(data):
        if i['category_id'] == id:
            yield i



