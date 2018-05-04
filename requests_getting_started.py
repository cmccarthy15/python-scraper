import requests
from bs4 import BeautifulSoup
### headers options found on stackoverflow to deal with encoding issues
headers = {'Accept-Encoding': 'identity'}
url = 'http://catalog.pomona.edu/content.php?catoid=24&navoid=4850'

r = requests.get(url)

## print all course names on that page
soup = BeautifulSoup(r.content)

for item in soup.find_all('a'):
  if item.parent.name == 'td':
    print(item.string)
