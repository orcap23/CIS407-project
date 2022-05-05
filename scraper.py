"""
Web Scraping

AUTHOR: Madeline Porcaro

functions:

news_rss():
Scrapes specified url for title, link and enclosure
    params: None
    
    returns: call to save_info() with list

save_info(article_list: list)
Takes list item and writes items to a JSON FILE. 
    params: list object

    returns: none

"""
import json
import requests
from bs4 import BeautifulSoup

# scraping function
def news_rss():

    # empty list to append data
    podcast_items = []

    try:
        # current url: The Daily from the New York Times
        url = 'https://feeds.simplecast.com/54nAGcIl'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='xml')
        
        
        items = soup.findAll('item')

        # get mp3 links -> limit 1 because find_all returns a list item
        enclosure = [link['url'] for link in soup.find_all('enclosure', limit = 1) if 'mp3' in link['url']]

        # item tags in RSS file
        for i in items:

            title = i.find('title').text
            link = i.find('link').text
            
            # init dictionary
            podcast_item = {
                'title': title,
                'link': link,
                'enclosure': enclosure
            }
            # append items
            podcast_items.append(podcast_item)

            # write to file
        return save_info(podcast_items)

    except Exception as e:
        print('Scraping Failed. See exception:')
        print(e)

# use json to write to text file
def save_info(article_list):
    json_object = json.dumps(article_list, indent=4, sort_keys=True)
    with open('rss.json', 'w') as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    print('Start scraping')
    news_rss()
    print('Finished scraping')
