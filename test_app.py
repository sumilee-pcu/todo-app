from app import app, todos


def setup_function():
    todos.clear()


def client():
    return app.test_client()


def test_empty_list():
    res = client().get("/api/todos")
    assert res.status_code == 200
    assert res.get_json() == []


def test_add_todo():
    res = client().post("/api/todos", json={"title": "원고 마감"})
    assert res.status_code == 201
    body = res.get_json()
    assert body["title"] == "원고 마감"
    assert body["done"] is False
