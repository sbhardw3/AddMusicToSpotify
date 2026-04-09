from spotify import SpotifyClient


def test_find_playlist_by_name_returns_correct_id(monkeypatch):
    client = SpotifyClient("fake-token")

    def fake_get_user_playlists():
        return [
            {"name": "Punjabi Mix", "id": "123"},
            {"name": "Gym Songs", "id": "456"}
        ]

    monkeypatch.setattr(client, "get_user_playlists", fake_get_user_playlists)

    result = client.find_playlist_by_name("Punjabi Mix")

    assert result == "123"

def test_find_playlist_by_name_returns_none_when_missing(monkeypatch):
    client = SpotifyClient("fake-token")

    def fake_get_user_playlists():
        return [
            {"name": "Punjabi Mix", "id": "123"}
        ]

    monkeypatch.setattr(client, "get_user_playlists", fake_get_user_playlists)

    result = client.find_playlist_by_name("Road Trip")

    assert result is None

def test_find_playlist_by_name_returns_none_when_missing(monkeypatch):
    client = SpotifyClient("fake-token")

    def fake_get_user_playlists():
        return [
            {"name": "Punjabi Mix", "id": "123"}
        ]

    monkeypatch.setattr(client, "get_user_playlists", fake_get_user_playlists)

    result = client.find_playlist_by_name("Road Trip")

    assert result is None