from bs4 import BeautifulSoup as BS
html = "SausageKraut.html"
soup = BS(open(html))
results = soup.find_all("li", {"itemprop": "ingredients"})
print results