
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy
from  bs4 import BeautifulSoup


def absolute_path(file_path):
    base_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_path, file_path)
    return file_path

def get_from_csv():
    file_path = absolute_path(file_path)
    
    # Read the data from CSV file
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def save_to_csv(data, file_path):
    file_path = absolute_path(file_path)

    # Write the data to the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Country', '1.00 USD', 'Inv 1.00 USD'])
        writer.writerows(data)

    print(f"Data saved to {file_path}")

# Get data from web page and append it to our CSV file
def data_from_url_to_csv(file_path):
    url = 'https://x-rates.com/table/?from=USD&amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'tablesorter ratesTable'})
    rows = table.find_all('tr')

    # Extract data from table rows
    data = []
    for row in rows:
        cells = row.find_all('td')
        if cells:
            country = cells[0].text.strip()
            usd = cells[1].text.strip()
            inverse_usd = cells[2].text.strip()
            data.append([country, usd, inverse_usd])

    # Save data to CSV
    save_to_csv(data, file_path)


if ('__name__') == ('__name__'):
    file_path = 'currency_data.csv'
    data_from_url_to_csv(file_path)
