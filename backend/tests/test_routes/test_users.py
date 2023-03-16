import json

def test_create_user(client):
    data = {"username":"test", "email":"abc@text.com","password":"yves15$"}
    data_json = json.dumps(data)
    response = client.post(url='/users/', data=data_json)
    assert response.status_code == 200
    