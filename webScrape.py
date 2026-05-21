import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table and extract all rows
table = soup.find('table')
rows = []
for tr in table.find_all('tr'):
    cells = [td.text.strip() for td in tr.find_all(['td', 'th'])]
    rows.append(cells)

# Create a DataFrame and save to CSV
df = pd.DataFrame(rows[1:], columns=rows[0]) # Assuming first row is header
df.to_csv('output_data.csv', index=False)

