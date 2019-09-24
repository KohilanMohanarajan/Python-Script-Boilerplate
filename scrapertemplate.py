from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()

scraperUrl = 

# scrape over months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

r = session.get(scraperUrl)
soup = BeautifulSoup(r.content, 'html.parser')

# For a list of BS4 commands, check: https://www.crummy.com/software/BeautifulSoup/bs4/doc/