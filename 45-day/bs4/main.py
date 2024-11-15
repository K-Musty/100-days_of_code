from bs4 import BeautifulSoup

with open("website.html", mode="r") as file:
    data = file.read()
soup = BeautifulSoup(data, "html.parser")
# print(soup.title)
# print(soup.title.string)
anchor_tags = soup.find_all(name="a")
# for tag in anchor_tags:
#     print(tag.get("href"))

print(anchor_tags)

h1 = soup.find(name="h1", id="name")
print(h1.string)

heading = soup.find(name="h3", class_="heading")
print(heading.getText())

company_url = soup.select_one(selector="#name")
print(company_url)

headings = soup.select(".heading")
print(headings)