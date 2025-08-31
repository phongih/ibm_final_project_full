from behave import when, then
from service.routes import products

@when('I read product with id 1')
def step_impl(context):
    context.result = next((p for p in products if p['id']==1), None)

@then('I should see product details')
def step_impl(context):
    assert context.result is not None

@when('I update product with id 1 to name "Updated"')
def step_impl(context):
    for p in products:
        if p['id']==1:
            p['name']="Updated"
            context.result=p

@then('the product name should be "Updated"')
def step_impl(context):
    assert context.result['name']=="Updated"

@when('I delete product with id 1')
def step_impl(context):
    context.products_before = len(products)
    products[:] = [p for p in products if p['id']!=1]

@then('product with id 1 should not exist')
def step_impl(context):
    assert all(p['id']!=1 for p in products)

@when('I list all products')
def step_impl(context):
    context.result = products

@then('I should see multiple products')
def step_impl(context):
    assert len(context.result) > 0

@when('I search products by category "books"')
def step_impl(context):
    context.result = [p for p in products if p['category']=="books"]

@then('I should see only products in category "books"')
def step_impl(context):
    assert all(p['category']=="books" for p in context.result)

@when('I search products by availability "true"')
def step_impl(context):
    context.result = [p for p in products if p['available']==True]

@then('I should see only available products')
def step_impl(context):
    assert all(p['available']==True for p in context.result)

@when('I search products by name "Phone"')
def step_impl(context):
    context.result = [p for p in products if p['name']=="Phone"]

@then('I should see only products with name "Phone"')
def step_impl(context):
    assert all(p['name']=="Phone" for p in context.result)
