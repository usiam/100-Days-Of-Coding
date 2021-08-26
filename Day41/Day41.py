from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_website = response.text

soup = BeautifulSoup(yc_website, 'html.parser')
articles = soup.find_all(name="a", class_="storylink")
article_titles = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

article_infos = list(zip(article_upvotes, article_titles, article_links))

for info in article_infos:
    print(info[0], info[1], info[2])

most_popular = article_infos[article_upvotes.index(max(article_upvotes))]
print(f"Most popular article in the list: {most_popular[0]}, {most_popular[1]}, {most_popular[2]}")





