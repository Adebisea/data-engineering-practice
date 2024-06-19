import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'


def scrape_data(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    d_table = soup.find_all('tr')

    dict_table = {row.contents[1].text:row.contents[0].text  for row in d_table[3:-1]}


    csv_file_link = dict_table.get('2024-01-19 10:31  ')
    return csv_file_link


def download_data(url):
        data_url = scrape_data(url)
        if data_url != None:
            data_resp = requests.get(url+data_url)

            with open(data_url, 'wb') as f:
                f.write(data_resp.content)

            return data_url

def main(url):
    download_data(url)


if __name__ == "__main__":
    main(url)


