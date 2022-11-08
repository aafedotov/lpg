import requests
from bs4 import BeautifulSoup


def get_benz_price():
    """Парсим текущую цену бензина."""
    url = 'https://fuelprice.ru/azs16708'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    prices = soup.find_all('span', class_='text-success font-weight-bold')
    dates = soup.find_all('small', class_='text-')
    price = {'price': prices[1].text, 'date': dates[0].text}
    return price


print(get_benz_price())
