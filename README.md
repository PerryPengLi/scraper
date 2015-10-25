# scraper
Perry's Python Scraper for CBOE daily trading volume.

A Python program uses selenium + BeautifulSoup to parse the following page:
    http://www.cboe.com/data/mktstat.aspx
    
The page let you Select a date to get CBOE historical trading data, mannualy input date is boring.  

So this program let you define a start and end date, use selenium to  send each date into the page to get that day's 
trading volume, and then use BeautifulSoup to parse the data and write to a csv file.
