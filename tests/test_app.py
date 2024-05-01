def test_index():
    # Create a test client using Flask's test_client method
    client = app.test_client()

    # Use the client to simulate accessing the '/' route
    response = client.get('/')

    # Check if the expected text is present in the response data
    assert b"Hello, worlfdfddixu8uxquixhqisxhqsoxh isxhs xquisxh qsihx hqs xix ishwxh ddddddddddd!" in response.data
