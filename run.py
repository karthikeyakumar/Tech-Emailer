import smtplib, ssl
import time
import requests
from bs4 import BeautifulSoup
import cssutils
import yagmail


emails = []


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
            imagelink = imagelink[0:len(imagelink)-1]
            #print(imagelink)
            data = get_article_data(i)
            link = "https://inshorts.com" + i.find("a", class_="clickable").get("href")
            part_content = '''<!DOCTYPE html>
                <html>
                <head>
                </head>
                    <body>
                        <div style="background-color:#eee;padding:5px 10px;">
                            <h1 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">{title}</h1>
                        </div>
                        <div>
                            <div style="padding:2px; width:900px">
                                    <div style= "margin: 10px; float: left; margin: 20px 20px 20px 20px">
                                    <img src={imagelink} length="100" width="200">
                                    </div>
                                    <div style= "margin: 10px; padding: 20px; text-align: justify">
                                    <p>{data}</p>
                                    <a href={link}>Read more</a>
                                    </div>
                            </div>
                        </div>
                    </body>
                </html>
                '''.format(title=title, data=data, link=link, imagelink=imagelink)

            out.append(part_content)
    except Exception as e:
        print(e)
    return out


def sendMail():
    yag = yagmail.SMTP(email, password)
    contents = main()
    for i in emails:
        yag.send(i, "Daily Tech News To a Developer By a Developer", contents)


if __name__ == "__main__":
    sendMail()
