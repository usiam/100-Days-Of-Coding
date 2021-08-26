from bs4 import BeautifulSoup
import lxml

with open('website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# soup now contains the html
print(soup.title) # prints the <title>string</title> line
print(soup.title.string) # prints the string only
print(soup.p) # prints the first <p> tag
all_anchor_tags, all_para_tags = soup.find_all(name="a"), soup.find_all(name="p")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading, heading.getText())

sec_heading = soup.find(name="h3", class_="heading")
print(sec_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)

soup.find_all()