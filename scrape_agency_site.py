from string import ascii_lowercase


class ScrapeAgencies:
    
    def __init__(self):
        
        #create all urls with each letter in the alphabet
        root_url = 'https://www.usa.gov/federal-agencies/'
        for letter in ascii_lowercase:
            print root_url + letter
            
            
            
if __name__ == "__main__":
    scrape = ScrapeAgencies()
    