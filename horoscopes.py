import requests
from bs4 import BeautifulSoup as bs

def find_links():
    main_link = "https://horo.mail.ru/"
    req = requests.get(main_link)
    html = bs(req.text, 'html.parser')
    links = {}
    for i in html.find_all(attrs={"class" : "cols__column cols__column_small_percent-25 cols__column_medium_percent-25 cols__column_large_percent-25 margin_bottom_30 align_center"}):
        name = i.find(attrs={"class" : "p-imaged-item__name"}).text
        link = i.find("a")['href']
        links.setdefault(name, main_link + link[1:])

    return links

def get_info(link):
    main_link = link
    req = requests.get(main_link)
    html = bs(req.text, 'html.parser')
    text = html.find(attrs={"class" : "article__item article__item_alignment_left article__item_html"}).text
    return text