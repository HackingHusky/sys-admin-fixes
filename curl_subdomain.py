import requests

with open("subdomain_list.txt", "r") as file:
    for subdomain in file:
        subdomain = subdomain.strip()
        url = f"https://{subdomain}.example.com"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"Subdomain found: {url}")
        except requests.exceptions.RequestException:
            pass  # Ignore unreachable subdomains