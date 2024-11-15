from bs4 import BeautifulSoup

with open("website.html", mode="r") as file:
    data = file.read()
soup = BeautifulSoup(data, "html.parser")
print(soup.title.string)
