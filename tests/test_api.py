def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_payload_and_cache_headers(client):
    # Arrange
    expected_cache_control = "no-store, no-cache, must-revalidate, max-age=0"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.headers["cache-control"] == expected_cache_control
    assert response.headers["pragma"] == "no-cache"
    assert response.headers["expires"] == "0"

    activities_payload = response.json()
    assert isinstance(activities_payload, dict)
    assert "Chess Club" in activities_payload
    assert "description" in activities_payload["Chess Club"]
    assert "schedule" in activities_payload["Chess Club"]
    assert "max_participants" in activities_payload["Chess Club"]
    assert "participants" in activities_payload["Chess Club"]
