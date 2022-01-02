import smtplib, ssl
import time
import requests
from bs4 import BeautifulSoup
import cssutils
import yagmail


emails = ["karthikeyakumar.nallam@gmail.com", "pmanikandan.nair2018@vitstudent.ac.in"]


def get_image_url(uri):
    imagelink = uri.find("div")["style"]
    style = cssutils.parseStyle(imagelink)
    url = style["background-image"]
    url = url.replace("url(", "").replace(")", "")
    return url


def get_article_data(url):
    return url.find("div", itemprop="articleBody").get_text()


def main():
    url = "https://inshorts.com/en/read/technology"
    out = ""
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find_all("div", class_="news-card z-depth-1")
        out = []
        for i in result:
            title = i.find("span", itemprop="description").get("content")
            imagelink = get_image_url(i)
            data = get_article_data(i)
            link = "https://inshorts.com" + i.find("a", class_="clickable").get("href")
            out.append(str("\n".join([title, imagelink, link])))
    except Exception as e:
        print(e)
    return out


def sendMail():
    yag = yagmail.SMTP("mail", "password")
    contents = main()
    for i in emails:
        yag.send(i, "Daily Tech News To a Developer By a Developer", contents)


if __name__ == "__main__":
    sendMail()
