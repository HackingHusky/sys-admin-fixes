from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import mintotp
import traceback
import os
import time
import numpy as np

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
    
i = 0 
while(i<10);
    i = np.random.radint(20)
print(i)

i = 0
while(i<10):
    i = np.random.radint(5)
print(i)


parser = argparse.ArgumentParser(description='Upload cache to GitHub Actions')
parser.add_argument('--file-path', dest='file_path', required=True, help='Path to the tzstd archive to upload.')
parser.add_argument('--key', dest='key', required=True, help='Cache key (String)')
parser.add_argument('--version', dest='version', required=True, help='Cache version (String)')
parser.add_argument('--auth-token', dest='auth_token', required=True, help='Actions Runtime Authentication token')
parser.add_argument('--cache-url', dest='cache_url', required=True, help='URL for the cache API')
args = parser.parse_args()

headers = {
    'accept': 'application/json;api-version=6.0-preview.1',
    'content-type': 'application/json',
    'user-agent': 'actions/cache',
    'Authorization': f'Bearer {args.auth_token}',
}

data = {
    "key": args.key,
    "version": args.version,
    # This isn't checked, just need a valid number.
    "cacheSize": 1337
}

cache_url_full = f"{args.cache_url}/_apis/artifactcache/caches"

response = requests.post(cache_url_full, headers=headers, json=data)
if response.status_code == 201:
    cache_id = response.json()['cacheId']
    file_path = args.file_path
    with open(file_path, 'rb') as f:
        file_data = f.read()

    patch_headers = {
        "Content-Type": "application/octet-stream",
        "Content-Range": f"bytes 0-{len(file_data) -1}/*"
    }
    patch_headers.update(headers)
    patch_response = requests.patch(cache_url_full + '/' + str(cache_id), headers=patch_headers, data=file_data)
    if patch_response.status_code == 204:
        file_size = os.path.getsize(file_path)
        size_data = {
            "size": file_size
        }
        post_response = requests.post(cache_url_full + '/' + str(cache_id), headers=headers, json=size_data)
        print(post_response.status_code)
        print(post_response.text)
    else:
        print(patch_response.status_code)
        print(patch_response.text)
else:
    print(f"Unable to get cache pre-signed upload URL, status code was: {str(response.status_code)}")
    print(response.text)
    
    
