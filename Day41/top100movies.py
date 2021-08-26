from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century")
website = response.text

soup = BeautifulSoup(website, 'html.parser')
titles = list(reversed([title.getText() for title in soup.select(selector="div h2 strong")]))
order = list(range(1,101))

with open('100GreatestFilms.txt', mode='w', encoding='utf-8') as file:
    string = "Source: The Guardian\n\n"
    for num, title in zip(order, titles):
        string += f"{num}) {title}\n"
    file.write(string)
