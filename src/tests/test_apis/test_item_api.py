from core.config import PREFIX

items_endpoint = f"{PREFIX}/items"

def test_create_item(client):
    body = {"name": "Item1", "description": "Description1", "price": 100.0, "tax": 10.0, "category_id": 1}
    response = client.post(f"{items_endpoint}/create", json=body)

    assert response.status_code == 200
    assert response.json()["name"] == "Item1"
    assert response.json()["description"] == "Description1"

def test_get_items(client):
    response = client.get(f"{items_endpoint}/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_by_id(client):
    response = client.get(f"{items_endpoint}/1")
    
    assert response.status_code == 200
