from string import ascii_lowercase as letters


class ScrapeAgencies:
    
    def __init__(self, letter):
        self.letter = letter

        
    #create all urls with each letter in the alphabet
    def create_urls(self, letter):
        root_url = 'https://www.usa.gov/federal-agencies/%s' % (self.letter)
        return root_url
        
            
            
            
if __name__ == "__main__":
    
    for letter in letters:
    
        scrape = ScrapeAgencies(letter)
        
    