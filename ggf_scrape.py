import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = "https://www.ggf.org.uk/members/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with member information
table = soup.find('table', class_='ggfTable')

# Create a list to hold the information
member_info = []

# Loop through each row in the table and extract the information
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) == 3:
        member_name = columns[0].get_text(strip=True)
        member_address = columns[1].get_text(strip=True)
        member_phone = columns[2].get_text(strip=True)
        member_info.append([member_name, member_address, member_phone])

# Save the information in a CSV file
with open('ggf_members.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(member_info)
