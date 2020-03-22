import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.worldometers.info/coronavirus/")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("div", {"class": "maincounter-number"})
infected = element.text.strip()
final_infected = infected.replace(",", ".")
print(final_infected)
final_number = float(final_infected)
if final_number < 50.000:
    print("Situation is under control, number infected is {}".format(final_number))
elif final_number < 150.000:
    print("Situation is moderate, some area might be quarantined, number infected is {}".format(final_number))
else:
    print("Situation is critical. Require emergency quarantine. The number infected reached {}".format(final_number))