# -*- coding: utf-8 -*-
import requests
from colorama import Fore,Style,Back
def hackertarget_api(hedef):
    istek_url = ("https://api.hackertarget.com/reverseiplookup/?q=")
    
    url = istek_url + hedef
    istek =requests.get(url)
    return istek.text
print("merhaba ")
hedef = input("ip / domain: ")
print("\n")
reverseiplookup = hackertarget_api(hedef)
print(Fore.GREEN)
print(reverseiplookup)
print(Style.RESET_ALL)
print("\n")
print("--------------------REVERSEİP TARAMASI BİTTİ-----------------------")






    