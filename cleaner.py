import re 

REMOVE_PATTERNS = [
    r"\(.*?\)",
    r"\[.*?\]",
    r"official video",
    r"official song",
    r"lyrics",
    r"remastered",
    r"audio",
    r"new punjabi songs? \d{4}",
    r"latest punjabi songs? \d{4}",
    r"punjabi songs? \d{4}",
    r"new punjabi songs?",
    r"latest punjabi songs?",
]

def clean_title(title: str) -> str:
    title = title.lower()

    for pattern in REMOVE_PATTERNS:
        title = re.sub(pattern, "", title)

    title = re.sub(r"\s+", " ", title).strip()

    return title