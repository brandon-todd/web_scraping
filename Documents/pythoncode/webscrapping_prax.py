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
"""This function takes stock data from the yahoo finance most active webpage and dumps it into a text file in the same folder with the name and amount of change indicated"""
def stocks_check(t):
    print("I'm working...")
    """path to the chrome webdriver on personal device"""
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    
    """url for website to scrape"""
    url = 'https://finance.yahoo.com/most-active'
    driver.get(url.format(q='Car'))
    try:
        """wait for elements to be available before selecting. This statement takes all data available under the Change aria-label"""
        change = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='Change']"))
        )
        """wait for elements to be available before selecting. This statement takes all data available under the Name aria-label"""
        names = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='Name']"))
        )
        """Companies is an array of all available data under Name aria-label on the page"""
        Companies = driver.find_elements_by_css_selector("[aria-label='Name']")
        """changes is an array of all available data under Change aria-label on the page"""
        changes = driver.find_elements_by_css_selector("[aria-label='Change']")
        """get text for all company names and store in array lst1"""
        lst1 = [i.text for i in Companies]
        """get text for all changes and store in array lst2"""
        lst2 = [i.text for i in changes]
    
    except:
        """if something went wrong quit"""
        driver.quit()
    """update stock_history with the name and change"""
    for i in range(0, len(lst1)):
        if lst1[i] not in list(stock_history.keys()):
            stock_history.update({lst1[i]:[lst2[i]]})
        else:
            stock_history[lst1[i]].append(lst2[i])
    """print all data to screen"""
    print(stock_history)
    """store the data in a text file with json format"""
    with open('data.txt', 'a') as outfile:
        json.dump(stock_history, outfile)
    return "done"
"""schedule to run everyday just before 9 am"""
schedule.every().day.at("08:58").do(stocks_check,'It is 08:58')
"""run automatically at 8:58 am everyday"""
while True:
    schedule.run_pending()
    time.sleep(30)
