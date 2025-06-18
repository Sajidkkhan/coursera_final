import factory
from faker import Faker
from service.models import Product

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n + 1)
    name = factory.LazyAttribute(lambda x: fake.unique.word())
    category = factory.LazyAttribute(lambda x: fake.random_element(elements=['Electronics', 'Books', 'Clothing', 'Toys']))
    price = factory.LazyAttribute(lambda x: round(fake.random_number(digits=3), 2))
    available = factory.LazyAttribute(lambda x: fake.boolean())
