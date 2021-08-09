import requests
proxies = {
    "http:":"125.88.122;84",
    "http:":"123.84.13.240:8118",
    "https:":"94.240.33.242:3128"
}

data = requests.get("http://icanhazip.com",proxies=proxies)
print(data.text)