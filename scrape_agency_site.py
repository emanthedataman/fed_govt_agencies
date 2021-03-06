from string import ascii_lowercase as letters
from bs4 import BeautifulSoup
from urlparse import urlparse
from time import sleep

import requests
import random

class ScrapeAgencies:

    def __init__(self):
#         self.letter = letter  
        
        self.min_sleep_sec = 0.5
        self.max_sleep_sec = 2.5



    #create urls to access all index pages    
    def create_urls(self, letter):
        urls_list = []
# #         root_url = 'https://www.usa.gov/federal-agencies/%s' % (self.letter)
        root_url = 'https://www.usa.gov/federal-agencies/%s' % (letter)
        return root_url
    
    def check_urls(self, url):
        '''checks url to get corresponding file path for cache folder'''
        
        
        parsed_url = urlparse(url)
        cache_file_name = parsed_url.path[1:].replace('/', '_')

        if len(parsed_url.path) == 19:
            file_path = '../cache/index_pages/' + cache_file_name + '.html'
        elif len(parsed_url.path) > 19:       
            file_path = '../cache/agency_pages/' + cache_file_name + '.html'
            
        return file_path

    
    #convert site to soup
    def convert_to_soup(self, url, file_path):

        #first try to read the file
        try:
            print 'Reading file...' + file_path
            read_cache = open(file_path, 'rb')
            soup = BeautifulSoup(read_cache, "html.parser")
            read_cache.close()

        #if that doesnt work, write the file
        except IOError:
            print 'Writing file...' + file_path
            
            response = requests.get(url)
            sleep(random.uniform(self.min_sleep_sec, self.max_sleep_sec))
            
            html = response.text
            write_cache = open(file_path, 'wb')
            write_cache.write(html.encode('utf-8'))
            soup = BeautifulSoup(html, "html.parser")
            write_cache.close()
            
        return soup

    #scrape site
    def scrape_index(self, soup):
        
        try:        
            #find the unordered list, within in that find all the a tags
            a_tags = soup.find('ul', {'class', 'one_column_bullet'}).findAll('a', {'class': 'url'})
            for a_tag in a_tags:
                agency_link = a_tag['href']
                agency_url = 'https://www.usa.gov' + agency_link
                return agency_url

        except AttributeError:
            return None
            
            
            
            
    def scrape_agency(self, soup):
        div_agency = soup.find('div', {'class', 'col-md-9'})
        
        
        print div_agency.find('h1').text
            
        

            
        

 
    
    
    
    #scrape agency links 
    #Hit the agency links to scrape agency details
    #write information to csv
        
if __name__ == "__main__":
    
# #FOR LOOP ITERATES THROUGH ONE LETTER
#     for letter in range(0, len(letters), 26):
#         scrape = ScrapeAgencies()
#         index_url = scrape.create_urls(letters[letter])
#         file_path = scrape.check_urls(index_url)
#         
#         scrape.convert_to_soup(index_url, file_path)
        

    index_links = []

#FOR LOOP BELOW ITERATES THROUGH ALL LETTERS IN THE ALPHABET
    for letter in letters:

        scrape = ScrapeAgencies()
        index_urls = scrape.create_urls(letter)
        file_path = scrape.check_urls(index_urls)
        
        soup = scrape.convert_to_soup(index_urls, file_path)
        links = scrape.scrape_index(soup)
        if links:    
            index_links.append(links)
        
    for index_link in index_links:
        file_path = scrape.check_urls(index_link)
        soup = scrape.convert_to_soup(index_link, file_path)
        scrape.scrape_agency(soup)
        
        
        
        