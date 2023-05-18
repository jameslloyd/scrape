from config import Config
import random
import requests
import logging
import threading

logging.basicConfig(format=Config.LOGGING_FORMAT,level=Config.LOGGING_LEVEL,datefmt=Config.LOGGING_DATEFMT)

def split_list(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]

def get_html(url, proxy = Config.PROXY_ENABLE):
    
    useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36']
    if proxy:
        proxy = random.choice(Config.PROXYS)
        if proxy == '':
            proxyh = False
        else:
            proxyh = {"http":proxy,"https":proxy}
    useragent = random.choice(useragents)
    headers = {"User-Agent": useragent}
    output = requests.get(url, headers=headers,proxies=proxyh)
    logging.info(f'requesting {url} with useragent {useragent} and proxy {proxy}')
    print(output.text)
    return output
    
def thread_jobs(jobs,noofthreads,function):
    # jobs should be a list of urls  
    # threads is the number of concurrent threads
    jobgroups = [jobs[x:x+noofthreads] for x in range(0, len(jobs), noofthreads)]
    for group in jobgroups:
        threads = list() 
        if len(group) < noofthreads:
            # last group wont nessecarily be full
            noofthreads = len(group)
        for index in range(noofthreads):
            url = str(group[index])
            logging.info(f"Starting Thread {index} for event id {group[index]}.")
            x = threading.Thread(target=function, args=(url,))
            threads.append(x)
            x.start()
        
        for index, thread in enumerate(threads):
            logging.debug(f"Starting grab {group[index]} ")
            thread.join()
            logging.debug(f"Completed {group[index]}")             


if __name__ == "__main__":
    #html = get_html('http://icanhazip.com')
    #print(html.text)
    
    
    listofjobs = ['http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com','http://icanhazip.com']
    thread_jobs(listofjobs,10,get_html)