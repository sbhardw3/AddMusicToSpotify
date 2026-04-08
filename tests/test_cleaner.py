from cleaner import clean_title


def test_removes_official_video():
    title = "Apology - Official Video"
    assert clean_title(title) == "apology -"


def test_removes_lyrics():
    title = "295 lyrics"
    assert clean_title(title) == "295"


def test_removes_punjabi_song_label():
    title = "My Block | New Punjabi Songs 2022"
    assert clean_title(title) == "my block |"


def test_removes_brackets():
    title = "Apology [HD]"
    assert clean_title(title) == "apology"


def test_keeps_actual_song_words():
    title = "Navaan Sandhu - Apology"
    assert clean_title(title) == "navaan sandhu - apology"