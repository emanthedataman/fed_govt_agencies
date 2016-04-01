from string import ascii_lowercase as letters

class ScrapeAgencies:

    def __init__(self):
        self.letter = letter  
        
    def create_urls(self, letter):
        root_url = 'https://www.usa.gov/federal-agencies/%s' % (self.letter)
        print root_url
        
        
if __name__ == "__main__":
    for letter in letters:
        scrape = ScrapeAgencies()
        scrape.create_urls(letter)