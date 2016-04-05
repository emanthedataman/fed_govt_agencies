from string import ascii_lowercase as letters
from bs4 import BeautifulSoup

import requests

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
    
    #convert site to soup
    def convert_to_soup(self, url):
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        return soup
        
    #scrape site
    def scrape_index(self, url):
        soup = self.convert_to_soup(url)
        
        #find the unordered list, within in that find all the a tags
        a_tags = soup.find('ul', {'class', 'one_column_bullet'}).findAll('a', {'class': 'url'})
        for a_tag in a_tags:
            agency_link = a_tag['href']
            agency_url = 'https://www.usa.gov' + agency_link
            return agency_url
            
            
    def scrape_agency(self, agency_url):
        soup = self.convert_to_soup(agency_url)
        div_agency = soup.find('div', {'class', 'col-md-9'})
        p_tags = div_agency.findAll('p')
        
        for p_tag in p_tags:
            print p_tag
            
            
        

            
        

 
    
    
    
    #scrape agency links 
    #Hit the agency links to scrape agency details
    #write information to csv
        
if __name__ == "__main__":
    
#FOR LOOP ITERATES THROUGH ONE LETTER
    for letter in range(0, len(letters), 26):
        scrape = ScrapeAgencies()
        index_url = scrape.create_urls(letters[letter])
        agency_url = scrape.scrape_index(index_url)
        scrape.scrape_agency(agency_url)
        




# FOR LOOP BELOW ITERATES THROUGH ALL LETTERS IN THE ALPHABET
#     for letter in letters:
#         scrape = ScrapeAgencies()
#         index_urls = scrape.create_urls(letter)
#         print index_urls