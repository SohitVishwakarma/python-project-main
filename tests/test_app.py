from app import app


def test_index():
    # Create a test client using Flask's test_client method
    client = app.test_client()

    # Use the client to simulate accessing the '/' route
    response = client.get('/')

    # Check if the response data matches the expected string
    assert response.data == b"Hello, worlfdfddixu8uxquixhqisxhqsoxh isxhs xquisxh qsihx hqs xix ishwxh ddddddddddd!"
