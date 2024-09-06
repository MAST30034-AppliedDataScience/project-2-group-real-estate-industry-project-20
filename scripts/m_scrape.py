import re
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from json import dump
import pandas as pd
import time

from collections import defaultdict
import urllib.request

# user packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from utilities import get_vic_subs, get_accessible_subs

# constants
BASE_URL = "https://www.domain.com.au"

# Get accessible Victoria suburbs
get_vic_subs('../australian-postcodes-2021-04-23.csv')
get_accessible_subs('../data/raw/suburb.txt')

'''
df = pd.read_csv('../data/raw/suburb_accessible.csv')

property_metadata = defaultdict(dict)

def scrape_suburb_data(sub):
    # begin code
    url_links = []

    # generate list of urls to visit
    for page in range(1, df.loc[df['suburb'] == sub, 'total_page'].values[0] + 1):
        url = BASE_URL + f"/rent/{sub}/?sort=price-desc&page={page}"
        #print(f"Visiting {url}")
        bs_object = BeautifulSoup(urlopen(Request(url, headers={'User-Agent':"PostmanRuntime/7.6.0"})), "lxml")
        try:
            # find the unordered list (ul) elements which are the results, then
            # find all href (a) tags that are from the base_url website.
            index_links = bs_object \
                .find(
                    "ul",
                    {"data-testid": "results"}
                ) \
                .findAll(
                    "a",
                    href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
                )

            for link in index_links:
                # if its a property address, add it to the list
                if 'address' in link['class']:
                    url_links.append(link['href'])
        except Exception as e:
            print(f"Issue with {url}: {e}")
    
    def scrape_features(property_url):
        bs_object = BeautifulSoup(urlopen(Request(property_url, headers={'User-Agent':"PostmanRuntime/7.6.0"})), "lxml")
        try: 
            # looks for the header class to get property name
            property_metadata[property_url]['name'] = bs_object \
                .find("h1", {"class": "css-164r41r"}) \
                .text

            # looks for the div containing a summary title for cost
            property_metadata[property_url]['cost_text'] = bs_object \
                .find("div", {"data-testid": "listing-details__summary-title"}) \
                .text

            # get rooms and parking
            rooms = bs_object \
                    .find("div", {"data-testid": "property-features"}) \
                    .findAll("span", {"data-testid": "property-features-text-container"})

            property_metadata[property_url]['rooms'] = [
                re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms
                if 'Bed' in feature.text or 'Bath' in feature.text
            ]
        
            
            # parking
            property_metadata[property_url]['parking'] = [
                re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in rooms
                if 'Parking' in feature.text
            ]
            
            # type
            property_metadata[property_url]['type'] = bs_object \
                .find("div", {"data-testid": "listing-summary-property-type"}) \
                .text
            
            # schools
            schools = bs_object.find_all("li", {"data-testid": "fe-co-school-catchment-school"})
            property_metadata[property_url]['schools'] = len(schools)
            print(len(schools))
                       
            # description
            property_metadata[property_url]['desc'] = re \
                .sub(r'<br\/>', '\n', str(bs_object.find("p"))) \
                .strip('</p>')
            
        except AttributeError:
            print(f"Issue with {property_url}")

    with ThreadPoolExecutor(max_workers=7) as executor:
        list(tqdm(executor.map(scrape_features, url_links), total=len(url_links), desc="Scraping Properties"))

subs = df['suburb'].tolist()

with ThreadPoolExecutor(max_workers=7) as executor:
        list(tqdm(executor.map(scrape_suburb_data, subs[:150]), total=len(subs[:150]), desc="Scraping Suburbs"))
        
time.sleep(10)

with ThreadPoolExecutor(max_workers=7) as executor:
        list(tqdm(executor.map(scrape_suburb_data, subs[150:300]), total=len(subs[150:300]), desc="Scraping Suburbs 2"))
  
time.sleep(10)  
        
with ThreadPoolExecutor(max_workers=7) as executor:
        list(tqdm(executor.map(scrape_suburb_data, subs[300:450]), total=len(subs[300:450]), desc="Scraping Suburbs 3"))

time.sleep(10)

with ThreadPoolExecutor(max_workers=7) as executor:
        list(tqdm(executor.map(scrape_suburb_data, subs[450:]), total=len(subs[450:]), desc="Scraping Suburbs 4"))


# output to json file in data/raw/
with open('../data/raw/current_rent_info.json', 'w') as f:
    dump(property_metadata, f)
    
'''