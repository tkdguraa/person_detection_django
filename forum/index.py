import requests
import threading
import re
import jieba
from bs4 import BeautifulSoup

# dynamic url crawler
def get_news_urls(soup):
    urls =  []
    for a in soup.find_all('a'):
        if a.has_attr('target') and a.has_attr('class'):
            if a['target'] == '_blank' and a['class'][0] == 'linkto':
                if a.has_attr('href'):
                    if a['href'][-4:] == 'html' or a['href'][-3:] == 'htm':
                        urls.append(a['href'])
    return urls

# get static urls
def get_urls_from_file(path):
    urls = []
    with open(path, 'r') as f:
        urls = f.readlines()

    for idx, url in enumerate(urls[:-1]):
        urls[idx] = url[:-1]

    return urls

def download_page(idx, url, datas):
    source = requests.get(url)
    text = source.text
    data = dict()
    
    soup = BeautifulSoup(text, 'html.parser')
    title = soup.find_all('title')[0].text
    date =  re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}|"     # yyyy-mm-dd
                    + r"\d{4}-\d{1}-\d{1} \d{2}:\d{2}|"     # yyyy-m-d
                    + r"\d{4}'/\d{2}'/\d{2} \d{2}:\d{2}|"   # yyyy/mm/dd
                    + r"\d{4}'/\d{1}'/\d{1} \d{2}:\d{2}"    # yyyy/m/d
                    , soup.text).group()

    data['url'] = url
    data['title'] = title
    data['date'] = date
    data['keywords'] = []
    data['text'] = ""

    for p in soup.find_all('p'):
        keywords = jieba.lcut_for_search(p.text)
        data['keywords'] = data['keywords'] + keywords
        data['text'] = data['text'] + p.text

    datas.append(data)

def get_news_from_web():
    source = requests.get('http://news.qq.com/')
    text = source.text
    soup = BeautifulSoup(text, 'html.parser')
        
    # urls = get_news_urls(soup)
    urls = get_urls_from_file('./urls.txt')

    datas = []
    for idx, url in enumerate(urls):
        t = threading.Thread(name=str(idx), target=download_page, args=(idx, url, datas))
        t.start()
        t.join()

    print('datas:', datas)
    print('success')

    return datas