from bs4 import BeautifulSoup
import requests
import json
from tqdm import tqdm
from pathlib import Path

def get_arabic_roots():
    
    URL = "https://www.lesanarab.com/letter/"
    page = requests.get(URL)
    save_path = Path(__file__).parent

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("a", href=True)
    words = []
    for tag in tqdm(results):
        if "letter" in tag["href"]:
            new_page = requests.get(requests.compat.urljoin(URL, tag["href"]))
            new_soup = BeautifulSoup(new_page.content, "html.parser")
            for t in tqdm(new_soup.find_all("a", href=True), leave=False):
                if "kalima" in t["href"]:
                    words.append(t.getText())

    with open(str(save_path / "words.json"), "w") as fp:
        json.dump(words, fp, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    # UnComment if you want to redownload the roots
    # get_arabic_roots()

    with open("words.json", "r") as fp:
        data = json.load(fp)
    print(f"Number of Arabic Language Roots is {len(data)} in Lesan El-Arab")
