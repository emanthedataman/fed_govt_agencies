from string import ascii_lowercase as letters
import requests

class ScrapeAgencies:

    def __init__(self):
        self.letter = letter  
        
        self.min_sleep_sec = 0.5
        self.max_sleep_sec = 2.5
        
    def create_urls(self, letter):
        urls_list = []
        root_url = 'https://www.usa.gov/federal-agencies/%s' % (self.letter)
        return root_url
        
if __name__ == "__main__":
    for letter in letters:
        scrape = ScrapeAgencies()
        index_urls = scrape.create_urls(letter)
        print index_urls