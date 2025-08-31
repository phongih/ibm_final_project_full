from behave import given
from service.routes import products

@given('the product list is loaded')
def step_impl(context):
    products.clear()
    products.append({"id":1,"name":"Phone","category":"electronics","available":True})
    products.append({"id":2,"name":"Book","category":"books","available":True})
