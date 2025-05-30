
# - @HAHAHA_DECOD
#2025-05-26
#ZAXOTEL MADE

from colorama import Fore , Style , init 
import requests 
import json
import urllib.request 
import os 
from pystyle import System

def gei_ip(ip='127.0.0.1'):
    try:
        init()
        ip = input(Fore.BLUE + Style.BRIGHT + '   Введите ip-адрес: ')
        print('')
        po = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(Fore.BLUE + Style.BRIGHT + 'Точность	50 км' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT +  f'ip Adress: {ip}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + f'ip ищите: {ip}' + Style.RESET_ALL)
        print(Fore.BLUE +Style.BRIGHT +  f'Страна: {po.get("country")}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + f'Код страны: {po.get("countryCode")}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + f'Регион: {po.get("region")}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + f'Название региона: {po.get("regionName")}' + Style.RESET_ALL)
        print(Fore.BLUE +Style.BRIGHT + f'Город: {po.get("city")}' + Style.RESET_ALL)
        print(Fore.BLUE +Style.BRIGHT + f'Почтовый индекс: {po.get("zip")}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT +f'Широта: {po.get("lat")}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT +f'Долгота: {po.get("lon")}' + Style.RESET_ALL)
        print(Fore.BLUE +Style.BRIGHT + f'Кординаты: {po.get("lat")},{po.get("lon")}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT +f'Часовой пояс: {po.get("timezone")}' + Style.RESET_ALL)
        print(Fore.BLUE +Style.BRIGHT + f'Провайдер: {po.get("isp")}' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT +f'Организация: {po.get("org")}' + Style.RESET_ALL)
        print(Fore.BLUE +Style.BRIGHT + f'as: {po.get("as")}' + Style.RESET_ALL)
        print(Fore.BLUE +Style.BRIGHT + f'Ссылка Google Maps: https://www.google.com/maps?q={po.get("lat")},{po.get("lon")}' + Style.RESET_ALL)
        print('')
        input(Fore.BLUE + Style.BRIGHT +"   нажмите ENTER для завершения.")
              
    except requests.exceptions.ConnectionError:
        print(Fore.BLUE +Style.BRIGHT + '   Проверьте своё подключение к интернету!')
        input(Fore.BLUE+ Style.BRIGHT + '   ENTER')
if __name__ == '__main__':
    gei_ip()