#!/usr/bin/python

import os; os.system('clear')

try:
   from bs4 import BeautifulSoup
   import requests
   from re import search, findall, sub
   from urllib import unquote
   from HTMLParser import HTMLParser
   from urlparse import urlparse
   import mechanize
   import datetime
   import argparse
   import sys
   import urllib
except ImportError as e:
   print("[!] '"+str(e)+"' Please Install !")
   print("[!] Use 'pip install NameModule' To Install This Module !")
   exit(1)

versi = "1.2"

print("""
    :::       ::: ::::::::::: :::::::::: 
   :+:       :+:     :+:     :+:         
  +:+       +:+     +:+     +:+          
 +#+  +:+  +#+     +#+     :#::+::#      
+#+ +#+#+ +#+     +#+     +#+            
#+#+# #+#+#      #+#     #+#             
###   ###       ###     ###  Web Toolkit Framework

""")
def info():
    print """[*] WTF V """+versi+""" ( Web Toolkit Framework )
[*] Devloped By ./Xi4u7
[*] Greetz : AndroSec1337 Cyber Team & LAmongan Xploiters
[*] Avilable Bug ? Contact Here : androsec1337@gmail.com

Externals Commamd :

  -a,  --admin     =  Admin Panel Finder
  -w,  --whois     =  WhoIs Lookup Scan
  -g,  --geoip     =  GeoIP Lookup Scan
  -s,  --sql       =  SQL Methode Scanner
  -p,  --port      =  Port Open Scanner
  -sn, --subnet    =  Subnet Calculation
  -ns. --nslookup  =  DNS Lookup Scanner

Example :

  python wtf.py http://target.com/ -a
  python wtf.py http://target.com/?id= -s
  python wtf.py www.target.com -w -g -p -sn -ns
"""

br = mechanize.Browser() # Jangan Di Ubah Y Kontol >:(

try:
   KONTOL = sys.argv[1]
except:
   info()
   exit()

def adm_ngentod(link):
 f = open("files/admin.txt","r");
 asu = link
 while True:
  sub_link = f.readline().replace("\n", "")
  if not sub_link:
   break
  anuuu = asu+"/"+sub_link
  wasem = urllib.urlopen(anuuu).getcode()
  if wasem == 200:
   print("[+] "+str(anuuu)+" Found ")
  else:
   print("[-] "+str(anuuu)+" Not Found")


def whois(ip_trgt):
    web = "http://api.hackertarget.com/whois/?q="+ip_trgt
    result = br.open(web).read()
    print result

def geoip(ip_trgt):
    web = "http://api.hackertarget.com/geoip/?q="+ip_trgt
    result = br.open(web).read()
    print result

def dnslookup(ip_trgt):
    web = "http://api.hackertarget.com/dnslookup/?q="+ip_trgt
    result = br.open(web).read()
    print result

def subnetcal(ip_trgt):
    web = "http://api.hackertarget.com/subnetcalc/?q="+ip_trgt
    result = br.open(web).read()
    print result

def nmap_port(ip_addr):
    port = "http://api.hackertarget.com/nmap/?q=" + ip_addr
    result = br.open(port).read()
    result = sub(r'Starting[^<]*\)\.', '', result)
    result = sub(r'Service[^<]*seconds', '', result)
    result = os.linesep.join([s for s in result.splitlines() if s])
    print("--------- GETING RESULT ---------\n\n")
    print result
    print("\n\n---------- GETING DONE ----------")


def sqlmap_onlen(url):
    print "[!] Keep Calm I Am Use SQLmap Online Tools :)"
    sqli = br.open('https://suip.biz/?act=sqlmap').read()
    br.select_form(nr=0)
    br.form['url'] = url
    req = br.submit()
    result = req.read()
    match = search(r"---(?s).*---", result)
    if match:
        print '[+] One or more parameters are vulnerable to SQL injection'
        option = raw_input('[?] Would you like to see the whole report? [Y/n] ').lower()
        if option == 'n':
            pass
        elif option == 'N':
            pass
        else:
            print"-"*40
            print match.group().split('---')[1][:-3]
            print"-"*40
    else:
        print '[-] Parameter Not Found To SQL Inject Vulnerable !'

target = KONTOL

for arg in sys.argv:
 if (arg == '-p' or arg == '--port'):
  nmap_port(target)
 if (arg == '-a' or arg == '--admin'):
  adm_ngentod(target)
 if (arg == '-w' or arg == '--whois'):
  whois(target)
 if (arg == '-g' or arg == '--geoip'):
  geoip(target)
 if (arg == '-s' or arg == '--sql'):
  sqlmap_onlen(target)
 if (arg == '-sn' or arg == '--subnet'):
  subnetcal(target)
 if (arg == '-ns' or arg == '--nslookup'):
  dnslookup(target)
