# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:59:58 2020

@author: TimK
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import time



class ZooplaScraper:
    results = []
    
    def fetch(self, url): # method to acess URL 
        print('HTTP GET request to URL: %s' % url, end ='')
        response = requests.get(url)
        print('| Status code: %s' % response.status_code)
        return response
    
    def parse(self, html): # taking the data from the HTML and restructing for a CSV file 
        content = BeautifulSoup(html,'lxml')
        
        cards = content.findAll('div', {'class':'listing-results-wrapper'})
        
        try:
            phone = card.find('span', {'class':'agent_phone'}).text.strip()
        except:
            phone = 'N/A'
        
        for card in cards:
            self.results.append ({
                'title': card.find('a', {'style': 'text-decoration:underline;'}).text,
                'address':card.find('a', {'class':'listing-results-address'}).text,
                'description': card.find('p').text.strip(),
                'price': card.find('a', {'class':'listing-results-price text-price'}).text.strip().strip('\u00a3'),
                'phone': phone,
                'closest_station': card.find('li', {'class':'clearfix'}).text.strip().strip('\n'),
                'listed_on': card.find('p', {'class':'top-half listing-results-marketed'}).text.strip().split('by')[0].split(),
                'image': card.find('a', {'class': 'photo-hover'}).find('img')['data-src']
            })
        
    def to_csv(self): # write webpage data to csv file
        with open('C:/Users/TimK/Documents/ds_zoop_proj/zoopla.csv', 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()
            
            for row in self.results:
                writer.writerow(row)
            
            print('Stored results to "zoopla.csv"') # debugging info 
            
            
    def run(self):
        # removing data from a webpage an putting on another web page.
        for page in range(1, 38):
            url = 'https://www.zoopla.co.uk/for-sale/houses/central-london/?beds_min=3&price_max=325000&property_sub_type=detached&property_sub_type=semi_detached&feature=has_garden&feature=has_parking_garage&identifier=central-london&property_type=houses&q=Central%20London&is_shared_ownership=false&is_retirement_home=false&search_source=refine&radius=40&pn='    
            url += str(page)
            res = self.fetch(url)
            self.parse(res.text)
            time.sleep(2)
        
        self.to_csv()
    
if __name__ == '__main__': # driver to run scraper 
    scraper = ZooplaScraper()
    scraper.run()