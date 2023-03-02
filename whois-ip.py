from colorama import *
import requests
import json
import os
import time

init()

# Text
plus = f'[{Fore.GREEN}+{Fore.WHITE}]'
minus = f'[{Fore.LIGHTRED_EX}-{Fore.WHITE}]'
wait = f'[{Fore.LIGHTGREEN_EX}>>{Fore.WHITE}]'
error = f'[{Fore.RED}!{Fore.WHITE}]'


def banner():
    os.system("cls")
    print(f"[{Fore.GREEN}+{Fore.WHITE}] IP Scanner")
    print("")


api_url = "http://ip-api.com/json/"
param = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {
    "fields": param
}


def IpScrap(ip=""):
    res = requests.get(api_url+ip, data=data)
    api_json_res = json.loads(res.content)
    return api_json_res


def initialize():
    if __name__ == '__main__':
        banner()
    print(f'{wait} IP: ', end="")
    ip = input()
    par = param.split(",")
    for x in par:
        print(f'{plus} {x.upper()}', ':', end=" ")
        try:
            print(IpScrap(ip)[x])
        except:
            print("")
            print(f'{error} Ocurrió un error, intentelo de nuevo')
            time.sleep(2)
            initialize()
    print(f'{wait} Scan completado, presione enter.')
    x = input()
    if (x == ""):
        initialize()
    else:
        initialize()


try:
    initialize()
except KeyboardInterrupt:
    print("")
    print(f'[{Fore.GREEN}+{Fore.WHITE}] Gracias por usar el IP Scanner.')
