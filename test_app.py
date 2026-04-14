from app import app

def test_flask_app():
    print("\nRunning Flask integration test...")

    app.testing = True
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    print("Flask integration test passed ✅")

test_flask_app()
