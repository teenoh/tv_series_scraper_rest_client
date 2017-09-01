# from __future__ import unicode_literals
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
#import os
#import re
from pprint import pprint

"""
   helps in scraping o2tvseries for data

   scrape_site: default function for scraping sites and getting links

   get_series_links: gets the links and titles of all series in dict format

   get_episodes_links: gets the links and corresponding episodes and seasons in 
                       nested dict format when provided the series link
                       i.e format = s01 : {
                                            "episode 01": "episode_download link"
                                            .
                                            .
                                            .
                                    }

   get_series_image:   gets the url of the series image

   get_download_link: scrapes site for download link when provided episode link
                       returns mp4 download link

    pagination:      gets the links for other pages containing episodes, such pages occur when the episodes are more than 10
"""


def scrape_site(url, get_image=False):
    with urlopen(url) as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="data")

        links = {(x.a.get_text()).lower(): x.a.get("href")
                 for x in divs}

        return links


def pagination(url):
    with urlopen(url) as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="pagination")
        divs = BeautifulSoup(str(divs), 'html.parser')
        links = divs.find_all('a')
        links = [x.get('href') for x in links]
        return links


def get_series_links():
    series = scrape_site("http://tvshows4mobile.com/search/list_all_tv_series", get_image=True)
    return series


def get_series_image(series_link):
    with urlopen(series_link) as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="img")
        img = [x.img.get('src') for x in divs]
        return img[0]

 
def get_episodes_links(series_link):
    seasons = scrape_site(series_link)
    for season, link in seasons.items():
        seasons[season] = [link]
        seasons[season].extend(
            pagination(seasons[season][0]))
    # links = pagination(series_link)
    #    seasons.update(scrape_site(link))

    episodes = {}
    for season, links in seasons.items():
        episodes[season] = {}
        for link in links:
            episode_pages = scrape_site(link)
            episodes[season].update({x: get_download_link(y) for x,y in episode_pages.items()})
            # episodes[season].update(episode_dict)
    return episodes




def get_download_link(episode_link):
    with urlopen(episode_link) as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="data")

        links = {x.a.get_text()[-3:]: x.a.get("href")
                 for x in divs
                 if x.a.get_text()[-3:] in ("3gp", "mp4")}

        # if string == "3gp": return links["3gp"]
        return links["mp4"]

#dump sample data
def scrape_data():
    data = get_series_links()
    episode_links = {}
    for key, value in data.items():
        episode_links.update({key: get_episodes_links(value)})
        print("completed : " + key)
    return episode_links


#load json data
# def load_sample_data():
#     with open('data.json', 'r') as fp:
#         data = json.load(fp)
#         fp.close()
#         return data

#pprint(series)
# boy = series['agents of shield']
# guy = get_episodes_links(boy)
# print(guy)
# print(pagination(guy))
# print(boy(guy)

# pprint(get_episodes_links(r"http://tvshows4mobile.com/The-Flash-3/index.html"))
# pprint(scrape_site(r"http://tvshows4mobile.com/The-Flash-3/index.html"))
# series= get_series_links()
# for key, value in series.items():
#         episode_links = get_episodes_links(value)
#         updated_episode_links = {}
#         for season, episode in episode_links:
#             updated_episode_links.update(
#                               { season:
#                                   { epis:
#                                       get_download_link() for epis, link in episode}
#                                })
# ...     all_links = {key: updated_episode_links}
# ...     pprint(all_links)
#
