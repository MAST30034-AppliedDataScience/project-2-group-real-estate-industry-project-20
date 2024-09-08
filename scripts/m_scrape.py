import re
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from json import dump
import pandas as pd
import time
import json
from collections import defaultdict
import urllib.request

# user packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from utilities import get_vic_subs, get_accessible_subs

# constants
BASE_URL = "https://www.domain.com.au"

df = pd.read_csv('./data/raw/suburb_accessible.csv')

property_metadata = defaultdict(dict)

def scrape_suburb_data(sub):
    url_links = []

    for page in range(1, df.loc[df['suburb'] == sub, 'total_page'].values[0] + 1):
        url = BASE_URL + f"/rent/{sub}/?ssubs=0&sort=price-desc&page={page}"
        try:
            bs_object = BeautifulSoup(urlopen(Request(url, headers={'User-Agent':"PostmanRuntime/7.6.0"})), "lxml")
            index_links = bs_object.find("ul", {"data-testid": "results"}) \
                .findAll("a", href=re.compile(f"{BASE_URL}/*"))

            for link in index_links:
                if 'address' in link['class']:
                    url_links.append(link['href'])
        except urllib.error.HTTPError as e:
            if e.code == 500:
                print(f"Server Error (500) with {url}")
            else:
                print(f"HTTP Error {e.code} with {url}")
        except urllib.error.URLError as e:
            print(f"URL Error with {url}: {e.reason}")
        except Exception as e:
            print(f"General issue with {url}: {e}")

    def scrape_features(property_url):
        try:
            bs_object = BeautifulSoup(urlopen(Request(property_url, headers={'User-Agent': "PostmanRuntime/7.6.0"})), "lxml")
            property_metadata[property_url]['name'] = bs_object.find("h1", {"class": "css-164r41r"}).text

            property_metadata[property_url]['cost_text'] = bs_object.find("div", {"data-testid": "listing-details__summary-title"}).text

            rooms = bs_object.find("div", {"data-testid": "property-features"}) \
                .findAll("span", {"data-testid": "property-features-text-container"})

            property_metadata[property_url]['rooms'] = [
                re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms if 'Bed' in feature.text or 'Bath' in feature.text
            ]

            property_metadata[property_url]['parking'] = [
                re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in rooms if 'Parking' in feature.text
            ]

            property_metadata[property_url]['type'] = bs_object.find("div", {"data-testid": "listing-summary-property-type"}).text

            script_tag = bs_object.find('script', {'id': '__NEXT_DATA__'})

            if script_tag:
                json_content = script_tag.string.strip()
                data = json.loads(json_content)

                schools = data.get('props', {}).get('pageProps', {}).get('componentProps', {}).get('schoolCatchment', {}).get('schools', [])
                num_schools = len(schools)
                property_metadata[property_url]['schools'] = num_schools

            property_metadata[property_url]['desc'] = re.sub(r'<br\/>', '\n', str(bs_object.find("p"))).strip('</p>')

        except urllib.error.HTTPError as e:
            if e.code == 500:
                print(f"Server Error (500) with {property_url}")
            else:
                print(f"HTTP Error {e.code} with {property_url}")
        except urllib.error.URLError as e:
            print(f"URL Error with {property_url}: {e.reason}")
        except AttributeError as e:
            print(f"Attribute Error with {property_url}: {e}")
        except Exception as e:
            print(f"General issue with {property_url}: {e}")

    with ThreadPoolExecutor(max_workers=5) as executor:
        list(tqdm(executor.map(scrape_features, url_links), total=len(url_links), desc="Scraping Properties"))

subs = df['suburb'].tolist()

with ThreadPoolExecutor(max_workers=5) as executor:
    list(tqdm(executor.map(scrape_suburb_data, subs), total=len(subs), desc="Scraping Suburbs"))

# Output to JSON file in data/raw/
with open('./data/raw/current_rent_info.json', 'w') as f:
    dump(property_metadata, f)
