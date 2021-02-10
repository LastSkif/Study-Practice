from bs4 import BeautifulSoup
import urllib.request

currency = []
mass = []
buf = []
z = {}

def pars():
        page = BeautifulSoup(urllib.request.urlopen('http://coinmarketcap.com'), 'html.parser').find_all('td')

        for i in page:
                mass.append(i.get_text(separator = ' '))
        for t in mass:
                if t != '':
                        buf.append(t)
        for i in range(100):
                z[buf[i * 7 + 1]] = buf[i * 7 + 2:i * 7 + 4]

def search():
        
        values = ['Market Cap ', 'Price ']
        for i in range(2):
                print(values[i], currency[i])

pars();

while(1):
        print('\nEnter cryptocurrency: ')
        a = input()
        if a == "Exit":
                break
        if a in z:
                currency = z.get(a)
                search();
        else:
                print('\nDoes not exist')
