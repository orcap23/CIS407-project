"""
Web Scraping

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
from tkinter import *

master = Tk()
master.configure(bg='light grey')

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

            title = i.find('title')
            link = i.find('link')
            
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

def display():
    # object of tkinter
    # and background set to grey
    master = Tk()
    master.configure(bg='light grey')
    
    # Variable Classes in tkinter
    title = StringVar();
    meta = StringVar();
    art_dec = StringVar();
    
    # Creating label for each information
    # name using widget Label
    Label(master, text="Title :",
        bg = "light grey").grid(row=3, sticky=W)
    Label(master, text="Meta information :",
        bg = "light grey").grid(row=4, sticky=W)
    Label(master, text="Article description :",
        bg = "light grey").grid(row=5, sticky=W)
    
    # Creating label for class variable
    # name using widget Entry
    Label(master, text="", textvariable=title,
        bg = "light grey").grid(row=3,column=1, sticky=W)
    Label(master, text="", textvariable=meta,
        bg = "light grey").grid(row=4,column=1, sticky=W)
    Label(master, text="", textvariable=art_dec,
        bg = "light grey").grid(row=5,column=1, sticky=W)
    mainloop()


# use json to write to text file
def save_info(article_list):
    for elem in article_list:
        print(f"{elem}\n\n")

    # json_object = json.dumps(article_list, indent=4, sort_keys=True)
    with open('FILE.txt', 'w') as outfile:
        for elem in article_list: 
            outfile.write('%s\n' % elem)


if __name__ == '__main__':
    print('Start scraping')
    news_rss()
    print('Finished scraping')
