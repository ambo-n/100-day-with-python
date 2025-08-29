from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://cookieclicker.gg/")
time.sleep(2)

cookie = driver.find_element(by=By.ID, value="bigCookie")
wait_time =5
time_to_check_cookies = time.time() + wait_time
timeout = time.time() +60*5

while True:
    try:
        cookie.click()
        if time.time() > time_to_check_cookies:
            cookies_text = driver.find_element(by=By.ID, value="cookies").text
            cookies_number = cookies_text.split()[0].replace(",","")
            print(f"Your have {cookies_number} cookies")
            best_item = None
            store_items = driver.find_elements(by=By.CSS_SELECTOR, value='div[id^="product"]')
            for store_item in reversed(store_items):
                if 'enabled' in store_item.get_attribute("class"): # type: ignore
                    best_item = store_item
                    break
            if best_item:
                try:
                    item_id = best_item.get_attribute("id")
                    purchased_item = driver.find_element(by=By.ID, value=item_id)
                    purchased_item.click()
                except NoSuchElementException:
                    print("No item found")
            time_to_check_cookies = time.time() +5
    except:
        print("Can't find cookie")
        break

    if time.time() > timeout:
        print(f"5 minutes have passed. You are making {cookies_text}")
        break

driver.quit()