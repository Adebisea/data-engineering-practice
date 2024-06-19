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
        
def load_data(file):
    df = pd.read_csv(file)

    # convert column to numeric
    df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'], errors='coerce')

    # Get the highest HourlyDryBulbTemperature value
    Highest_HDBT_value = df['HourlyDryBulbTemperature'].max()

    # Query the DataFrame for all records with the highest HourlyDryBulbTemperature value
    Highest_HDBT_records = df[df['HourlyDryBulbTemperature'] == Highest_HDBT_value]
    print(Highest_HDBT_records)


def main(url):
    filename = download_data(url)
    if filename:
        load_data(filename)


if __name__ == "__main__":
    main(url)


