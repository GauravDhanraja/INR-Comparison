
import os
import csv
import requests
import pandas as pd
import matplotlib.pyplot as plt
from  bs4 import BeautifulSoup


def absolute_path(file_path: str) -> str:
    base_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_path, file_path)
    return file_path

def get_from_csv(file_path: str) -> list: 
    file_path = absolute_path(file_path)
    
    # Read the data from CSV file
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def save_to_csv(data: str, file_path: str) -> None:
    file_path = absolute_path(file_path)

    # Write the data to the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Country', '1.00 INR', 'Inv 1.00 INR'])
        writer.writerows(data)

    print(f"Data saved to {file_path}")

# Get data from web page and append it to our CSV file
def data_from_url_to_csv(file_path: str) -> None:
    url = 'https://www.x-rates.com/table/?from=INR&amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'tablesorter ratesTable'})
    rows = table.find_all('tr')

    # Extract data from table rows
    data = [[str.strip(tag.text) for tag in row.find_all('td')[:3]] for row in rows
            if row.find_all('td') and len(row.find_all('td')) >= 3]
    data = [[country, inr, inverse_inr] for country, inr, inverse_inr in data if float(inr) <= 150]

    save_to_csv(data, file_path)


if __name__ == '__main__':
    
    file_path = 'currency_data.csv'
    
    data_from_url_to_csv(file_path)
    data = pd.read_csv('currency_data.csv')

    data['Currency Strength'] = 1 / data['1.00 INR']

    plt.figure(figsize=(12, 8))
    plt.barh(data['Country'], data['Currency Strength'], color='green', alpha=0.7)

    plt.xlabel('Currency Strength (relative to 1.00 INR)')
    plt.title('Currency Strength Relative to INR')
    plt.gca().invert_yaxis()
    plt.tight_layout()

    plt.show()