import os
import csv
import requests
from  bs4 import BeautifulSoup


def file_path(folder_name: str, file_name: str) -> str:
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    file_path = os.path.join(folder_name, file_name)
    return file_path


def save_to_csv(data: list, file: str) -> None:
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Country', 'INR', 'inv_INR'])
        writer.writerows(data)

    print(f"Data saved to {file}")


def data_from_url_to_csv(file: str) -> None:
    url = 'https://www.x-rates.com/table/?from=INR&amount=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'tablesorter ratesTable'})
    rows = table.find_all('tr')

    data = [[str.strip(tag.text) for tag in row.find_all('td')][:3] for row in rows
            if row.find_all('td') and len(row.find_all('td')) >= 3]

    data = [[country, float(inr), float(inverse_inr)] for country, inr, inverse_inr in data]

    save_to_csv(data, file)


if __name__ == "__main__":
    folder_name = 'data'
    file_name = "current_data.csv"
    file = file_path(folder_name, file_name)
    data_from_url_to_csv(file)
