
import requests
from bs4 import BeautifulSoup
import json

url= 'https://quotes.toscrape.com'
quotes_list= []
tag_list= []
authors_list= []
check_list = []
new_link= None

while True:
    if new_link == None:
        response = requests.get(url)
    else:
        response = requests.get(url+new_link)
    soup=BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', class_ ='quote')

    for quote in quotes:

        tags= quote.find_all('a', class_='tag')
        for tag in tags:
            tag_list.append(tag.text)
        author= quote.find('small', class_= 'author').text
        text = quote.find('span', class_ = 'text').text
        quotes_list.append({'tags':tag_list.copy(), 'author': author, 'quote': text})
        tag_list.clear()

        if author not in check_list:
            check_list.append(author)
            author_link= quote.find('a').get('href')
            autthor_response= requests.get('https://quotes.toscrape.com'+ author_link)
            author_soup = BeautifulSoup(autthor_response.text, 'lxml')
            fullname = author_soup.find('h3', class_= 'author-title').text
            born_date= author_soup.find('span', class_='author-born-date').text
            born_location= author_soup.find('span', class_='author-born-location').text
            description = author_soup.find('div', class_='author-description').text
            authors_list.append({'fullname': fullname,'born_date': born_date, 'born_location': born_location,'description': description })
    if soup.findChild('li', class_='next') == None:
        break
    else:
        new_link= soup.findChild('li', class_='next').find('a').get('href')




 


with open('quotes.json', 'w')as f:
    json.dump(quotes_list, f)

    

with open('authors.json', 'w')as f:
    json.dump(authors_list, f)
