import requests
from bs4 import BeautifulSoup
import geocoder
from time import sleep
import dataset
import datetime

def getll(address,county):
    try:
        g = geocoder.bing(address+", "+county+" Irerland",key='AjdRUJdlipFZJyYepG25haklqvZElnvYlMR9KjtyT3uk4N3afpPlPcaPKT7p65Ef')
        return g.json['lng'],g.json['lat']
    except:
        return 0,0


def get_data(url,table):
    while True:
        try:
            r = requests.get(url, verify=False)
            break
        except:
            sleep(5)
    soup = BeautifulSoup(r.text,'lxml')
    if len(soup.find('table',{'class':'resultsTable'}).find_all('tr'))<4:
        return None
    for tr in soup.find('table',{'class':'resultsTable'}).find_all('tr'):
        tds = tr.find_all('td')
        if len(tds)==3:
            saledate = tds[0].text
            saledate = datetime.datetime.strptime(saledate, '%d/%m/%Y')
            price = float(tds[1].text.replace(',','')[1:].replace('*',''))
            address = tds[2].text
            print(saledate,price,address)
            lng,lat = getll(address,'Cork')
            if lng==0:
                continue
            print(lng,lat)
            table.insert({'geom':"""{"type": "Point", "coordinates": [%s, %s]}""" % (str(lng),str(lat)),'description': address,'address':address,'price':price,'saledate':saledate,'created':datetime.datetime.now()})
    return True


db = dataset.connect('sqlite:///../db.sqlite3')
houses = db
table = db['housemap_homespot']

for i in range(1,1100,50):
    print(50+i)
    url = "https://www.propertypriceregister.ie/Website/npsra/PPR/npsra-ppr.nsf/PPR-By-Date&Start="+str(i)+"&Query=%5Bdt_execution_date%5D%3E=01/01/2019%20AND%20%5Bdt_execution_date%5D%3C01/01/2020%20AND%20%5Bdc_county%5D=Cork&County=Cork&Year=2019&StartMonth=&EndMonth=&Address="
    print(url)
    x = get_data(url, table)
    if x is None:
        break


