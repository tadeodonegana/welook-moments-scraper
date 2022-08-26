from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# PATH constants
IMG_FOLDER_PATH = "images/"
POAP_FOLDER_PATH = "poap-img/"

# Function to download images from the scraped urls
def download_image(url, name, path):
    r = requests.get(url=url)
    path= path + name + ".png"

    if r.status_code == 200:
        with open(path, 'wb') as f:
            f.write(r.content)

# Function that scrapes the images from moment_path and download them into images folder
def scrape_and_download_images(moment_path):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    # URL with the desired moments page
    driver.get(moment_path)

    # Wait 10 seconds for the site to load.
    time.sleep(10)  

    # Load all the moments clicking the 'Load More' button until there's no more moments
    while True:
        try:
            loadMoreButton = driver.find_element("xpath","/html/body/div/div/div[2]/div[3]/div/button")
            time.sleep(2)
            loadMoreButton.click()
            time.sleep(5)
        except Exception as e:
            break

    # Beautiful Soup instance
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find and download the POAP image
    poap_img = soup.findAll('div', {"flex w-full min-w-[12.5rem] items-center justify-center self-center overflow-hidden rounded-lg bg-slate-700 p-6 lg:w-36 lg:bg-transparent lg:p-0"})
    download_image(poap_img[0].a.picture.source['srcset'], "poap_img", POAP_FOLDER_PATH)

    # Get a list with the divs of all the moments
    moments = soup.findAll('div', {"flex flex-col gap-2"})

    # Loop trough the moments and download the images to the images subfolder
    for i, moment in enumerate(moments):
        # Get the address of the picture creator
        address = moment.find("span", class_="truncate text-sm font-bold").text 
        download_image(moment.button.picture.source['srcset'], address+'-'+str(i), IMG_FOLDER_PATH)

    driver.close()