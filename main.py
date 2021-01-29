

import requests

from bs4 import BeautifulSoup

stock_informer_base = "https://www.stockinformer.co.uk/"

ps5 = stock_informer_base + "checker-ps5-playstation-5-console"
webhook = "https://maker.ifttt.com/trigger/Webhook_triggered/with/key/G2byZ4ydAByE8QhVTnbPi"

def open_browser(name):
    html = requests.get(ps5).content
    # print(html)
    soup = BeautifulSoup(html, 'html5lib')
    rows = soup.find(id="TblProduct1").contents[0].contents
    # print(rows[3])
    in_stock = []
    for row in rows[2:]:
        try:
            # print(row.prettify())
            link = stock_informer_base + row.find_all("a")[0].get("href")
            site = row.find_all("img")[0].get("alt")
            print(site, link)
            metadata = ""
            for s in row.stripped_strings:
                metadata += s + " - "
                if "In Stock" in s:
                    in_stock.append(site + " - " + link + " - " + metadata)
        except:
            continue

    filtered_alerts = [item for item in in_stock if "StockX" not in item and "Ebay" not in item]
    print(filtered_alerts)
    if len(filtered_alerts) > 0:
        if(len(filtered_alerts) == 1):
            json = {"value1": in_stock[0], }
        elif(len(filtered_alerts) == 2):
            json = {"value1": in_stock[0], "value2": in_stock[1], }
        elif(len(filtered_alerts) == 3):
            json = {"value1": in_stock[0], "value2": in_stock[1], "value3": in_stock[2], }
        else:
            json = {"value1": str(in_stock), }

        requests.post(webhook, data=json)



if __name__ == '__main__':
    open_browser('PyCharm')

