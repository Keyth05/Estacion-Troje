import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_machangara_data(url: str) -> pd.DataFrame:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    return df
