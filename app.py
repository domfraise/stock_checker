

import requests
from selenium import webdriver

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

stock_informer_base = "https://www.stockinformer.co.uk/"

ps5 = stock_informer_base + "checker-ps5-playstation-5-console"
zen3 = stock_informer_base + "checker-amd-ryzen-5000-zen-3-cpu"
series_x = stock_informer_base + "checker-xbox-series-x"
webhook = "https://maker.ifttt.com/trigger/Webhook_triggered/with/key/G2byZ4ydAByE8QhVTnbPi"




def check_stock(product_page_link, products_to_watch, driver):

    driver.get(product_page_link)
    response = driver.page_source

    html = BeautifulSoup(response, 'html5lib')
    products_to_check = products_to_watch
    in_stock = []
    for product in products_to_check:
        product_table_id = "TblProduct" + str(product)
        in_stock.extend(find_instock_sites_for_product(product_table_id, html))

    filtered_alerts = [item for item in in_stock if "StockX" not in item and "Ebay" not in item]
    print(product_page_link, filtered_alerts)
    return filtered_alerts


def send_webhook(data_to_send):
    if len(data_to_send) > 0:
        if (len(data_to_send) == 1):
            json = {"value1": data_to_send[0], }
        elif (len(data_to_send) == 2):
            json = {"value1": data_to_send[0], "value2": data_to_send[1], }
        elif (len(data_to_send) == 3):
            json = {"value1": data_to_send[0], "value2": data_to_send[1], "value3": data_to_send[2], }
        else:
            json = {"value1": ("\n".join(data_to_send)), }

        requests.post(webhook, data=json)


def find_instock_sites_for_product(product_table_id, soup):
    table = soup.find(id=product_table_id)
    try:
        rows = table.contents[0].contents
    except:
        print("Error parsing product table")
        print(soup.contents)
        return []
    in_stock = []
    for row in rows[2:]:  # ignore product name and whitespace row
        try:
            link = stock_informer_base + row.find_all("a")[0].get("href")
            site = row.find_all("img")[0].get("alt")
            metadata = ""
            for s in row.stripped_strings:
                metadata += s + " - "
                if "In Stock" in s:
                    in_stock.append(site + " - " + link + " - " + metadata)
        except:
            continue
    return in_stock



def check_all_stock(driver):
    print("Checking stock...")
    all_stock = []
    all_stock.extend(check_stock(ps5, [1, 2], driver))
    all_stock.extend(check_stock(zen3, [1, 2], driver))
    # all_stock.extend(check_stock(series_x, [1]))
    send_webhook(all_stock)


def handler(event, context):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options, service_log_path="/tmp", executable_path="/usr/bin/chromedriver")

    try:
        check_all_stock(driver)
    finally:
        driver.close()
    print("done!!")

if __name__ == '__main__':
    handler(None, None)
