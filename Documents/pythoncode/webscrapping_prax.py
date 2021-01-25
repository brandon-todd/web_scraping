from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import selenium
from selenium import webdriver
import time
import io
import schedule
import time
stock_history = {}
def stocks_check(t):
    print("I'm working...")
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    
    url = 'https://finance.yahoo.com/most-active'
    driver.get(url.format(q='Car'))
    try:
        change = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='Change']"))
        )
        names = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='Name']"))
        )
        Companies = driver.find_elements_by_css_selector("[aria-label='Name']")
        changes = driver.find_elements_by_css_selector("[aria-label='Change']")
        lst1 = [i.text for i in Companies]
        lst2 = [i.text for i in changes]
    
    except:
        driver.quit()

    for i in range(0, len(lst1)):
        if lst1[i] not in list(stock_history.keys()):
            stock_history.update({lst1[i]:[lst2[i]]})
        else:
            stock_history[lst1[i]].append(lst2[i])
    
    print(stock_history)
    with open('data.txt', 'a') as outfile:
        json.dump(stock_history, outfile)
    return "done"

schedule.every().day.at("08:58").do(stocks_check,'It is 08:58')

while True:
    schedule.run_pending()
    time.sleep(30)
