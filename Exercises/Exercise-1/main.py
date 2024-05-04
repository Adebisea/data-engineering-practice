import requests
import os
from urllib.parse import urlparse
from zipfile import ZipFile, BadZipFile

directory = 'downloads'
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def create_directory(directory):
    folder_path = os.path.join(os.getcwd(), directory)
    
    if os.path.exists(folder_path): #check if directory exists
        pass
    else:
        os.mkdir(folder_path) #create directory
        print('done')


def download_files(url,file_path):
        try:
            download_response = requests.get(url) #get file content
            with open(file_path,"wb") as f: #write content to local as file
                f.write(download_response.content)
                print('downloaded')
        except Exception as e: #catch all errors
            print(url +':'+ e)

def download_all_files(download_uris,directory):
    for url in download_uris:
        _,filename = urlparse(url).path.split('/') #get filename from url
        file_path = os.path.join(directory, filename)
        download_files(url,file_path)






    

def main(download_uris,directory):
    create_directory(directory)
    download_all_files(download_uris,directory)
    
    


if __name__ == "__main__":
    main(download_uris,directory)