
import requests 
from bs4 import BeautifulSoup 
  
  
# Making a GET request 
r = requests.get('https://nihongoichiban.com/2011/04/30/complete-list-of-vocabulary-for-the-jlpt-n5/') 
  
# check status code for response received 
# success code - 200 
print(r) 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify()) 