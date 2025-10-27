from faker import Faker
import random
from .models import Product, Category

fake = Faker()

def run():

    category_name =['Ноутбук', 'Смартфоны', 'Периферия', 'Аксессуары', 'Наушники']
    categories= []
    for name in category_name:
        cat, created = Category.objects.get_or_create(name=name)
        categories.append(cat)

    for _ in range(40):
        cat = random.choice(categories)
        Product.objects.create(
            name = fake.word().capitalize() + ' ' + cat.name,
            description = fake.sentence(nb_words=8),
            price = round(random.uniform(100, 2000), 2),
            in_stock = random.choice([True, False]),
            category = cat
        )
    print('Данные успешно созданы')