import re 

REMOVE_PATTERNS = [
    r"\(.*?\)",     # remove (Official Video)
    r"\[.*?\]",     # remove [HD]
    r"official video",
    r"lyrics",
    r"remastered",
    r"audio",
]

def clean_title(title: str) -> str:
    title = title.lower()

    for pattern in REMOVE_PATTERNS:
        title = re.sub(pattern, "", title)

    title = re.sub(r"\s+", " ", title).strip()

    return title