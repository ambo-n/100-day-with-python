from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

list_of_events = driver.find_element(By.CLASS_NAME, value="event-widget")
# upcoming_events_list = list_of_events.text.split("\n")[2:]
# upcoming_events_dict = {}
# n=0
# for number in range(5):
#     upcoming_events_dict[number] = {"time":upcoming_events_list[n],"name":upcoming_events_list[n+1]}
#     n +=2

event_times = list_of_events.find_elements(By.TAG_NAME,"time")
event_names = list_of_events.find_elements(By.CSS_SELECTOR, ".menu li a")

upcoming_events_dict = {
    i: {"time": time.text, "name": name.text}
    for i, (time,name) in enumerate(zip(event_times, event_names))
}

print(upcoming_events_dict)
driver.quit()