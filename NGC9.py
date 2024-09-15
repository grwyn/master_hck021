from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome("chromedriver.exe")
link = "https://coinmarketcap.com/"

page = requests.get(link)
print(page)