import argparse
import img_scraper

parser = argparse.ArgumentParser(description='Scrape Welook Moments')

parser.add_argument('-g', '--generate', type=str, help='Moment URL')

args = parser.parse_args()

print('Scraping images from ' + args.generate + ' ...')
# Scrape Images from Welook's website
img_scraper.scrape_and_download_images(args.generate)
print('Images ready! Check them out at /images folder.')