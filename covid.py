from bs4 import BeautifulSoup as bs
import requests

def get_stat():
    a = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/")
    html = bs(a.text, 'html.parser')
    args = []

    for i in html.find_all(attrs={"class": "cv-countdown__item"}):
        args.append(i)

    out_string = "Проведено тестов: " + args[0].find("span").text[1:] + ",\n"
    out_string += "Выявлено случаев: " + args[1].find("span").text[:len(args[1].find("span").text)-1] + ",\n"
    out_string += "Выявлено случаев за последние сутки: " + args[2].find("span").text + ",\n"
    out_string += "Человек выздоровело: " + args[3].find("span").text + ',\n'
    out_string += "Человек умерло: " + args[4].find("span").text + "."

    return out_string