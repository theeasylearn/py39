# 1) findout website that can provide ai news with heading and text 
#   https://www.therundown.ai/news
# 2) extract all the news using requests and beautifulsoup4
import requests
from bs4 import BeautifulSoup
from gtts import gTTS

def getContentFromSite():
    url = "https://www.therundown.ai/news?category=ai#stories"
    response = requests.get(url)
    return response.text
def getNews(siteContent):
    soup = BeautifulSoup(siteContent, "html.parser")
    print(soup.title.text)
    div = soup.find("div", class_="mt-8 grid gap-6 md:grid-cols-2 lg:grid-cols-3")
    articles = div.find_all('article')
    news = []
    for article in articles:
        heading = article.find("a",class_="group-hover:text-brand-violet")
        content = article.find("p",class_="mt-4 text-sm leading-6 text-mute")
        # print(heading.text)
        # print(content.text)
        # print("_"*100)
        news.append("news heading " + heading.text + " News detail " + content.text)
    return news
siteContent = getContentFromSite()
news = getNews(siteContent)
hindi = gTTS(text=news[0], lang="hi")
hindi.save("hindi.mp3")



