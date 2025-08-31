import json
import pytest
from service.routes import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_read(client):
    client.post('/products', json={"name":"Toy","category":"toys","available":True})
    resp = client.get('/products/1')
    assert resp.status_code == 200

def test_update(client):
    client.post('/products', json={"name":"Book","category":"books","available":True})
    resp = client.put('/products/1', json={"name":"Updated Book"})
    assert resp.json['name'] == "Updated Book"

def test_delete(client):
    client.post('/products', json={"name":"Laptop","category":"electronics","available":True})
    resp = client.delete('/products/1')
    assert resp.status_code == 204

def test_list_all(client):
    client.post('/products', json={"name":"Pen","category":"stationery","available":True})
    resp = client.get('/products')
    assert resp.status_code == 200

def test_list_by_name(client):
    client.post('/products', json={"name":"Phone","category":"electronics","available":True})
    resp = client.get('/products?name=Phone')
    assert resp.json[0]['name'] == "Phone"

def test_list_by_category(client):
    client.post('/products', json={"name":"TV","category":"electronics","available":True})
    resp = client.get('/products?category=electronics')
    assert resp.json[0]['category'] == "electronics"

def test_list_by_availability(client):
    client.post('/products', json={"name":"Chair","category":"furniture","available":True})
    resp = client.get('/products?available=true')
    assert resp.json[0]['available'] is True
