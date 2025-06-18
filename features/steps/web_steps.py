from behave import given, when, then
from service.models import Product
from service import app
import json

@given('a product exists with id {product_id}')
def step_impl(context, product_id):
    context.product = Product.find_by_id(int(product_id))
    assert context.product is not None

@when('I request the product with id {product_id}')
def step_impl(context, product_id):
    client = app.test_client()
    response = client.get(f'/products/{product_id}')
    context.response = response

@when('I update the product with id {product_id} with new data')
def step_impl(context, product_id):
    client = app.test_client()
    data = {"name": "Updated Name"}
    response = client.put(f'/products/{product_id}', json=data)
    context.response = response

@when('I delete the product with id {product_id}')
def step_impl(context, product_id):
    client = app.test_client()
    response = client.delete(f'/products/{product_id}')
    context.response = response

@when('I request the list of products')
def step_impl(context):
    client = app.test_client()
    response = client.get('/products')
    context.response = response

@when('I search products by name "{name}"')
def step_impl(context, name):
    client = app.test_client()
    response = client.get(f'/products?name={name}')
    context.response = response

@when('I search products by category "{category}"')
def step_impl(context, category):
    client = app.test_client()
    response = client.get(f'/products?category={category}')
    context.response = response

@when('I search products by availability "{available}"')
def step_impl(context, available):
    client = app.test_client()
    response = client.get(f'/products?available={available}')
    context.response = response

@then('I should receive a list of all products')
def step_impl(context):
    assert context.response.status_code == 200
    data = json.loads(context.response.data)
    assert isinstance(data, list)

@then('I should receive the product details')
def step_impl(context):
    assert context.response.status_code == 200
   
