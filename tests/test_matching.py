from spotify import SpotifyClient


def test_choose_best_match_returns_correct_song():
    client = SpotifyClient("fake-token")

    youtube_title = "apology navaan sandhu"

    fake_results = [
        {
            "name": "Apology",
            "artists": [{"name": "Navaan Sandhu"}],
            "id": "correct-id"
        },
        {
            "name": "Game",
            "artists": [{"name": "Sidhu Moose Wala"}],
            "id": "wrong-id"
        }
    ]

    result = client.choose_best_match(youtube_title, fake_results)

    assert result == "correct-id"


def test_choose_best_match_returns_none_when_no_good_match():
    client = SpotifyClient("fake-token")

    youtube_title = "completely unknown song"

    fake_results = [
        {
            "name": "Different Track",
            "artists": [{"name": "Different Artist"}],
            "id": "wrong-id"
        }
    ]

    result = client.choose_best_match(youtube_title, fake_results)

    assert result is None


def test_choose_best_match_prefers_better_similarity():
    client = SpotifyClient("fake-token")

    youtube_title = "my block sidhu moose wala"

    fake_results = [
        {
            "name": "My Block",
            "artists": [{"name": "Sidhu Moose Wala"}],
            "id": "best-id"
        },
        {
            "name": "My Song",
            "artists": [{"name": "Other Artist"}],
            "id": "other-id"
        }
    ]

    result = client.choose_best_match(youtube_title, fake_results)

    assert result == "best-id"