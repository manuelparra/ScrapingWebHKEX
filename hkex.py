#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @description: this program parser the url
    https://www.hkex.com.hk/eng/stat/smstat/dayquot/d181204e.htm
    and convert the context in a CSV File
    @author: Manuel Parra
    @date: 20/01/19
    @modified: 28/01/19
"""

import urllib.request, urllib.parse, urllib.error
import nettest
import ssl
import sys
import csv

# variable for check data
checkpoint = '----------------------------------------------------------' \
             '---------------------'

# test our Internet connection
print("Testing the Internet connection, plase wait!")
nt = nettest.chargetest(['8.8.8.8', '8.8.4.4'])
if not nt.isnetup():
    print("Error, your Internet connection is down!")
    exit()

print("The Internet connection is ok!")

# ignore SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# put the URL
url = "https://www.hkex.com.hk/eng/stat/smstat/dayquot/d181204e.htm"

# get data
try:
    data = urllib.request.urlopen(url, context=ctx)
except Exception as err:
    print("Error to retrieve the URL", err)
    exit()

counttab = 0
newline = '\r\n'
info = list()
endline = False

for line in data:
    text = line.decode('utf-8')
    if text.find(checkpoint) != -1:
        if counttab == 3:
            with open('hkex/10_MOST_ACTIVES_(DOLLARS).csv', 'w') as file:
                write = csv.writer(file)
                write.writerows(info)
                print('* 14% retrieved and csv file created')
            info = []
        elif counttab == 4:
            with open('hkex/10_MOST_ACTIVES_(SHARES).csv', 'w') as file:
                write = csv.writer(file)
                write.writerows(info)
                print('* 28% retrieved and csv file created')
            info = []
        elif counttab == 5:
            with open('hkex/QUOTATIONS.csv', 'w') as file:
                write = csv.writer(file)
                write.writerows(info)
                print('* 44% retrieved and csv file created')
            info = []
        elif counttab == 9:
            with open('hkex/SALES_RECORDS_FOR_ALL_STOCKS.csv', 'w') as file:
                write = csv.writer(file)
                write.writerows(info)
                print('* 58% retrieved and csv file created')
            info = []
        elif counttab == 12:
            with open('hkex/SALES_RECORDS_OVER_500000_DOLLARS.csv',
                      'w') as file:
                write = csv.writer(file)
                write.writerows(info)
                print('* 72% retrieved and csv file created')
            info = []
        elif counttab == 15:
            with open('hkex/AMENDMENT_RECORDS_FOR_TRADE.csv', 'w') as file:
                write = csv.writer(file)
                write.writerows(info)
                print('* 86% retrieved and csv file created')
            info = []
        elif counttab == 20:
            with open('hkex/SHORT_SELLING_TURNOVER_DAILY_REPORT.csv',
                      'w') as file:
                write = csv.writer(file)
                write.writerows(info)
                print('* 100% retrieved')
            info = []
            print("It's done!")
            exit() # finish for now
        counttab += 1
        currentline = 0

    if counttab == 3:
        currentline += 1
        if text == newline or currentline == 1 or currentline == 2 : continue
        CODE = text[0:6].strip()
        NAME_OF_STOCK = text[6:22].strip()
        CUR = text[22:25].strip()
        TURNOVER = text[25:45].strip().replace(',', '').replace('.', ',')
        SHARES_TRADED = text[45:64].strip().replace(',', '').replace('.', ',')
        HIGH = text[64:72].strip().replace(',', '').replace('.', ',')
        LOW = text[72:81].strip().replace(',', '').replace('.', ',')
        ROW = [CODE, NAME_OF_STOCK, CUR, TURNOVER, SHARES_TRADED, HIGH, LOW]
        info.append(ROW)

    if counttab == 4:
        currentline += 1
        if text == newline or currentline == 1 or currentline == 2 : continue
        CODE = text[0:6].strip()
        NAME_OF_STOCK = text[6:22].strip()
        CUR = text[22:25].strip()
        SHARES_TRADED = text[25:43].strip().replace(',', '').replace('.', ',')
        TURNOVER = text[43:64].strip().replace(',', '').replace('.', ',')
        HIGH = text[64:73].strip().replace(',', '').replace('.', ',')
        LOW = text[73:82].strip().replace(',', '').replace('.', ',')
        ROW = [CODE, NAME_OF_STOCK, CUR, SHARES_TRADED, TURNOVER, HIGH, LOW]
        info.append(ROW)

    if counttab == 5:
        currentline += 1
        if text == newline or currentline == 1 or currentline == 2: continue
        text = text.replace('amp;', '').replace('PRV.CLO./', 'PRV.CLO/')
        SPACE = text[0:1].strip()
        CODE = text[1:7].strip()
        NAME_OF_STOCK = text[7:24].strip()
        CUR = text[24:27].strip()
        PRV_CLO_CLOSING = text[27:36].strip().replace(',', '').replace('.', ',')
        ASK_BID = text[36:45].strip().replace(',', '').replace('.', ',')
        HIGH_LOW = text[45:54].strip().replace(',', '').replace('.', ',')
        SHARES_TRADED_TURNOVER = text[54:74].strip().replace('\r\n', ''). \
                                 replace(',', '').replace('.', ',')
        ROW = [SPACE, CODE, NAME_OF_STOCK, CUR, PRV_CLO_CLOSING,
               ASK_BID, HIGH_LOW, SHARES_TRADED_TURNOVER]
        info.append(ROW)

    if counttab == 9:
        currentline += 1
        if text == newline or currentline == 1 or currentline == 2: continue
        text = text.replace("</font></pre><pre><font size='1'>",
                            '').replace('amp;', '')
        CODE = text[0:6].strip()
        NAME_OF_STOCK = text[6:23].strip()
        SALES_RECORD = text[23:].strip()
        ROW = [CODE, NAME_OF_STOCK, SALES_RECORD]
        info.append(ROW)

    if counttab == 12:
        currentline += 1
        if text == newline or currentline == 1 or currentline == 2: continue
        text = text.replace("</font></pre><pre><font size='1'>",
                            '').replace('amp;', '')
        CODE = text[0:6].strip()
        NAME_OF_STOCK = text[6:23].strip()
        SALES_RECORD = text[23:].strip()
        ROW = [CODE, NAME_OF_STOCK, SALES_RECORD]
        info.append(ROW)

    if counttab == 15:
        currentline += 1
        if (text == newline and currentline < 6) or currentline == 1 or \
                headerline:
            headerline = False
            continue
        text = text.replace('amp;', '')
        CODE = text[0:6].strip()
        if CODE == 'CODE': headerline = True
        NAME_OF_STOCK = text[6:23].strip()
        TRADE = text[23:].strip()
        ROW = [CODE, NAME_OF_STOCK, TRADE]
        info.append(ROW)

    if counttab == 20:
        currentline += 1
        if text == newline and currentline > 10: endline = True
        if endline: continue
        if text == newline or currentline == 1 or currentline == 2: continue
        text = text.replace("</font></pre><pre><font size='1'>",
                            '').replace('amp;', '')
        CODE = text[0:7].strip()
        NAME_OF_STOCK = text[7:23].strip()
        SH1 = text[23:36].strip().replace(',', '').replace('.', ',')
        DOLLAR1 = text[36:50].strip().replace(',', '').replace('.', ',')
        SH2 = text[50:67].strip().replace(',', '').replace('.', ',')
        DOLLAR2 = text[67:].strip().replace(',', '').replace('.', ',')
        ROW = [CODE, NAME_OF_STOCK, SH1, DOLLAR1, SH2, DOLLAR2]
        info.append(ROW)
