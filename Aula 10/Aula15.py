import requests

url = "https://joaobidu.com.br/horoscopo-do-dia/horoscopo-do-dia-para-leao/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as err:
    print(err)