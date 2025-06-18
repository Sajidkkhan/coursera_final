from behave import given
from service.models import Product
from tests.factories import ProductFactory

@given('the following products exist')
def step_impl(context):
    for row in context.table:
        Product.create(
            name=row['name'],
            category=row['category'],
            price=float(row['price']),
            available=row['available'].lower() == 'true'
        )
