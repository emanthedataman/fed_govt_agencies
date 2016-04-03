from string import ascii_lowercase as letters
import requests

class ScrapeAgencies:

    def __init__(self):
        self.letter = letter  
        
        self.min_sleep_sec = 0.5
        self.max_sleep_sec = 2.5

    #create urls to access all index pages    
    def create_urls(self, letter):
        urls_list = []
#         root_url = 'https://www.usa.gov/federal-agencies/%s' % (self.letter)
        root_url = 'https://www.usa.gov/federal-agencies/%s' % (letter)
        return root_url
        
    #requests pages
    #scrape agency links 
    #Hit the agency links to scrape agency details
    #write information to csv
        
if __name__ == "__main__":
    
#FOR LOOP ITERATES THROUGH ONE LETTER
    for letter in range(0, len(letters), 26):
        scrape = ScrapeAgencies()
        index_url = scrape.create_urls(letters[letter])
        print index_url




# FOR LOOP BELOW ITERATES THROUGH ALL LETTERS IN THE ALPHABET
#     for letter in letters:
#         scrape = ScrapeAgencies()
#         index_urls = scrape.create_urls(letter)
#         print index_urls