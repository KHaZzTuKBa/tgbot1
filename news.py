from bs4 import BeautifulSoup as bs
import requests

def news():
    main_link = "https://izhlife.ru/news"
    req = requests.get(main_link)
    html = bs(req.text, "html.parser")
    items = html.find_all(attrs={"class" : "main_news"})

    all_params = []
    items = items[1:]

    for item in items:
        params = {
            "theme": "",
            "idea": "",
            "link": "",
            "date": "",
            "epilog": ""
        }

        theme = item.find(attrs={"class" : "cat_news"})
        params['theme'] = theme.text

        idea = item.find("h3").text
        params["idea"] = idea

        link = item.find("h3")
        link = link.find("a")["href"]
        link = main_link + link
        params["link"] = link

        date = item.find(attrs={"class" : "short_story_date"})
        params["date"] = date.text

        epilog = item.find(attrs={"class" : "short_story"})
        params["epilog"] = epilog.text
        all_params.append(params)

    return all_params