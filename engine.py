import pandas as pd
from scrapper import scrape
from clean_data import clean
import multiprocessing
from multiprocessing.dummy import Pool

def get_queries():
    num_que = int(input("Enter the number of queries : "))
    url_list = []
    for i in range(num_que):
        print(f'Query_{i+1}')
        brand = input('Enter the Brand Name :').upper()
        body_type = input('Enter the Body Type :').lower()
        fuel = input('Enter the Fuel Type :').lower()
        min_price = int(input('Enter the min. price :'))
        max_price = int(input('Enter the max. price :'))
        min_range = int(input('Enter the min. running :'))
        max_range = int(input('Enter the max. running :'))

        url = f"https://www.cars24.com/buy-used-car?listingPrice-range={min_price}-{max_price}&carName={brand}&odometerReading-range={min_range}-{max_range}&fuelType={fuel}&bodyType={body_type}&sort=P&storeCityId=2"
        url_list.append(url)

    print('Scraping Started....')
    return url_list

if __name__ == '__main__':
    url = get_queries()
    with multiprocessing.Pool(processes=3) as pool:
        pool.map(scrape,url)
    clean()
    print('Scrapping Completed')  