import requests
from bs4 import BeautifulSoup
import smtplib
# import time

URL = 'https://www.google.com/finance/quote/M%26M:NSE?hl=en'
URL2 = 'https://www.google.com/finance/quote/TCS:NSE?hl=en'
headers = { 
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def check_price():

    page = requests.get(URL, headers=headers)
    page2 = requests.get(URL2, headers=headers)

    # soup = BeautifulSoup('<html><body><div class="zzDege"></div><div class="zzDege"></div></body></html>')
    # soup.findAll('div',['class':"zzDege", "zzDege"])

    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(page2.content, 'html.parser')

    title = soup.find('div',{'class':"zzDege"}).get_text()
    title2 = soup2.find('div',{'class':"zzDege"}).get_text()

    # actualprice = soup.find('div', {'class':'_3I9_wc _2p6lqe'}).get_text().replace('.', '').replace('₹', '').replace(',', '').strip()

    price = soup.find('div', {'class':'YMlKec fxKbKc'}).get_text().replace('.', '').replace('₹', '').replace(',', '').strip()
    price2 = soup2.find('div', {'class':'YMlKec fxKbKc'}).get_text().replace('.', '').replace('₹', '').replace(',', '').strip()

    converted_price = float(price[0:4])
    converted_price2 = float(price2[0:4])

    print(title)
    print(title2)

    # print(actualprice)

    print(price)
    print(price2)

    print(converted_price)
    print(converted_price2)

    if(converted_price > 1000):
        send_mail1()

    if(converted_price < 1072):
        send_mail()
    
    if(converted_price2 < 3400):
        send_mail2()

    if(converted_price2 > 3295):
        send_mail3()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()
 
    server.ehlo()
    
    server.login('pragati.hiwale11.8.14@gmail.com', 'acimpmirqkfrhccx')

    subject = 'Mahindra Stock Price fell down!'
    body = 'check the stock link https://www.google.com/finance/quote/M%26M:NSE?hl=en'


    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('pragati.hiwale11.8.14@gmail.com', 'siddhivakhardar2002@gmail.com', msg)

    print('Hey! Mahindra2 has been sent.')

    server.quit()

def send_mail1():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.ehlo()
    
    server.login('pragati.hiwale11.8.14@gmail.com', 'acimpmirqkfrhccx')

    subject = 'Mahindra Stock Price Increased!'
    body = 'check the stock link https://www.google.com/finance/quote/M%26M:NSE?hl=en'


    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('pragati.hiwale11.8.14@gmail.com', 'siddhivakhardar2002@gmail.com', msg)

    print('Hey! Mahindra2 has been sent.')

    server.quit()

def send_mail2():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.ehlo()
    
    server.login('pragati.hiwale11.8.14@gmail.com', 'acimpmirqkfrhccx')

    subject = 'Tata Stock Price fell down!'
    body = 'check the stock link https://www.google.com/finance/quote/M%26M:NSE?hl=en'


    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('pragati.hiwale11.8.14@gmail.com', 'siddhivakhardar2002@gmail.com', msg)

    print('Hey! Tata1 has been sent.')

    server.quit()

def send_mail3():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()

    server.starttls()

    server.ehlo()
    
    server.login('pragati.hiwale11.8.14@gmail.com', 'acimpmirqkfrhccx')

    subject = 'Tata Stock Price have increased!'
    body = 'check the stock link https://www.google.com/finance/quote/M%26M:NSE?hl=en'


    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('pragati.hiwale11.8.14@gmail.com', 'siddhivakhardar2002@gmail.com', msg)

    print('Hey! Tata2 has been sent.')

    server.quit()

check_price()
# # time.sleep()    #86400
