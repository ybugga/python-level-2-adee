import requests
from bs4 import BeautifulSoup
import csv

URL = "https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations"

def get_countries():
    response = requests.get(URL)
    if response.status_code !=200:
        raise Exception("Failed to load page")

    with open("Project/countries.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "wikitable sortable sticky-header-multi plainrowheaders"})
    tablerows = table.find_all("tr")
    with open("Project/countries.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Country", "Membership Year", "Latitude", "Longitude", "URL"])
        for row in tablerows[1:]:
            th = row.find("th")
            country = th.text.strip()
            link = th.find("a")
            href = "https://en.wikipedia.org"+link.get("href")
            countryhtml = requests.get(href)
            countrysoup = BeautifulSoup(countryhtml.text, "html.parser")
            latitude = countrysoup.find("span", {"class": "latitude"})
            if latitude is not None:
                latitude = latitude.text.strip()
            else:
                print(country)
            longitude = countrysoup.find("span", {"class": "longitude"})
            if longitude is not None:
                longitude = longitude.text.strip()
            else:
                print(country)
            td = row.find("td")
            membership_year = td.text.strip()
            writer.writerow([country, membership_year, latitude, longitude, href])

    return

if __name__ == "__main__":
    get_countries()