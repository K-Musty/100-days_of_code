from operator import index

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
# print(yc_webpage)
soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(class_="athing submission")
articles_links = []
articles_texts = []
article_votes = []
for article in articles:
    titleline = article.select_one(".titleline")

    if titleline:
        link = titleline.find("a")["href"]
        articles_links.append(link)
        text = titleline.getText(strip=True)
        articles_texts.append(text)
upvotes = soup.find_all(name="span", class_="score")

for votes in upvotes:
    article_votes.append(int(votes.getText().split()[0]))

largest = max(article_votes)
largest_index = article_votes.index(largest)

print(articles_texts[largest_index])
print(articles_links[largest_index])

# for i in range(len(articles_links) -1):
#     print(articles_texts[i])
#     print(articles_links[i])
#     print(f"{article_votes[i]}\n")












# with open("website.html", mode="r") as file:
#     data = file.read()
# soup = BeautifulSoup(data, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# anchor_tags = soup.find_all(name="a")
# # for tag in anchor_tags:
# #     print(tag.get("href"))
#
# print(anchor_tags)
#
# h1 = soup.find(name="h1", id="name")
# print(h1.string)
#
# heading = soup.find(name="h3", class_="heading")
# print(heading.getText())
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)