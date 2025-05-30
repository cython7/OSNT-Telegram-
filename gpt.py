
# - @HAHAHA_DECOD
#2025-05-26
#ZAXOTEL MADE

import g4f
import os
import pyfiglet
import xlrd
from openpyxl import load_workbook
from colorama import init, Fore, Style
from pystyle import *
import random
import time              
import requests
from fake_useragent import UserAgent
import subprocess
from colorama import Fore, Style
import colorama
def clear():
	os.system("clear")
main = """   Chat GPT
   '00'' - Выход"""
while True:
    print(Fore.BLUE + Style.BRIGHT + main)
    user_input = input("Введите ваш запрос: ")
    if user_input == "00":
        print("   Выход из программы...")
        os.system("python main.py")
        clear()
        break
    else:
        print("   Обработка...")
        response = g4f.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': user_input}]
             )
        print(response)