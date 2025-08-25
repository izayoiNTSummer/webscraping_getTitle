import time
import requests
from bs4 import BeautifulSoup

def main():
    with open("./URLfile/URLs.txt") as f:
        for url in f:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            title = soup.title.string
            print(title)
            time.sleep(1)
    print("処理終了")

if __name__ == "__main__":
    main()