import json
import random
import time

def scrape_amazon_mock():
    print('Initializing browser fingerprint...')
    time.sleep(0.5)
    print('Scraping mock BSR data...')
    return {'asin': 'B08XXXX', 'est_sales': random.randint(150, 1200), 'trend': 'upward'}

if __name__ == '__main__':
    print(json.dumps(scrape_amazon_mock(), indent=2))