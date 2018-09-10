import requests
from bs4 import BeautifulSoup

#Pre-2003 format:
url = 'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:31995L0046'
# page = requests.get('https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:31995L0046')
# print(page.status_code)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# title = soup.find('p', id='translatedTitle')
# print(title.get_text())
#
# text = soup.find('div', id='TexteOnly')
# print(text.get_text()[10:50])

#2003 and onwards:
# url = 'https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1536371039325&uri=CELEX:32017R0352'
page = requests.get(url)

print('eur-lex.europa.eu/legal-content/EN/TXT/' in url)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('p', id='translatedTitle')
print(title.get_text())

text_box = soup.find('div', id='document1')
text_resultSet = text_box.find_all('p')
merged_text = ""

for paragraph in text_resultSet:
    merged_text = merged_text + '\n' + paragraph.get_text()
    # print(paragraph.get_text())
    # print(type(paragraph))

print(merged_text)