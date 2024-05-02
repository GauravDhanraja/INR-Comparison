
import os
import csv
import requests
import pandas as pd
import matplotlib.pyplot as plt
from  bs4 import BeautifulSoup

file = 'currency_data.csv'

def save_to_csv(data: list, file: str) -> None:

    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Country', 'INR', 'inv_INR'])
        writer.writerows(data)

    print(f"Data saved to {file}")

def get_from_csv(file: str) -> list: 
    
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data


def data_from_url_to_csv(file: str) -> None:
    url = 'https://www.x-rates.com/table/?from=INR&amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'tablesorter ratesTable'})
    rows = table.find_all('tr')

    # Extract data from table rows
    data = [row_data[:3] for row_data in [[str.strip(tag.text) for tag in row.find_all('td')] for row in rows
          if row.find_all('td') and len(row.find_all('td')) >= 3]]

    data = [[country, float(inr), float(inverse_inr)] for country, inr, inverse_inr in data if float(inr) <= 150]

    save_to_csv(data, file)


if __name__ == "__main__":
    data_from_url_to_csv(file)
