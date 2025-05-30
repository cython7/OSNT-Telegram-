
# - @HAHAHA_DECOD
#2025-05-26
#ZAXOTEL MADE

import sys
import random
import logging
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
logging.basicConfig(filename="osint_error.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_random_user_agent():
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ]
    return random.choice(USER_AGENTS)

def search_info(query):
    query_encoded = quote_plus(query)
    headers = {'User -Agent': get_random_user_agent()}
    reveng_url = f'https://reveng.ee/search?q={query_encoded}&per_page=100'
    results = []

    try:
        reveng_response = requests.get(reveng_url, headers=headers)
        reveng_response.raise_for_status()
        soup = BeautifulSoup(reveng_response.text, 'html.parser')
        for link in set(a['href'] for a in soup.find_all('a', href=True) if 'entity' in a['href']):
            page_response = requests.get(f'https://reveng.ee{link}', headers=headers)
            page_response.raise_for_status()
            soup = BeautifulSoup(page_response.text, 'html.parser')
            entity = soup.find('div', class_='bg-body rounded shadow-sm p-3 mb-2 entity-info')
            if entity:
                result = {}
                name = entity.find('span', class_='entity-prop-value')
                if name:
                    result['Имя'] = name.get_text(strip=True)
                for row in entity.find_all('tr', class_='property-row'):
                    prop_name = row.find('td', class_='property-name').get_text(strip=True)
                    prop_value = row.find('td', class_='property-values').get_text(strip=True)
                    result[prop_name] = prop_value
                results.append(result)
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка запроса: {e}")
    except Exception as e:
        logging.error(f"Ошибка: {e}")
    
    return results

def main():
    while True:
        query = input("   Облачная база данных\n   Введите запрос (или '00' для выхода): ")
        if query.lower() == '00':
            break
        if query:
            print("   Выполняется поиск...")
            results = search_info(query)
            if results:
                print("   Результаты поиска:")
                for idx, result in enumerate(results, start=1):
                    print(f"{idx}. Имя: {result.get('Имя', 'Не указано')}")
                    for key, value in result.items():
                        if key != 'Имя':
                            print(f"   {key}: {value}")
            else:
                print("Нет результатов.")
        else:
            print("Введите запрос.")

if __name__ == "__main__":
    main()
