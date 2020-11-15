from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS
from win10toast import ToastNotifier
import time

# req website to access information
header = {"User-Agent": "Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/india/", headers=header)
html = urlopen(req)

# grabbing req data
obj = BS(html)
new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
new_deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

total_cases = obj.find("div", {"class": "maincounter-number"}).span.text.split()[0]
date = obj.find("div", {"class": "news_date"}).h4.text

# req win10 notifier
notifier = ToastNotifier()
message2 = "Corona Cases : "+total_cases
notifier.show_toast(title=date, msg=message2, duration=5, icon_path=r"C:\Users\adity\Documents\Python_Learning\PythonProjects\Projects\india.ico")

time.sleep(1)

message = "New Cases : "+new_cases+"\nNew Deaths : "+new_deaths
notifier.show_toast(title = "COVID-19 Update",msg = message,duration=5,icon_path=r"C:\Users\adity\Documents\Python_Learning\PythonProjects\Projects\covid19.ico")
