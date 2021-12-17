from bs4 import BeautifulSoup
import requests


#
# with open("website.html",encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# all_a_tags = soup.find_all(name="a")
# for tag in all_a_tags:
#     print(tag.get("href"))
#


response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []
for article in articles:
    article_text = article.get_text()
    article_texts.append(article_text)
    article_link = article.get('href')
    article_links.append(article_link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_upvotes)

