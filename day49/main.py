from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os, time
from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_EMAIL = os.getenv("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD= os.getenv("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 10)

login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()

email_input = wait.until(EC.presence_of_element_located((By.ID,"email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL) #type: ignore

password_input = wait.until(EC.presence_of_element_located((By.ID,"password-input")))
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD) # type: ignore

submit_btn = driver.find_element(by=By.ID, value="submit-button")
submit_btn.click()

wait.until(EC.presence_of_element_located((By.ID,"schedule-page")))


today = datetime.now()
targeted_weekdays = [0,1]
targeted_weekdays_in_datetime = [today+timedelta(days=((weekday-today.weekday() +7)%7) or 7) for weekday in targeted_weekdays]
formatted_weekdays =[weekday.strftime("%a %b %d") for weekday in targeted_weekdays_in_datetime]

counters = {
    "new_booking":0,
    "already_booked":0,
    "waitlist":0
}
detailed_class_summary = "\n--- DETAILED CLASS LIST ---\n"


for weekday, formatted_weekday in zip(targeted_weekdays_in_datetime, formatted_weekdays):
    try:
        booking_button = driver.find_element(
            by=By.CSS_SELECTOR, 
            value=f'div[id*="{weekday.date()}-0700"] button') # type: ignore
        class_name = booking_button.find_element(
            By.XPATH, "ancestor::div/preceding-sibling::div/h3").text
        button_text = booking_button.text.strip()
        actions = {
            "Join Waitlist": ("✓ Joined waitlist", "new waitlist", "waitlist", True),
            "Waitlisted":("✓ Already on waitlist","already on waitlist","already_booked", False),
            "Booked":("✓ Already booked", "already booked","already_booked", False),
            "Book Class":("✓ Booked", "new booking", "new_booking", True)
        }
        
        if button_text in actions:
            msg, summary_label, counter_key, should_click = actions[button_text]
            if should_click:
                booking_button.click()
                time.sleep(0.5)
            print(f"{msg}: {class_name} on {formatted_weekday}")
            counters[counter_key] += 1
            detailed_class_summary += f"[{summary_label.title()}] {class_name} on {formatted_weekday}\n"
        else:
            print(f"⚠ Unknown button state '{button_text}' for {class_name}")
    except NoSuchElementException:
        print("Can't find the button")


total_classes = counters["new_booking"]+counters["waitlist"]+counters["already_booked"]

# print(f"""
# --- BOOKING SUMMARY ---
# New Bookings           : {counters['new_booking']}
# New Waitlist Entries   : {counters['waitlist']}
# Already Booked/Waitlist: {counters['already_booked']}
# Total Tue & Thu 6pm    : {total_classes}
# """)
print(f"""
--- Total Tue & Thu 6pm    : {total_classes} ---
""")

#  --- Go To Booking Page ---

driver.find_element(by=By.ID, value="my-bookings-link").click()
wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

all_cards = driver.find_elements(by=By.CSS_SELECTOR, value='[class*="MyBookings_bookingDetails"]')
if not all_cards:
    print("No classes found")
else:
    print("\n --- VERIFYING ON MY BOOKINGS PAGE ---")
    for card in all_cards:
        try:
            h3 = card.find_element(By.TAG_NAME, "h3").text
            print(f"✓ Verified: {h3}")
        except NoSuchElementException:
            print("No class name found")

print(f"""
--- VERIFICATION RESULT ---
Expected: {total_classes} bookings
Found: {len(all_cards)} bookings
""")

if total_classes == len(all_cards):
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_classes-len(all_cards)} bookings")

# print(detailed_class_summary)