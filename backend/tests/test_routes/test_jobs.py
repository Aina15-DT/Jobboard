import json

def test_create_job(client):
    data = {
        "title":"test", 
        "company":"ABC",
        "company_url":"https://www.fdj.com" ,
        "location":"France", 
        "description": "Not Hiring", 
        "date_posted" : "2022-07-20"
        }
    data_json = json.dumps(data)
    response = client.post(url='/job/create-job', data=data_json)
    print(response.content)
    assert response.status_code == 200


def test_retrieve_job_by_id(client):
    data = {
        "title":"SDE 1 Yahoo",
        "company" :"testhoo",
        "company_url" : "https://www.fdj.com",
        "location" : "USA",
        "description" :"Testing",
        "date_posted":"2022-07-20"
    }

    resp1 = client.post(url="/job/create-job", data=json.dumps(data))
    response = client.get(url="/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"
    