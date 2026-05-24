import re

def is_valid_url(url: str):
    pattern = re.compile(
        r'^'
        r'https?://'                # Протокол
        r'(?:[\w.:-]+\.)*[\w.-]+'   # Домен
        r'(?::\d+)?'                # Порт (опционально)
        r'(?:/[\w@-]*)*'            # Путь
        r'(?:/[\w./~%#&=?\[\]-]*)?',           # query - параметры
        re.IGNORECASE
    )
    return bool(pattern.match(url))



def main():
    urls = [
        "http://example.com",
        "https://example.com",
        "http://www.example.com",
        "https://subdomain.example.com",
        "http://example.com/path",
        "https://example.com/path/to/resource",
        "http://example.com/path?query=param",
        "https://example.com/path?query=param&other=value",
        "http://example.com:8080",
        "https://example.com:443/path",
        "http://user:password@example.com",
        "http://example.com#anchor"
    ]

    for url in urls:
        if is_valid_url(url):
            print(f"Correct url: {url}")
        else:
            print(f"Not correct url: {url}")




if __name__ == "__main__":
    main()
