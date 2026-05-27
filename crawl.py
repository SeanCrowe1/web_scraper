import urllib.parse as urllib

def normalize_url(url: str) -> str:
    parts = urllib.urlparse(url)

    netloc = parts.netloc
    if netloc == "":
        return "Invalid URL"
    
    if parts.path[-1] == "/":
        path = parts.path[:-1]
    else:
        path = parts.path

    if path == "":
        return "Invalid URL"

    normalized_url = f"{netloc}{path}"

    return normalized_url
    