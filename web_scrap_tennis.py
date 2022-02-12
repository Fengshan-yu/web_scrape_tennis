from bs4 import BeautifulSoup
import requests

url="https://www.espn.com/tennis/rankings"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")

ths = soup.find_all("th")
trs= soup.find_all("tr")

from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active

heading = [th.string for th in ths]
ws.append(heading)

for tr in trs:
    tds = tr.find_all("td")
    row = [td.get_text() for td in tds]
    ws.append(row)

wb.save("tennis_2022.xlsx")