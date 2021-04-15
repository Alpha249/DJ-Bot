# To-Do:
# 1. Sort company link list into separate lists - ✓
# 2. Export link list to individual csv files - ✓
# 3. Figure out way to remove column name in .csv - ✓
# 4. Filter links based on date - ✓
# 5. Change links data to title - ✓
# 6. Filter news sources from title data in .csv - ✓

import random
import time
from datetime import datetime, date

from itertools import islice
import requests
from bs4 import BeautifulSoup

start = time.perf_counter()

companies = ['Google', 'Microsoft']
dates = []
f_date = []
titles = []
user_agents = []
links = []

with open('guide/useragents.txt', 'r') as ua:
    ua = ua.readlines()
    for p in ua:
        p = p.replace('\n', '')
        user_agents.append(p)

headers = {
    "User-Agent": random.choice(user_agents),
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive"

}


# Get news for any company/product


def News(thing, count):
    # Initialize BeautifulSoup and requests
    URL = f"https://news.google.com/rss/search?q={thing}&hl=en-US&gl=US&ceid=US:en"
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'xml')

    # Link filtering
    link_ = soup.find_all("link")
    for v in link_:
        links.append(v.get_text())

    # Title filtering
    title_ = soup.find_all("title")
    for v in title_:
        titles.append(v.get_text())

    # Date filtering
    Date_ = soup.find_all("pubDate")
    for n in Date_:
        dates.append(n.get_text())

    for t in dates:
        obj = datetime.strptime(t, '%a, %d %b %Y %H:%M:%S %Z')
        d = date(year=obj.year, month=obj.month, day=obj.day)
        f_date.append(d.strftime('%d-%b-%Y'))

    # Create t_dictionary
    t_dictionary = dict(zip(titles, f_date))
    l_dictionary = dict(zip(links, f_date))

    for key, value in dict(t_dictionary).items():
        vald = datetime.strptime(value, '%d-%b-%Y')
        today = date.today()

        if vald.month == today.month:
            if vald.day >= int(today.day) - 2:
                pass
            else:
                del t_dictionary[f'{key}']
        else:
            del t_dictionary[f'{key}']

        pass

    for key, value in dict(l_dictionary).items():
        vald = datetime.strptime(value, '%d-%b-%Y')
        today = date.today()

        if vald.month == today.month:
            if vald.day >= int(today.day) - 2:
                pass
            else:
                del l_dictionary[f'{key}']
        else:
            del l_dictionary[f'{key}']

        pass

    final_titles = list(t_dictionary.keys())
    final_links = list(l_dictionary.keys())

    final_titles.pop(0)
    final_links.pop(0)

    print(f"{thing}'s news scraped successfully.")

    # Pause to avoid IP blocking
    time.sleep(3)

    # Slicing list according to user preference

    n_links = final_links[:int(count)]
    n_titles = final_titles[:int(count)]

    return n_titles, n_links


