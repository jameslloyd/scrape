from config import Config
import random, requests, logging

logging.basicConfig(format=Config.LOGGING_FORMAT,level=Config.LOGGING_LEVEL,datefmt=Config.LOGGING_DATEFMT)


def get_html(url, proxy = Config.PROXY_ENABLE):
    
    useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36']
    if proxy:
        proxy = random.choice(Config.PROXYS)
        if proxy == '':
            proxy = False
        else:
            proxyh = {"http":proxy,"https":proxy}
    useragent = random.choice(useragents)
    headers = {"User-Agent": useragent}
    output = requests.get(url, headers=headers,proxies=proxyh)
    logging.info(f'requesting {url} with useragent {useragent} and proxy {proxy}')
    return output
    
    
if __name__ == "__main__":
    html = get_html('http://icanhazip.com')
    print(html.text)