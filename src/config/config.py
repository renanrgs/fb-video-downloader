import os
from dataclasses import dataclass, field

__COOKIES = {
    'c_user': os.environ['FACEBOOK_USER_ID'],
    'xs': os.environ['FACEBOOK_XS']
}

__HEADERS = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en,en-US;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'viewport-width': '2560',
}


def get_cookies() -> dict:
    return __COOKIES


def get_headers() -> dict:
    return __HEADERS

# @dataclass(frozen=True, init=False)
# class Config:
#     cookies: dict = field(default_factory=_get_config()[0])
#     headers: dict = field(default_factory=_get_config()[1])
