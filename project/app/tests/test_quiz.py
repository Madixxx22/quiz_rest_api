from fastapi.testclient import TestClient

from app.main import app

def test_request_quiz_clear_db():
    request_data = {"questions_num": 3}
    with TestClient(app) as client:
        response = client.post("/quiz", json=request_data)
    assert response.status_code == 200
    assert response.json() == {}

def test_request_quiz():
    request_data = {"questions_num": 3}
    with TestClient(app) as client:
        response = client.post("/quiz", json=request_data)
    assert response.status_code == 200
    assert response.json()["id_question"] is not None
    assert response.json()["text_question"] is not None
    assert response.json()["text_answer"] is not None
    assert response.json()["date_create_question"] is not None
