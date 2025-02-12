from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import mintotp
import traceback
import os
import time

current_file_path = os.path.dirname(os.path.realpath(__file__))

def get_client_doc_from_json(client_id):
    try:
        json_file = os.path.join(current_file_path, 'credentials.json')
        with open(json_file) as f:
            data = json.load(f)
            return data[client_id]
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        traceback.print_exc()

def get_totp(userid):
    totp_key = get_client_doc_from_json(userid)['totp_key']
    return mintotp.totp(totp_key)

def disable_segment(driver, client_id):
    try:
        password = get_client_doc_from_json(client_id)['password']
        driver.get("https://console.zerodha.com/account/segment-activation")
        time.sleep(2)

        # Login
        driver.find_element(By.ID, "userid").send_keys(client_id)
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/form/div[4]/button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/form/div[1]/input").send_keys(get_totp(client_id))
        time.sleep(5)

        # Disable the NSE-FO segment
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[3]/div/div/div/label").click()
        time.sleep(1)

        # Clicking on continue
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/button").click()
        time.sleep(5)

        # Clicking on confirm-page continue button
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/div/form/div[2]/button[2]").click()
        time.sleep(10)
    except Exception as e:
        print(f"Error disabling segment: {e}")
        traceback.print_exc()
    finally:
        driver.quit()

def main(client_id):
    options = webdriver.ChromeOptions()
    options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    disable_segment(driver, client_id)

if __name__ == '__main__':
    main("<your client id here>")
