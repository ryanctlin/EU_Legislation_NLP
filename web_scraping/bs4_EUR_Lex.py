"""This module contains functions to extract the legislation texts from a given EUR-Lex website address"""

import requests
from bs4 import BeautifulSoup


def scrape_contents(url):
    """This function checks and accepts an EUR-Lex URL, extracts the legislation title and text.
    Returns title and text in JSON format."""

    #Check if EUR-Lex link supplied is supported
    if ('eur-lex.europa.eu/legal-content/EN/TXT/' in url):
        #GET page and convert content to bs4 soup
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        #Call get_title to extract legislation title
        title = scrape_title(soup)

        #Call get_text to extract legislation text
        text = scrape_text(soup)

        #Return json
        result = {"title": title, "text": text}
        return result


    else: #Throw value error
        raise ValueError("Unsupported URL")



def scrape_title(soup):
    """This function accepts the Beautiful Soup object of the full EUR-Lex page,
    and returns the title of the legislation"""
    title = soup.find('p', id='translatedTitle')
    title = title.get_text() #Extract text from bs4 tag object
    return title


def scrape_text(soup):
    """This function accepts the Beautiful Soup object of the full EUR-Lex page,
    and returns the text of the legislation as a list of Beautiful Soup tags"""
    text_box = soup.find('div', id='document1')
    text_resultSet = text_box.find_all('p')

    #Extract and concatonate text from bs4 resultSet object
    text = ""
    for paragraph in text_resultSet:
        text = text + '\n' + paragraph.get_text() #Note concatenation order

    return text