import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# scores = soup.find_all(name="span", class_="score")
# score_list =[int(score.get_text().split()[0]) for score in scores]
# print(max(score_list))
articles = soup.find_all("span", class_="titleline")
article_texts =[]
article_links=[]
for article_tag in articles:
    text = article_tag.get_text()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_upvotes)
largest_number = max(article_upvotes)
index = article_upvotes.index(largest_number)
print(article_upvotes[index])
print(article_texts[index])