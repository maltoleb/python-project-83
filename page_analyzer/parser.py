from bs4 import BeautifulSoup


def extract_h1(html):
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return None


def extract_title(html):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("title")
    if title:
        return title.get_text(strip=True)
    return None


def extract_description(html):
    soup = BeautifulSoup(html, "html.parser")
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        return meta.get("content")
    return None