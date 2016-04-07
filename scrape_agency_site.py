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
    
    def check_urls(self, url):
        '''checks url to get corresponding file path for cache folder'''
    
        split_url = url.split('/')[-1]
        
        if split_url == 1:
            file_path = '../cache/index_pages/' + split_url + '_index.html'
        elif split_url > 1:
            file_path = '../cache/agency_pages/' + split_url + '_agency.html'
            
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
            html = response.text
            write_cache = open(file_path, 'wb')
            write_cache.write(html.encode('utf-8'))
            soup = BeautifulSoup(html, "html.parser")
            write_cache.close()
            
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
            print p_tag.text
            
            
        

            
        

 
    
    
    
    #scrape agency links 
    #Hit the agency links to scrape agency details
    #write information to csv
        
if __name__ == "__main__":
    
#FOR LOOP ITERATES THROUGH ONE LETTER
    for letter in range(0, len(letters), 26):
        scrape = ScrapeAgencies()
        index_url = scrape.create_urls(letters[letter])
        file_path = scrape.check_urls(index_url)
        soup = scrape.convert_to_soup(index_url, file_path)
        scrape.scrape_agency(index_url)





#         print index_url




#         agency_url = scrape.scrape_index(index_url)
#         scrape.scrape_agency(agency_url)
        




# FOR LOOP BELOW ITERATES THROUGH ALL LETTERS IN THE ALPHABET
#     for letter in letters:
#         scrape = ScrapeAgencies()
#         index_urls = scrape.create_urls(letter)
#         print index_urls