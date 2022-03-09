import requests
from selenium import webdriver

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
# options.headless = True

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)


driver.get("https://driverpracticaltest.dvsa.gov.uk/login")
wait = WebDriverWait(driver, 1000)
wait.until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))