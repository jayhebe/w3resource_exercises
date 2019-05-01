import requests
import bs4
import json


def get_baidu_net_news():
    url = r"http://news.baidu.com/tech"
    response = requests.post(url)
    response.raise_for_status()
    # print(response.text)
    news_soup = bs4.BeautifulSoup(response.text, "html.parser")

    internet_news = news_soup.select("div[id='internet_news'] ul li a")
    # print(internet_news)
    news = []
    for link in internet_news:
        title = link.text
        if len(title) > 30:
            title = (title[:30] + "...")

        news.append({"title": title, "link": link.get("href")})

    return json.dumps(news)


if __name__ == "__main__":
    for item in json.loads(get_baidu_net_news()):
        print(item["title"], item["link"])
