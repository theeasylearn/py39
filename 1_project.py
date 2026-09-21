# 1) findout website that can provide ai news with heading and text 
#   https://www.therundown.ai/news
# 2) extract all the news using requests and beautifulsoup4
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import translators as ts
from playsound import playsound
sound_file_name = "news.mp3"

def getContentFromSite():
    url = "https://www.therundown.ai/news?category=ai#stories"
    response = requests.get(url)
    print("Page found....")
    return response.text
def getNews(siteContent):
    soup = BeautifulSoup(siteContent, "html.parser")
    print(soup.title.text)
    div = soup.find("div", class_="mt-8 grid gap-6 md:grid-cols-2 lg:grid-cols-3")
    articles = div.find_all('article')
    news = []
    count = 1
    for article in articles:
        #get heading of article
        heading = article.find("a",class_="group-hover:text-brand-violet")
        #get content of article
        content = article.find("p",class_="mt-4 text-sm leading-6 text-mute")
        # print(heading.text)
        # print(content.text)
        # print("_"*100)
        news.append("news  " + str(count) + " : " + heading.text + " News detail " + content.text)
        count= count + 1
    print("Content extracted....")
    return news

def getTranslatedText(temp_news):
    translated_news = ts.translate_text(temp_news,from_language='en', to_language='hi',translator='google')
    print("Content Converted into another language....")
    return translated_news
def TextToAudio(translated_news):
    global sound_file_name
    print("Converting into audio started (it may take some times(few minutes)).....")
    hindi = gTTS(text=translated_news, lang="hi")
    hindi.save(sound_file_name)
    print("Audio generated")
siteContent = getContentFromSite()
news = getNews(siteContent)
temp_news = ' '.join(news) 
translated_news =  getTranslatedText(temp_news)
TextToAudio(translated_news)
#play hindi text using tts 
print("Playing audio, Press Ctrl+c to stop in between")
playsound(sound_file_name)
print("program finished....")
