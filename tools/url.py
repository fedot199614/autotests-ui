from furl import furl

def build_url(protocol: str, host: str, path: str, query_params: dict = {}) -> str:
    f = furl()

    f.scheme = protocol
    f.host = host
    f.path.segments = path.strip('/').split('/')
    f.add(query_params)

    return f.url